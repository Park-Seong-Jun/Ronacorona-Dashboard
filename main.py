# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
from data import countries_df
from builder import make_table


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(

    [
        html.Header(
            [html.H1("Corona Dashboard", style={
                "fontSize": 50, "color": "white"})],
            style={
                "textAlign": "center",
                "padding": "50px",
                "border": "1px solid white"
            }

        ),
        html.Div(
            [html.Div(style={"width": "50%", "border": "1px solid white"}),
             html.Div(make_table(countries_df), style={"height": "300px", "width": "100%", "overflow": "auto"})], style={"border": "1px solid white", "display": "flex"})
    ], style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",

        "fontFamily": "Open Sans, sans-serif",


    }
)

if __name__ == "__main__":
    app.run_server(debug=True)
