import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import csv

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=["url('/assets/boostrap.css')"])

server = app.server

# FORMS
modal_form_body = dbc.Form([  # Signup form
        dbc.FormGroup([  # First name input
            dbc.Label("Navn",
                      html_for="name_row",
                      style={"color": "#fafafa"}),
            dbc.Input(type="text",
                      id="modal_form_name",
                      placeholder="... Skriv inn navnet ditt her",
                      style={"width": "100%",
                             "box-shadow": "0px 2px black"})
        ]),
        dbc.FormGroup([
            dbc.Label("E-postadresse",
                      html_for="email_row",
                      style={"color": "#fafafa"}),
            dbc.Input(type="email", id="modal_form_email",
                      placeholder="... Skriv inn din e-postadresse her",
                      style={"width": "100%",
                             "box-shadow": "0px 2px black"})
        ]),
        dbc.Button("Send inn",
                   color="warning",
                   className="mt-4 mb-2",
                   style={"box-shadow": "0px 2px black"})
    ])

main_form_body = dbc.Form([  # Signup form
    dbc.FormGroup([  # First name input
        dbc.Label("Navn",
                  html_for="name_row",
                  style={"color": "#fafafa"}),
        dbc.Input(type="text",
                  id="main_form_name",
                  placeholder="... Skriv inn navnet ditt her",
                  style={"width": "80%",
                         "box-shadow": "0px 2px black"})
    ]),
    dbc.FormGroup([
        dbc.Label("E-postadresse",
                  html_for="email_row",
                  style={"color": "#fafafa"}),
        dbc.Input(type="email", id="main_form_email",
                  placeholder="... Skriv inn din e-postadresse her",
                  style={"width": "80%",
                         "box-shadow": "0px 2px black"})
    ]),
    dbc.Button("Send inn",
               color="warning",
               className="mt-4 mb-2",
               style={"box-shadow": "0px 2px black"},
               id="submit_main_form_button",
               size="lg")
    ])


body = dbc.Container(  # Main container
    fluid=True,
    children=[
        dbc.Row(
            [  # Banner first row
                dbc.Col(  # Banner first column
                    lg=4,
                    md=10,
                    children=[
                        html.H1(
                            "Plukk.",
                            className="mb-5 mt-5",
                            style={"color": "white",
                                   "text-shadow": "0px 3px black",
                                   "text-align": "center"},
                        ),
                        html.P(
                            """\
Plukk gjør det morsomt å plukke søppel.\n Med din egen QR-kode, en mobil \
og egne poser kan store og små konkurrere mot venner, samarbeide, \
vinne dritkule premier og få belønninger.""",
                            style={"color": "#D6D6D6",
                                   "text-align": "center"},
                        )
                ]),
                dbc.Col(  # Banner second column
                    [html.Img(src="/assets/images/three_phones_2.png",
                              width="100%")],
                    lg="5",
                    md="10",
                    className="mb-5"
                ),
            ],
            style={
                "background-image": "url('/assets/images/lofoten_beach_background_blur.jpg')",
                "background-repeat": "no-repeat",
                "background-size": "cover",
                "background-attachment": "fixed",
                "min-height": "700px"
            },
            align="center",
            justify="around"
        ),  # Banner row closing parantheses
        dbc.Row(
            [  # About-row
                dbc.Col(  # About-row: Main col
                    [
                        dbc.Col(
                            [  # Main col: Heading
                                html.H2("Slik fungerer PLUKK.", style={"text-align": "center"})
                            ],
                            width=12,
                            className="mb-5 mt-5",
                        ),
                        dbc.Row(
                            [  # Main col: Row for cards
                                dbc.Col(
                                    [  # First card
                                        html.Img(
                                            src="/assets/images/about_card.png",
                                            width="100%",
                                            className="mb-4 mt-2"
                                        )
                                    ],
                                    lg=4,
                                    md=8
                                ),  # First card closing parantheses
                                dbc.Col(
                                    [  # Second card
                                        html.Img(
                                            src="/assets/images/about_card_2.png",
                                            width="100%",
                                            className="mb-4",
                                        ),
                                    ],
                                    lg=4,
                                    md=8
                                ),  # Second card closing parantheses
                                dbc.Col(  # Third card
                                    [
                                        html.Img(
                                            src="/assets/images/about_card_3.png",
                                            width="100%",
                                            className="mb-4",
                                        ),
                                    ],
                                    lg=4,
                                    md=8
                                ),  # Third card col closing parantheses
                            ],
                            justify="around",
                            align="center",
                            style={"text-align": "left"},
                            className="mb-5"
                        ),  # Card row closing parantheses
                    ]
                )
            ],  # Properties of about-row
            style={"min-height": "700px"},
            align="center",
            justify="center",
        ),  # About row closing parantheses
        dbc.Row(
            [  # Feature-row
                dbc.Col(  # Feature-row: Main col
                    [
                        dbc.Col(
                            [  # Main col: Heading
                                html.H2(
                                    "Hva kan du glede deg til?",
                                    style={"text-align": "center",
                                           "color": "white",
                                           "text-shadow": "0px 2px black"},
                                )
                            ],
                            width=12,
                            className="mt-5 mb-3",
                        ),
                        dbc.Col(
                            [  # Main col: Paragraph
                                html.P(
                                    """\
PLUKK kommer med mange kule funksjoner som eget poengsystem, felles events, \
personlige utfordringer, lederlister og et skattekart som viser hvor plastavfallet befinner\
 seg i dag.
\nHer er noen eksempler:""",
                                    style={"text-align": "center",
                                           "color": "silver"},
                                    className="mt-2 mb-4",
                                )
                            ],
                            lg={"size": 6, "offset": 3},
                            md={"size": 10, "offset": 1},
                            className="mb-5",
                        ),
                        dbc.Row(
                            [  # Main col: Row for cards
                                dbc.Col(
                                    [  # First card
                                        html.Img(
                                            src="/assets/images/feature_achievements_2.png",
                                            width="100%")
                                    ],
                                    lg=4,
                                    md=7
                                ),  # First card closing parantheses
                                dbc.Col(
                                    [  # Second card
                                        html.Img(
                                            src="/assets/images/feature_map_2.png",
                                            width="100%"
                                        )
                                    ],
                                    lg=4,
                                    md=7
                                ),  # Second card closing parantheses
                                dbc.Col(  # Third card
                                    [
                                        html.Img(
                                            src="/assets/images/feature_mypage_2.png",
                                            width="100%"
                                        )
                                    ],
                                    lg=4,
                                    md=7
                                ),  # Third card col closing parantheses
                            ],
                            justify="around",
                            align="start",
                            style={"text-align": "center"},
                        ),  # Card row closing parantheses
                    ]
                )
            ],  # Properties of feature row
            style={
                "min-height": "1000px",
                "background-image": "url('assets/images/green_background.png')",
                "background-size": "cover",
                "background-repeat": "no-repeat",
                "background-attachment": "fixed"
            },
            align="start",
            justify="center"
        ),  # Feature row closing parantheses
        dbc.Row([  # Signup row
            dbc.Col([  # First col for signup form
                html.H2("Bli først til å teste Plukk!",
                        className="mb-4 mt-5",
                        style={"text-shadow": "0px 2px black"}),
                html.P("""Fyll ut skjemaet under for å få informasjon om\
                 utviklingen av Plukk eller være én av\
                 de første til å teste appen.""",
                       className="mb-4",
                       style={"color": "teal"}),
                main_form_body  # Gets the form body from resources.py
            ],  # Signup col properties
                lg=6,
                md=8,
                style={"color": "white",
                       "font-size": "1.2rem"},
                className="mt-5 mb-5"
            )
        ],  # Signup row properties
            align="center",
            justify="center",
            style={"min-height": "800px",
                   "background-color": "#3b3b3b",
                   "font-family": "Courier New"}
        ),
        dbc.Row(
            [  # Story row
                dbc.Col([
                    html.H2("Historien bak Plukk",
                            className="mb-5 mt-5",
                            style={"text-shadow": "0px 2px black"}),
                    html.P(
"""En kald februarnatt i 2019 satte et team fra konsulentselskapet Bouvet seg \
ned for være med å løse et enormt problem: Plast i havet.\n
I tillegg til et enormt problem hadde de 24 timer på å komme frem til en løsning.\n Med hjelp \
fra Plastkoordinator i Oslo, Anja Stokkan, ble Plukk løsningen til teamet. \
Appen hadde som hensikt å motivere folket til å plukke plast og søppel i \
naturen ved å skape et pantesystem som belønnet dem for strevet.\n
Dette er Plukk.
                           """)
                     ],  # Story first col
                    lg=5,
                    md=9,
                    align="center",
                    style={"text-align": "left",
                           "color": "#D6D6D6"},
                    className="mb-5 mt-5"
                ),
                dbc.Col(  # Story second col
                    [html.Img(src="/assets/images/bouvet_hackathon.jpg",
                              width="100%",
                              style={"border-radius": "20px",
                                     "border": "solid",
                                     "border-color": "#ffcc00"})],
                    lg=5,
                    md=7,
                    style={"text-align": "center"},
                    className="mt-3 mb-5"
                )
                # Closing parantheses of Story row
            ],
            style={
                "min-height": "700px",
                "background-image": "url('/assets/images/green_background.png')",
                "background-repeat": "no-repeat",
                "background-size": "cover",
                "background-attachment": "fixed",
                "color": "#fafafa"
            },
            align="center",
            justify="around",
            # Footer row properties
        )
    ]  # Container children closure
)  # Container end bracket


# CALLBACKS
# Open modal 1
@app.callback(
    Output("modal_form", "is_open"),
    [Input("open_modal_form_button", "n_clicks"),
     Input("close_modal_form_button", "n_clicks")],
    [State("modal_form", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# Submit forms
@app.callback(
Output("modal_form_response", "children"),
    [Input("submit_modal_form_button", "n_clicks")],
    [State("modal_form_name", "value"),
     State("modal_form_email", "value")])
def update_output(n_clicks, input1):
    return input1


app.layout = html.Div([body])  # Define layout


if __name__ == "__main__":  # Run program
    app.run_server(debug=True)
