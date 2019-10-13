from dash.dependencies import Input, Output, State
from app import app

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
            return "Hurra! Du har spennende tider i vente."


