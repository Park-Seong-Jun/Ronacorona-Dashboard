# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
from data import countries_df
from data import make_daily_df
from data import totals_df
from data import dropDown_options
from builder import make_table


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(__name__, external_stylesheets=stylesheets)

bubble_map = px.scatter_geo(countries_df,
                            title="Cases by Country",
                            size="Confirmed",
                            size_max=40,
                            hover_name='Country_Region',
                            hover_data={

                                "Country_Region": False,
                                'Confirmed': ":,",
                                'Deaths': ":,",
                                'Recovered': ":,"},
                            color="Confirmed",
                            locations="Country_Region",
                            locationmode="country names",
                            template="plotly_dark",
                            projection="natural earth",
                            color_continuous_scale=px.colors.sequential.Oryel

                            )
bubble_map.update_layout(margin=dict(l=0, r=0, b=0, t=25))

total_bar_chart = px.bar(totals_df,
                         x='Condition',
                         y='Count',
                         title="Total Cases",
                         template="plotly_dark",
                         hover_data={
                             "Condition": False,
                             'Count': ":,"
                         },
                         )


total_bar_chart.update_layout(xaxis=dict(
    title="CONDITION"), yaxis=dict(title="COUNT"))

def make_line_chart(country=None):
    df = make_daily_df(country)
    if country is None:
        chart_title = "World daily Cases"
    else:
        chart_title=f'{country} daily Cases'
    fig = px.line(df, x="Date", y=["confirmed_total","deaths_total","recovered_total"],
                  title=chart_title,
                  labels={"value":"Cases",
                          "variable":"Condition"
                  },
                  hover_name='Date',
                  hover_data={"Date": False,
                              'value': ":,"},

                 )
    return fig

#HTML 변환 부분

app.layout = html.Div(

    [
        html.Header(
            [html.H1("Corona Dashboard", style={
                "fontSize": 50, "color": "white"})],
            style={
                "textAlign": "center",
                "padding": "50px",

            }

        ),
        html.Div(
            [
                dcc.Graph(figure=bubble_map,style={
                    "gridColumn":"span 3"
                }),
                html.Div(make_table(countries_df), style={"padding": "40px","gridColumn":"span 2"}),
                dcc.Graph(figure=total_bar_chart,style={
                    "gridColumn":"span 2"
                }),
                html.Div(
                    [
                        dcc.Dropdown(
                            id='country-input',
                            options=[
                            
                                {'label': country_name, 'value': country_name}
                                for country_name in dropDown_options
                            ],
                            style={"color":"black"}
                        
                        ),
                        dcc.Graph(id="country-output")
                       
                    ],style={"gridColumn":"span 3"}
                )
            ],id="main_part", style={
                "display":"grid",
                "gridTemplateColumns":"repeat(5,1fr)",
                "gap":"50"
            }
        )
    ], style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "fontFamily": "Open Sans, sans-serif",
        "color":"white"
    }
)

@app.callback(Output("country-output","figure"),[Input("country-input","value")])
def update_bar_chart(value):
    return make_line_chart(value)

if __name__ == "__main__":
    app.run_server(debug=True)
