import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
import layout  # Import the dash bootstrap layout
import callbacks
from models import Contact

body = layout.body  # Get layout from layout.py

app.layout = html.Div([body])  # Define layout

def add_contact():
    name = request.args.get('name')
    email = request.args.get('email')
    try:
        contact = Contact(
            name=name,
            email=email
        )
        db.session.add(contact)
        db.session.commit()
        return "Contact added. Contact name={}".format(contact.name)
    except Exception as e:
        return(str(e))


if __name__ == "__main__":  # Run program
    app.run_server(debug=True)
