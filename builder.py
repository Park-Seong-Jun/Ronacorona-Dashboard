from dash import html


def make_table(dataframe):
    return [html.Table(
        [html.Thead(
            [html.Tr(
                [html.Th(header_index, style={"borderBottom": "1px solid #444444", "padding": "10px"})
                 for header_index in dataframe.columns])
             ]),
         html.Tbody(
            [html.Tr(
                [html.Td(data, style={"borderBottom": "1px solid #444444", "padding": "10px"})
                 for data in data_row]) for data_row in dataframe.values
             ])
         ], id="country_total_daily", style={"width": "100%", "borderTop": "1px solid #444444", "borderCollapse": "collapse", "color": "white"}

    )]
