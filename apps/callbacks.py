from dash.dependencies import Input, Output, State
from app import app
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

cs = 'postgres://qxtmarboumalkd:a70cd9ccf0b9b65bbb7d0da3bffe65c94f99c8b7c6d2a9cbfb2a24a15287074b@ec2-107-20-173-227.compute-1.amazonaws.com:5432/d7q3kba2rlkchv'

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


# Callback for modal
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open





