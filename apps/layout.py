import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from apps.resources import faq_table

# FORMS

main_form_body = dbc.Form([  # Signup form
    dbc.FormGroup([  # First name input
        html.P("Navn", style={"font-family": "courier"}),
        dbc.Input(type="text",
                  id="main_form_name",
                  placeholder="Skriv inn navnet ditt...",
                  style={"width": "80%",
                         "box-shadow": "0px 2px black"},
                  className="m_bottom_md")
    ]),
    dbc.FormGroup([
        html.P("E-postadresse*", style={"font-family": "courier"}),
        dbc.Input(type="email",
                  id="main_form_email",
                  placeholder="Skriv inn e-posten din...",
                  style={"width": "80%",
                         "box-shadow": "0px 2px black",
                         "size": "3rem"},
                  className="m_bottom_md")
    ]),
    html.P("", id="main_form_output", style={"color": "orange"},
           className="m_bottom_md"),
    dbc.Button("Send inn!",
               color="warning",
               className="mt-4 mb-2 p",
               style={"box-shadow": "0px 2px black"},
               id="submit_main_form",
               size="lg")
    ])


body = dbc.Container(  # Main container
    fluid=True,
    children=[
        dbc.Row(
            [  # Banner first row
                dbc.Col(  # Banner first column
                    lg=4,
                    md=8,
                    sm=8,
                    children=[
                        html.H1(
                            "PLUKK.",
                            className="mb-5 mt-5",
                            style={"color": "white",
                                   "text-shadow": "0px 3px black",
                                   "text-align": "center",
                                   "font-size": "4rem"},
                        ),
                        html.P(
                            """\
PLUKK gjør det lønnsomt å plukke søppel.\n Med en PLUKKpose med QR-kode og en mobil \
kan store og små dra ut på eventyr for å vinne kule premier og få belønninger.""",
                            style={"color": "#D6D6D6",
                                   "text-align": "center",
                                   "font-size": "1.4rem"},
                        )
                    ],
                    className="m_top_lg"
                ),  # Banner first col closure
                dbc.Col(  # Banner second column
                    [html.Img(src="/assets/images/three_phones_2.png",
                              width="100%")],
                    lg="5",
                    md="8",
                    sm="10",
                    className="m_top_lg m_bottom_lg"
                ),
            ],  # Banner row properties
            style={
                "background-image": "url('/assets/images/lofoten_beach_"
                                    "background_blur.png')",
                "background-repeat": "no-repeat",
                "background-size": "cover",
                "background-attachment": "fixed",
                "min-height": "750px"
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
                                html.H1("Slik fungerer PLUKK.",
                                        style={"text-align": "center",
                                               "color": "rgba(0,0,0,0.8)",
                                               "text-shadow": "0px 1px gray"})
                            ],
                            width=12,
                            className="m_top_lg m_bottom_md",
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
                                    md=8,
                                    sm=8,
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
                                    md=8,
                                    sm=8,
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
                                    md=8,
                                    sm=8,
                                ),  # Third card col closing parantheses
                            ],
                            justify="around",
                            align="center",
                            style={"text-align": "left"},
                            className="mb-5"
                        ),  # Card row closing parantheses
                    ],
                    className="mt-5 m_bottom_lg"  # Properties of about-col
                )  # About col closure
            ],  # Properties of about-row
            style={"min-height": "700px",
                   "background-image": "url('/assets/images/"
                                       "paper_background_3.jpg')",
                   "background-size": "cover"
                   },
            align="center",
            justify="center"
        ),  # About row closure
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
                                           "text-shadow": "0px 2px black",},
                                    className="mt-5 mb-4"
                                )
                            ],
                            width=12,
                            className="m_top_lg m_bottom_md",
                        ),
                        dbc.Col(
                            [  # Main col: Paragraph
                                html.P(
                                    """\
PLUKK kommer med mange kule funksjoner som eget poengsystem, felles events, \
personlige utfordringer, lederlister og et skattekart som viser hvor \
plastavfallet befinner seg i dag.
\nHer er noen eksempler:""",
                                    style={"text-align": "center",
                                           "color": "silver",
                                           "font-family": "Courier New",
                                           "font-size": "1.4rem"},
                                    className="mt-5 mb-5",
                                )
                            ],
                            lg={"size": 6, "offset": 3},
                            md={"size": 8, "offset": 2},
                            sm={"size": 8, "offset": 2},
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
                                    md=10
                                ),  # First card closing parantheses
                                dbc.Col(
                                    [  # Second card
                                        html.Img(
                                            src="/assets/images/feature_map_2.png",
                                            width="100%"
                                        )
                                    ],
                                    lg=4,
                                    md=10
                                ),  # Second card closing parantheses
                                dbc.Col(  # Third card
                                    [
                                        html.Img(
                                            src="/assets/images/feature_mypage_2.png",
                                            width="100%"
                                        )
                                    ],
                                    lg=4,
                                    md=10,
                                    className="m_bottom_lg"
                                ),  # Third card col closing parantheses
                            ],
                            justify="around",
                            align="start",
                            style={"text-align": "center"},
                        ),  # Card row closing parantheses
                    ], className="mt-5 mb-5"
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
                html.H1("Bli først til å teste PLUKK!",
                        className="m_bottom_md",
                        style={"text-shadow": "0px 2px black"}),
                html.P("""Bli betatester og vær førstemann til å få \
                oppdateringer om appen.\n
                 (Slapp av, vi sender bare kult innhold.)""",
                       className="mt-5 mb-5",
                       style={"color": "#25b8b0"}),
                main_form_body  # Gets the form body from resources.py
            ],  # Signup col properties
                lg=8,
                md=10,
                style={"color": "white",
                       "font-size": "1.2rem"},
                className="mt-4"
            )
        ],  # Signup row properties
            align="center",
            justify="center",
            style={"min-height": "800px",
                   "background-color": "#3b3b3b",
                   "font-family": "Courier New"}
        ),
        dbc.Row(
            [  # Story and FAQ row
                dbc.Col([  # FAQ and feedback master col
                    dbc.Col([  # FAQ col
                        html.H1("Ofte stilte spørsmål:",
                            style={
                                "color": "#ea6621",
                                "text-shadow": "0px 2px black"})
                    ],
                        width=12,
                        className="mt-5"
                    ),
                    dbc.Col([
                        faq_table
                    ],
                        width=12),
                    dbc.Col([  # Feedback col
                        html.H2("Har du andre spørsmål eller innspill til PLUKK?",
                                style={"color": "#ffcc00",
                                       "text-shadow": "0px 2px black"},
                                className="mt-5 mr-3 ml-3"),
                        html.P("""Ta kontakt med oss på Innspill@plukkappen.no!\n
                        Vi gleder oss til å høre fra deg.
                        """,
                               style={"color": "#F6F6F6",
                                      "font-family": "courier new",
                                      "text-shadow": "0px 1px black"},
                               className="m_bottom_md m_top_md"),
                        html.A([
                            dbc.Button("Send oss en e-post",
                                       color="dark",
                                       size="md",
                                       style={"text-align": "center"},
                                       className="mb-5",
                                       id="email_button")
                            ],
                            href='mailto:innspill@plukkappen.no',
                            className='mt-3 mb-3'),
                    ],
                        width=12,
                        className="m_top_lg m_bottom_lg",
                        style={"text-align": "center"}
                    )  # Feedback col properties
                ],  # FAQ and feedback master col properties
                    style={"border": "dashed",
                           "border-size": "10px",
                           "border-color": "#3b3b3b",
                           "text-align": "center"},
                    lg=9,
                    md=11
                ),  # FAQ and feedback master col closure
                dbc.Col([
                    html.H1("Historien bak PLUKK",
                            className="mb-5 mt-5",
                            style={"text-shadow": "0px 2px black"}),
                    html.P(
"""En kald februarnatt i 2019 satte et team fra konsulentselskapet Bouvet seg \
ned for være med å løse et enormt problem: Plast i havet.\n
I tillegg til et enormt problem hadde de 24 timer på å komme frem til en løsning.\n Med hjelp \
fra Plastkoordinator i Oslo, Anja Stokkan, ble PLUKK løsningen til teamet. \
Appen hadde som hensikt å motivere folket til å plukke plast og søppel i \
naturen ved å skape et pantesystem som belønnet dem for strevet.\n
Dette er PLUKK.
                           """)
                     ],  # Story first col
                    lg=5,
                    md=10,
                    align="center",
                    style={"text-align": "left",
                           "color": "#D6D6D6",
                           "text-shadow": "0px 1px black"},
                    className="mb-5 mt-5"
                ),
                dbc.Col(  # Story second col
                    [html.Img(src="/assets/images/bouvet_hackathon.jpg",
                              width="100%",
                              style={"border-radius": "20px",
                                     "border": "solid",
                                     "border-color": "#ffcc00"})],
                    lg=5,
                    md=10,
                    style={"text-align": "center"},
                    className="mt-3 mb-5"
                )
                # Closing parantheses of Story row
            ],
            style={
                "min-height": "1000px",
                "background-image": "url('/assets/images/green_background.png')",
                "background-repeat": "no-repeat",
                "background-size": "cover",
                "background-attachment": "fixed",
                "color": "#fafafa",
                "font-family": "courier new"
            },
            align="center",
            justify="around",
            # Footer row properties
        ),  # Footer row closure
        dbc.Row([
            dbc.Col([
                html.H2("Kontakt oss:",
                        style={"font-size": "1.2rem",
                               "color": "#ea6621",
                               "font-weight": "bold"}),
                html.A(html.P("- Send oss en e-post",
                              style={"font-size": "1rem",
                                     "color": "silver",
                                     "font-weight": "bold"},
                              className="mt-2"),
                       href="mailto:Innspill@plukkappen.no",
                       target="_blank"),
                html.A(html.P("- Send oss en melding på Facebook",
                              style={"font-size": "1rem",
                                     "color": "silver",
                                     "font-weight": "bold"},
                              className="mt-2"),
                       href="https://www.facebook.com/plukkappen/",
                       target="_blank"),
                html.H2("Personvernerklæring:",
                        style={"font-size": "1.2rem",
                               "color": "#ea6621",
                               "font-weight": "bold"},
                        className="mt-5"),
                html.P("Denne tjenesten er eid av Bouvet AS og "
                       "blir dekket av deres personvernerklæring.",
                       style={"font-size": "1rem",
                              "color": "silver"}),
                html.A(html.P("- Les personvernerklæringen her",
                       style={"font-size": "1rem",
                              "color": "silver",
                              "font-weight": "bold"}),
                       href="https://www.bouvet.no/om-bouvet/"
                            "informasjonskapsler-og-personvern",
                       target="_blank"),
                html.Div([
                    dbc.Button("* Hva gjør vi med dataen du sender inn? "
                               "Les mer her.",
                               id="open_modal",
                               outline=True,
                               color="warning",
                               className="mt-5",
                               style={"font-family": "Courier",
                                      "font-size": "0.8rem"}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Databehandling"),
                            dbc.ModalBody(
                                html.Div([html.P(["""\
De eneste dataene vi samler inn \
fra deg er navnet du skriver inn og e-posten din. \
Disse bruker vi til å måle interessen for produktet, \
og vises ikke til noen utenfor teamet vårt.\n
Alle data slettes 2 måneder etter innsamling.\n
PLUKK er et samarbeid mellom studenter ved NMBU og Bouvet. \
Dersom du har spørsmål eller ønsker at dine data \
skal slettes, kan du kontakte oss via vår ansvarlige \
kontaktperson ved NMBU:\n
Petter Kolstad Hetland \n
Mobil: 978 87 892 \n
E-post: Pehe@nmbu.no\n
Takk!
                            """],
                                                 style={"font-size": "1rem"})
                                          ])
                                         ),
                            dbc.ModalFooter(
                                dbc.Button("Lukk vinduet",
                                           id="close_modal",
                                           className="ml-auto",
                                           style={"font-family": "Courier"})
                            ),
                        ],
                        id="data_info_modal",
                        style={"min-width": "70%",
                               "white-space": "pre-line"}
                    )
                ])
            ],
                lg=5,
                md=10,
                sm=10,
                style={"color": "white",
                       "font-size": "0.5rem",
                       "text-shadow": "0px 1px black"},
                className="mt-5 mb-5 ml-5 mr-5",
            )
        ],
            align="center",
            justify="start",
            style={"min-height": "200px",
                   "background-color": "#3b3b3b"}
        ),  # Footer contact info closure
        dbc.Row([  # Footer logo
            dbc.Col([
                html.A([html.Img(src="/assets/images/bouvet_logo.png",
                         width="100%")],
                       href="https://www.bouvet.no",
                       target="_blank")
            ],
                lg=2,
                md=4,
                sm=4,
                align="end",
                className="mb-5 mr-5 ml-5"
            )
        ],
            align="center",
            justify="end",
            style={"background-color": "#3b3b3b"}
        )  # Footer logo closure
    ],
    style={"font-family": "Courier New"}  # Container children closure
)  # Container end bracket
