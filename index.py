import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
import layout  # Import the dash bootstrap layout
import callbacks

body = layout.body  # Get layout from layout.py

app.layout = html.Div([body])  # Define layout

if __name__ == "__main__":  # Run program
    app.run_server(debug=True)
