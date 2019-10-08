import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
"""
navbar = dbc.NavbarSimple(
    children=[dbc.NavItem(dbc.NavLink("Last ned appen", href="#"))],
    brand="PLUKK by Bouvet",
    brand_href="#",
    sticky="top",
    color="dark",
    dark=True,
    style={"font-family": "helvetica"}
)
"""
body = dbc.Container(  # Main container
    fluid=True,
    children=[
        dbc.Row(
            [  # Banner first row
                dbc.Col(  # Banner first column
                    className="ml-5",
                    lg=5,
                    md=8,
                    sm=8,
                    children=[
                        html.H1(
                            "PLUKK.",
                            className="mb-5",
                            style={"color": "white",
                                   "font-size": "4rem"},
                        ),
                        html.P(
                            """\
PLUKK gjør det morsomt å plukke søppel. Med din egel QR-kode, mobilen din 
og dine egne poser kan du konkurrere mot vennene dine, 
vinne dritkule premier og få belønninger.""",
                            style={"color": "white"},
                        ),
                        dbc.Row(
                            [  # Row for buttons within column 1
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "Last ned appen",
                                            # Download button
                                            color="info",
                                            size="lg",
                                            outline=False
                                        )
                                    ],
                                    width=6,
                                ),
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "Lær mer om PLUKK",
                                            # Read more button
                                            color="light",
                                            size="lg",
                                            outline=True
                                        )
                                    ],
                                    width=6,
                                ),
                            ],
                            className="mt-5",
                            justify="center",
                            align="center",
                        ),
                    ],
                ),
                dbc.Col(  # Banner second column
                    [html.Img(src="/assets/images/three_phones_2.png",
                              width="100%")],
                    width="5",
                ),
            ],  # Banner row children closure
            style={
                "background-image": "url('/assets/images/lofoten_beach_background.png')",
                "min-height": "650px",
                "font-family": "courier"},
            justify="around",
            align="center",
        ),  # Banner row closing parantheses
        dbc.Row(
            [  # About-row
                dbc.Col(  # About-row: Main col
                    [
                        dbc.Col(
                            [  # Main col: Heading
                                html.H1(
                                    "Slik fungerer PLUKK.",
                                    style={"text-align": "center"},
                                )
                            ],
                            width=12,
                            className="mb-5"
                        ),
                        dbc.Row(
                            [  # Main col: Row for cards
                                dbc.Col(
                                    [  # First card
                                        html.Img(
                                            src="/assets/images/bottles_quadratic.png",
                                            width="100%",
                                            className="mb-5"
                                        ),
                                        html.H4(
                                            "1. Plukk søppel i Plukkposer."
                                        )
                                    ],
                                    lg=3
                                ),  # First card closing parantheses
                                dbc.Col(
                                    [  # Second card
                                        html.Img(
                                            src="/assets/images/bin_bag.png",
                                            width="100%",
                                            className="mb-5"
                                        ),
                                        html.H4(
                                            "2. Scann din personlige QR-kode og kast søpla på best mulig sted."
                                        )
                                    ],
                                    lg=3
                                ),  # Second card closing parantheses
                                dbc.Col(  # Third card
                                    [
                                        html.Img(
                                            src="/assets/images/trophy.png",
                                            width="100%",
                                            className="mb-5"
                                        ),
                                        html.H4(
                                            "3. Få en poengsum på din konto og bruk dem på markedsplassen vår!"
                                        ),
                                    ],
                                    lg=3
                                ),  # Third card col closing parantheses
                            ],
                            justify="around",
                            align="start",
                            style={"text-align": "left"}
                        )  # Card row closing parantheses
                    ])
            ],  # Properties of about-row
            style={"min-height": "700px",
                   "font-family": "courier"},
            align="center",
            justify="center",
        ),  # About row closing parantheses
        dbc.Row(
            [  # Feature-row
                dbc.Col(  # Feature-row: Main col
                    [
                        dbc.Col(
                            [  # Main col: Heading
                                html.H1(
                                    "Hva kan du glede deg til?",
                                    style={"text-align": "center",
                                           "color": "white"},
                                )
                            ],
                            width=12,
                            className="mt-5",
                        ),
                        dbc.Col(
                            [  # Main col: Paragraph
                                html.P(
                                    """\
PLUKK gjør det morsomt å plukke søppel. Med din egel QR-kode, mobilen din 
og dine egne poser kan du konkurrere mot vennene dine, 
vinne dritkule premier og få belønninger.""",
                                    style={"text-align": "center",
                                           "color": "white"},
                                    className="mt-5 mb-5"
                                )
                            ],
                            lg={"size": 6, "offset": 3},
                            md={"size": 8, "offset": 2},
                            className="mb-8",
                        ),
                        dbc.Row(
                            [  # Main col: Row for cards
                                dbc.Col(
                                    [  # First card
                                        html.Img(
                                            src="/assets/images/feature_achievements_glare.png",
                                            width="100%"
                                        ),
                                        html.H4(
                                            "Personlige utfordringer og belønninger",
                                            className="mt-3 mb-2",
                                            style={"color": "white"}
                                        )
                                    ],
                                    lg=3
                                ),  # First card closing parantheses
                                dbc.Col(
                                    [  # Second card
                                        html.Img(
                                            src="/assets/images/feature_map.png",
                                            width="100%"
                                        ),
                                        html.H4(
                                            "Et skattekart for plast og Plukk-events",
                                            className="mt-3 mb-2",
                                            style={"color": "white"}
                                        )
                                    ],
                                    lg=3
                                ),  # Second card closing parantheses
                                dbc.Col(  # Third card
                                    [
                                        html.Img(
                                            src="/assets/images/feature_achievements_glare.png",
                                            width="100%"
                                        ),
                                        html.H4(
                                            "Et råkult poengsystem med premier",
                                            className="mt-3 mb-2",
                                            style={"color": "white"}
                                        )
                                    ],
                                    lg=3
                                ),  # Third card col closing parantheses
                            ],
                            justify="around",
                            align="start",
                            style={"text-align": "center"}
                        )  # Card row closing parantheses
                    ])
            ],  # Properties of feature row
            style={"min-height": "1200px",
                   "background-image": "url('assets/images/green_background.png')",
                   "font-family": "courier"},
            align="center",
            justify="center",
        ),  # Feature row closing parantheses
        dbc.Row([  # Footer row
            dbc.Col([  # Footer first col
                html.P("Historien")
            ],  lg=4,
                align="center",
                style={"text-align": "center"}
            ),
            dbc.Col([  # Footer second col
                html.P("Footer text")
            ],
                lg=4,
                align="center",
                style={"text-align": "center"})
            # Closing parantheses of Footer row
        ],
            style={"min-height": "300px",
                   "background-image": "url('assets/images/green_background.png')"},
            align="center",
            justify="center",
            # Footer row properties
        )
    ],  # Container children closure
)  # Container end bracket

app.layout = html.Div([body])

if __name__ == "__main__":
    app.run_server(debug=True)
