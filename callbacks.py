from dash.dependencies import Input, Output, State
from app import app


# Submit forms
@app.callback(
    Output("main_form_output", "children"),
    [Input("submit_main_form", "n_clicks")])
def form_response(n_clicks):
    if n_clicks:
        return "Takk for interessen! Du har spennende tider i vente."
