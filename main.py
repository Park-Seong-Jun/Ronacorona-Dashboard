# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
from data import countries_df
from data import totals_df
from builder import make_table


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(__name__, external_stylesheets=stylesheets)

bubble_map = px.scatter_geo(countries_df,
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
                            projection="natural earth"

                            )

total_bar_chart = px.bar(totals_df, x='Condition',
                         y='Count', title="Total Cases")

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
            [html.Div(
                [dcc.Graph(figure=bubble_map)]),
             html.Div(make_table(countries_df))], style={"display": "flex", }),

        html.Div(
            [dcc.Graph(figure=total_bar_chart)]
        )
    ], style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",

        "fontFamily": "Open Sans, sans-serif",


    }
)

if __name__ == "__main__":
    app.run_server(debug=True)
