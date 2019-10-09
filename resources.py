"""Python file meant to contain any callbacks for app.py
"""
import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import *


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


# CALLBACKS
# Open modal 1
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
