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



cs = 'postgres://qxtmarboumalkd:a70cd9ccf0b9b65bbb7d0da3bffe65c94f99c8b7c' \
     '6d2a9cbfb2a24a15287074b@ec2-107-20-173-227.compute-1.amazonaws.co' \
     'm:5432/d7q3kba2rlkchv'

engine = create_engine(cs)


# Submit forms
@app.callback(
    Output("main_form_output", "children"),
    [Input("submit_main_form", "n_clicks")],
    [State("main_form_name", "value"),
     State("main_form_email", "value")])
def form_response(n_clicks, main_form_name, main_form_email):
    if n_clicks:
        if main_form_name is None or main_form_email is None:
            return "Du må fylle inn både e-postadresse og navnet ditt."
        else:
            userdict = {'name': [main_form_name], 'email': [main_form_email]}
            df = pd.DataFrame(userdict)
            df.to_sql('plukk_contacts',
                      engine,
                      if_exists='append')
            return "Hurra! Du har spennende tider i vente."
            # return str(pd.read_sql_table('contacts', engine))


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


# Content for FAQ module

q1 = html.Tr([
    html.Td([
        html.H3("Hvor kan jeg levere de fulle posene?",
                style={"color": "#F6F6F6",
                       "text-shadow": "0px 1px black",
                       "text-align": "left"},
                className="mt-2"),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(
                "Det velger du helt selv.\n"
                "Maksimal poengsum får du dersom du leverer posene "
                "dine på et mottak som sorterer restavfall, plast og resirkulerbar "
                "havplast. \nSlik skaper vi mest verdi med innsatsen vår."
                "\nDu kan selvfølgelig også kaste posene i "
                "nærmeste restavfall mot en lavere poengsum. "
                "\nAlle tiltak bidrar mot en renere kystlinje for mennesker og dyreliv!"
            ),
                style={
                    "background-image": "url('/assets/images/paper_background_3.jpg')",
                    "background-size": "cover",
                    "color": "rgba(0, 0, 0, 0.80)",
                    "font-family": "courier"}
            ),
            id="q1_collapse",
            className="mt-4",
            style={"white-space": "pre-line",
                   "text-align": "start"}
        )
    ]),
    html.Td([
        html.Div([
            dbc.Button(
                "Se svaret",
                id="q1_collapse_button",
                size="md",
                color="dark")
        ])
    ])
])

q2 = html.Tr([
    html.Td([
        html.H3("Hvor finner jeg PLUKKposer?",
                style={"color": "#F6F6F6",
                       "text-shadow": "0px 1px black",
                       "text-align": "left"},
                className="mt-2"),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(
                "Posene kommer til å være tilgjengelige "
                "flere steder. \nDe kan:"
                "\n - Hentes på nærbutikken din"
                "\n - Hentes i dispensere ved en rekke strender og naturområder"
                "\n - Bestilles på nett helt gratis."
            ),
                style={
                    "background-image": "url('/assets/images/paper_background_3.jpg')",
                    "background-size": "cover",
                    "color": "rgba(0, 0, 0, 0.80)",
                    "font-family": "courier"
                }
            ),
            id="q2_collapse",
            className="mt-4",
            style={"white-space": "pre-line",
                   "text-align": "start",
                   "color": "#E63b3b3b"}
        )
    ]),
    html.Td([
        html.Div([
            dbc.Button(
                "Se svaret",
                id="q2_collapse_button",
                size="md",
                color="dark"
            )
        ])
    ])
])

faq_table_body = [html.Tbody([q1, q2])]

faq_table = dbc.Table(faq_table_body,
                      bordered=False, hover=True,
                      striped=True, responsive=True,
                      size="lg",
                      borderless=True)


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



