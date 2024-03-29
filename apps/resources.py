# Imports
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

from app import app

# Defining Postgres database URL
cs = (
    "postgres://qxtmarboumalkd:a70cd9ccf0b9b65bbb7d0da3bffe65c94f99c8b7c"
    "6d2a9cbfb2a24a15287074b@ec2-107-20-173-227.compute-1.amazonaws.co"
    "m:5432/d7q3kba2rlkchv"
)

# Define SQLalchemy engine
engine = create_engine(cs)


# Callback for data info modal
@app.callback(
    Output("data_info_modal", "is_open"),
    [Input("open_modal", "n_clicks"), Input("close_modal", "n_clicks")],
    [State("data_info_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# FAQ CONTENT
# Content for FAQ module
# FAQ question one
q1 = html.Tr(
    [
        html.Td(
            [
                html.H3(
                    "Hvor kan jeg levere de fulle posene?",
                    style={"color": "#F6F6F6", "text-shadow": "0px 1px black"},
                    className="",
                ),
                dbc.Collapse(
                    dbc.Card(
                        dbc.CardBody("""
Det velger du helt selv.\n
Maksimal poengsum får du dersom du leverer posene 
dine på et mottak som sorterer restavfall, plast og resirkulerbar 
havplast. \nSlik skaper vi mest verdi med innsatsen vår.
\nDu kan selvfølgelig også kaste posene i 
nærmeste restavfall mot en lavere poengsum. 
\nAlle tiltak bidrar mot en renere kystlinje for mennesker og dyreliv!
                        """),
                        style={
                            "background-image": "url('/assets/images/"
                                                "paper_background_3.jpg')",
                            "background-size": "cover",
                            "color": "rgba(0, 0, 0, 0.80)",
                            "font-family": "courier",
                        },
                    ),
                    id="q1_collapse",
                    className="mt-3 mb-2",
                    style={"white-space": "pre-line"},
                ),
                dbc.Button(
                    "Åpne/Lukke",
                    id="q1_collapse_button",
                    size="sm",
                    color="dark",
                    className="mt-1",
                ),
            ]
        )
    ]
)

# FAQ question two
q2 = html.Tr(
    [
        html.Td(
            [
                html.H3(
                    "Hvor finner jeg PLUKKposer?",
                    style={"color": "#F6F6F6", "text-shadow": "0px 1px black"},
                    className="",
                ),
                dbc.Collapse(
                    dbc.Card(
                        dbc.CardBody(
                            "Posene kommer til å være tilgjengelige "
                            "flere steder. \n\nDe kan:"
                            "\n - Hentes på nærbutikken din"
                            "\n - Hentes i dispensere ved en rekke strender "
                            "og naturområder"
                            "\n - Bestilles på nett helt gratis."
                        ),
                        style={
                            "background-image": "url('/assets/images/"
                            "paper_background_3.jpg')",
                            "background-size": "cover",
                            "color": "rgba(0, 0, 0, 0.80)",
                            "font-family": "courier",
                        },
                    ),
                    id="q2_collapse",
                    className="mt-3 mb-2",
                    style={"white-space": "pre-line", "color": "#E63b3b3b"},
                ),
                dbc.Button(
                    "Åpne/Lukke",
                    id="q2_collapse_button",
                    size="sm",
                    color="dark",
                    className="mt-1",
                ),
            ]
        )
    ]
)

# Define FAQ table body
faq_table_body = [html.Tbody([q1, q2])]

# Define FAQ table with properties
faq_table = dbc.Table(
    faq_table_body,
    bordered=False,
    hover=True,
    striped=True,
    responsive=True,
    size="lg",
    borderless=True,
    style={"width": "100%"},
)


# Callback for faq table q1
@app.callback(
    Output("q1_collapse", "is_open"),
    [Input("q1_collapse_button", "n_clicks")],
    [State("q1_collapse", "is_open")],
)
def toggle_q1_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# Callback for faq table q2
@app.callback(
    Output("q2_collapse", "is_open"),
    [Input("q2_collapse_button", "n_clicks")],
    [State("q2_collapse", "is_open")],
)
def toggle_q2_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# Main form content
main_form_body = dbc.Form(
    [  # Signup form
        dbc.FormGroup(
            [  # First name input
                html.P("Navn:", style={"font-family": "courier"}),
                dbc.Input(
                    type="text",
                    id="main_form_name",
                    placeholder="Skriv inn navnet ditt...",
                    style={
                        "width": "80%",
                        "box-shadow": "0px 2px black",
                        "font-family": "courier",
                    },
                    className="m_bottom_md",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                html.P("E-postadresse:", style={"font-family": "courier"}),
                dbc.Input(
                    type="email",
                    id="main_form_email",
                    placeholder="Skriv inn e-posten din...",
                    style={
                        "width": "80%",
                        "box-shadow": "0px 2px black",
                        "font-family": "courier",
                    },
                    className="",
                ),
            ]
        ),
        html.P(
            "", id="main_form_output", style={"color": "orange"}, className=""
        ),
        dbc.Button(
            "Send inn!",
            color="warning",
            className="mt-4 mb-2",
            style={"box-shadow": "0px 2px black"},
            id="submit_main_form",
            size="lg",
        ),
    ]
)


# Feedback form content
feedback_form_body = dbc.Form(
    [  # Signup form
        dbc.FormGroup(
            [  # First name input
                html.P(
                    "Navn:",
                    style={"font-family": "courier", "text-align": "left"},
                ),
                dbc.Input(
                    type="text",
                    id="feedback_form_name",
                    placeholder="Skriv inn navnet ditt...",
                    style={
                        "width": "100%",
                        "box-shadow": "0px 2px black",
                        "font-family": "courier",
                    },
                    className="mb-2",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                html.P(
                    "E-postadresse:",
                    style={"font-family": "courier", "text-align": "left"},
                    className="mt-4",
                ),
                dbc.Input(
                    type="email",
                    id="feedback_form_email",
                    placeholder="Skriv inn e-posten din...",
                    style={
                        "width": "100%",
                        "box-shadow": "0px 2px black",
                        "font-family": "courier",
                    },
                    className="mb-2",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                html.P(
                    "Innspill/tilbakemelding:",
                    style={"font-family": "courier", "text-align": "left"},
                    className="mt-4",
                ),
                dbc.Textarea(
                    id="feedback_form_content",
                    placeholder="Skriv inn din beskjed...",
                    style={
                        "width": "100%",
                        "box-shadow": "0px 2px black",
                        "font-family": "courier",
                    },
                    maxLength=800,
                    className="",
                ),
            ]
        ),
        html.P(
            "",
            id="feedback_form_output",
            style={"color": "orange", "font-family": "courier"},
            className="",
        ),
        dbc.Button(
            "Send inn",
            color="dark",
            className="mt-2 mb-5",
            style={"box-shadow": "0px 2px black", "justify-item": "left"},
            id="submit_feedback_form",
            size="lg",
        ),
    ]
)


# FORM CALLBACKS
# Submit feedback form
@app.callback(
    Output("feedback_form_output", "children"),
    [Input("submit_feedback_form", "n_clicks")],
    [
        State("feedback_form_name", "value"),
        State("feedback_form_email", "value"),
        State("feedback_form_content", "value"),
    ],
)
def form_response(
    n_clicks, feedback_form_name, feedback_form_email, feedback_form_content
):
    if n_clicks:
        if feedback_form_email is None or feedback_form_content is None:
            return "Du må fylle inn både e-postadressen og skrive en beskjed."
        else:
            feedback_dict = {
                "name": [feedback_form_name],
                "email": [feedback_form_email],
                "message": [feedback_form_content],
            }
            df = pd.DataFrame(feedback_dict)
            df.to_sql("plukk_feedback", engine, if_exists="append")
            return "Takk for tilbakemeldingen din!"


# Submit tester form
@app.callback(
    Output("main_form_output", "children"),
    [Input("submit_main_form", "n_clicks")],
    [State("main_form_name", "value"), State("main_form_email", "value")],
)
def form_response(n_clicks, main_form_name, main_form_email):
    if n_clicks:
        if main_form_name is None or main_form_email is None:
            return "Du må fylle inn både e-postadresse og navnet ditt."
        else:
            userdict = {"name": [main_form_name], "email": [main_form_email]}
            df = pd.DataFrame(userdict)
            df.to_sql("plukk_contacts", engine, if_exists="append")
            return "Hurra! Du har spennende tider i vente."
            # return str(pd.read_sql_table('contacts', engine))
