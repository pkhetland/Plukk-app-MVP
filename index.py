import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import psycopg2  # Manages connection to Postgres database
from flask_sqlalchemy import SQLAlchemy

from app import app
import layout  # Import the dash bootstrap layout
import callbacks

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

body = layout.body  # Get layout from layout.py

app.layout = html.Div([body])  # Define layout

if __name__ == "__main__":  # Run program
    app.run_server(debug=True)
