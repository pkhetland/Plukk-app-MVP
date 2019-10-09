import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import csv

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])

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
                      style={"width": "80%",
                             "box-shadow": "0px 2px black"})
        ]),
        dbc.FormGroup([
            dbc.Label("E-postadresse",
                      html_for="email_row",
                      style={"color": "#fafafa"}),
            dbc.Input(type="email", id="modal_form_email",
                      placeholder="... Skriv inn din e-postadresse her",
                      style={"width": "80%",
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
               id="submit_main_form_button")
    ])


body = dbc.Container(  # Main container
    fluid=True,
    children=[
        dbc.Row(
            [  # Banner first row
                dbc.Col(  # Banner first column
                    lg=4,
                    md=6,
                    sm=12,
                    children=[
                        html.H1(
                            "Plukk.",
                            className="mb-5 mt-5",
                            style={"color": "white",
                                   "font-size": "4rem",
                                   "text-shadow": "0px 3px black",
                                   "text-align": "center"},
                        ),
                        html.P(
                            """\
Plukk gjør det morsomt å plukke søppel.\n Med din egen QR-kode, en mobil \
og egne poser kan store og små konkurrere mot venner, samarbeide, \
vinne dritkule premier og få belønninger.""",
                            style={"color": "#fafafa",
                                   "text-align": "center"},
                        ),
                        dbc.Row([
                            dbc.Col([
                                dbc.Button(  # Download button
                                    "Last ned appen",
                                    id="open_modal_form_button",
                                    color="warning",
                                    size="lg",
                                    style={"box-shadow": "0px 2px black"},
                                    className="mb-4"
                                ),
                                dbc.Modal(
                                    [
                                        dbc.ModalBody([
                                            html.H2(
                                                "Takk for interessen!",
                                                style={"color": "#f5a818"}
                                            ),
                                            html.H5("""
    Plukk er ikke helt ferdig ennå, men fyll ut e-post og navn under, så kan du \
    være én av de første til å teste den!\n Vi holder deg også oppdatert på \
    utviklingen fremover.""",
                                                    style={"color": "#fafafa"},
                                                    className="mt-3 mb-3"),
                                            modal_form_body,  # Gets the form body
                                            html.Div(id="modal_form_response"),
                                            dbc.Button("Lukk vinduet",
                                                       id="close_modal_form_button",
                                                       className="mt-4",
                                                       color="danger",
                                                       size="sm",
                                                       style={
                                                           "box-shadow": "0px 2px black"})
                                        ], style={"background-image": "url('assets/images/green_striped_background.jpg')",
                                                  "border": "solid 5px #3b3b3b"}
                                        ),
                                    ],
                                    id="modal_form",
                                    size="md",
                                    scrollable=True,
                                    centered=True,
                                    style={"color": "#fafafa",
                                           "font-family": "courier"}
                                )],
                                lg=7,
                                md=7,
                                sm=5,
                                xs=6,
                                className="mt-5"
                            )
                        ],
                        align="center",
                        justify="center"
                    )
                ]),
                dbc.Col(  # Banner second column
                    [html.Img(src="/assets/images/three_phones_2.png",
                              width="100%")],
                    lg="5",
                    md="5",
                    sm="9",
                    className="mb-5"
                ),
            ],
            style={
                "background-image": "url('/assets/images/lofoten_beach_background_blur.jpg')",
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
                                html.H1("Slik fungerer PLUKK.", style={"text-align": "center"})
                            ],
                            lg=12,
                            md=12,
                            sm=12,
                            className="mb-5 mt-5",
                        ),
                        dbc.Row(
                            [  # Main col: Row for cards
                                dbc.Col(
                                    [  # First card
                                        html.Img(
                                            src="/assets/images/pick_garbage_boy.png",
                                            width="100%",
                                            className="mb-4"
                                        ),
                                        html.H4("1. Plukk søppel i Plukkposer.",
                                                style={"text-align": "center"})
                                    ],
                                    lg=3,
                                    md=3,
                                    sm=7,
                                    xs=7
                                ),  # First card closing parantheses
                                dbc.Col(
                                    [  # Second card
                                        html.Img(
                                            src="/assets/images/bag_bin.png",
                                            width="100%",
                                            className="mb-4",
                                        ),
                                        html.H4(
                                            "2. Scann din personlige QR-kode og kast søpla på best mulig sted.",
                                            style={"text-align": "center"}
                                        ),
                                    ],
                                    lg=3,
                                    md=3,
                                    sm=7,
                                    xs=7
                                ),  # Second card closing parantheses
                                dbc.Col(  # Third card
                                    [
                                        html.Img(
                                            src="/assets/images/trophy.png",
                                            width="100%",
                                            className="mb-4",
                                        ),
                                        html.H4(
                                            "3. Få en poengsum på din konto og bruk dem på markedsplassen vår!",
                                            style={"text-align": "center"}
                                        ),
                                    ],
                                    lg=3,
                                    md=3,
                                    sm=7,
                                    xs=7
                                ),  # Third card col closing parantheses
                            ],
                            justify="around",
                            align="start",
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
                                html.H1(
                                    "Hva kan du glede deg til?",
                                    style={"text-align": "center",
                                           "color": "white",
                                           "text-shadow": "0px 2px black"},
                                )
                            ],
                            width=12,
                            className="mt-5",
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
                            md={"size": 8, "offset": 2},
                            className="mb-8",
                        ),
                        dbc.Row(
                            [  # Main col: Row for cards
                                dbc.Col(
                                    [  # First card
                                        html.Img(
                                            src="/assets/images/feature_achievements_glare.png",
                                            width="100%",
                                        ),
                                        html.H4(
                                            "Personlige utfordringer og belønninger",
                                            className="mt-3 mb-2",
                                            style={"color": "white",
                                                   "text-shadow": "0px 1px black"},
                                        ),
                                    ],
                                    lg=3,
                                ),  # First card closing parantheses
                                dbc.Col(
                                    [  # Second card
                                        html.Img(
                                            src="/assets/images/feature_map.png", width="100%"
                                        ),
                                        html.H4(
                                            "Et skattekart for plast og Plukk-events",
                                            className="mt-3 mb-2",
                                            style={"color": "white",
                                                   "text-shadow": "0px 1px black"},
                                        ),
                                    ],
                                    lg=3,
                                ),  # Second card closing parantheses
                                dbc.Col(  # Third card
                                    [
                                        html.Img(
                                            src="/assets/images/feature_mypage.png",
                                            width="100%",
                                        ),
                                        html.H4(
                                            "Og mye mer...",
                                            className="mt-3 mb-2",
                                            style={"color": "white",
                                                   "text-shadow": "0px 1px black"},
                                        ),
                                    ],
                                    lg=3,
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
                "background-image": "url('assets/images/green_background.png')"
            },
            align="start",
            justify="center",
        ),  # Feature row closing parantheses
        dbc.Row([  # Signup row
            dbc.Col([  # First col for signup form
                html.H1("Bli først til å teste Plukk!",
                        className="mb-4",
                        style={"text-shadow": "0px 2px black"}),
                html.P("""Fyll ut skjemaet under for å få informasjon om\
                 utviklingen av Plukk eller være én av\
                 de første til å teste appen.""",
                       className="mb-4",
                       style={"color": "teal"}),
                main_form_body  # Gets the form body from resources.py
            ],  # Signup col properties
                lg=6,
                style={"color": "white"}
            )
        ],  # Signup row properties
            align="center",
            justify="center",
            style={"min-height": "600px",
                   "background-color": "#3b3b3b"}
        ),
        dbc.Row(
            [  # Story row
                dbc.Col([
                    html.H1("Historien bak Plukk",
                            className="mb-3",
                            style={"text-shadow": "0px 2px black"}),
                    html.P(
"""En kald februarnatt i 2019 satte et team fra konsulentselskapet Bouvet seg \
ned for være med å løse et enormt problem: Plast i havet.\n
I tillegg til et enormt problem hadde de 24 timer på å komme frem til en løsning. Med hjelp \
fra Plastkoordinator i Oslo, Anja Stokkan, ble Plukk løsningen til teamet. \
Appen hadde som hensikt å motivere folket til å plukke plast og søppel i \
naturen ved å skape et pantesystem som belønnet dem for strevet.\n
Dette er Plukk.
                           """)
                     ],  # Story first col
                    lg=5,
                    align="center",
                    style={"text-align": "left"},
                ),
                dbc.Col(  # Story second col
                    [html.Img(src="/assets/images/bouvet_hackathon.jpg",
                              width="100%",
                              style={"border-radius": "20px",
                                     "border": "solid",
                                     "border-color": "#ffcc00"})],
                    lg=4,
                    style={"text-align": "center"}
                )
                # Closing parantheses of Story row
            ],
            style={
                "min-height": "500px",
                "background-image": "url('/assets/images/green_background.png')",
                "color": "#fafafa"
            },
            align="center",
            justify="center",
            # Footer row properties
        ),
    ],  # Container children closure
    style={"font-family": "courier"}
)  # Container end bracket


# CALLBACKS
# Open modal 1
@app.callback(
    Output("modal_form", "is_open"),
    [Input("open_modal_form_button", "n_clicks"), Input("close_modal_form_button", "n_clicks")],
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
