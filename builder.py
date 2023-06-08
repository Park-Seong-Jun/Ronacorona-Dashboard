from dash import html


def make_table(dataframe):
    return html.Table(
        [
            html.Thead(
                [
                    html.Tr(
                        [
                            html.Th(column_name.replace("_", " "))
                            for column_name in dataframe.columns
                        ],
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(4, 1fr)",
                            "fontWeight": "600",
                            "fontSize": 22,
                        },
                    )
                ],
                style={"display": "block", "marginBottom": 25},

            ),
            html.Tbody(
                [
                    html.Tr(
                        [
                            html.Td(value_column, style={
                                "textAlign": "center"})
                            for value_column in value
                        ],
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(4, 1fr)",
                            "border-top": "1px solid white",
                            "padding": "30px 0px",
                        },

                    )
                    for value in dataframe.values
                ],
                style={"maxHeight": "50vh", "display": "block",
                       "overflow": "scroll", },

            ),
        ], style={"color": "white"}
    )


""" def make_table(dataframe):
    return [html.Table(
        [html.Thead(
            [html.Tr(
                [html.Th(header_index.replace("_", " "), style={"padding": "10px"})
                 for header_index in dataframe.columns])
             ],
            style={

                "backgroundColor": "#111111",
                "borderBottom": "1px solid white",
                "borderTop": "1px solid white",
                "fontWeight": "600",
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)"
            }),
         html.Tbody(
            [html.Tr(
                [html.Td(data, style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(4, 1fr)",
                    "borderBottom": "1px solid white",
                    "padding": "30px 0px",
                    "textAlign": "center"})

                    for data in data_row]) for data_row in dataframe.values
             ])
         ], style={

             "fontSize": "22px",
             "maxHeight": "50vh",



             "color": "white",



        }

    )]
 """
