import dash
from moesifwsgi import MoesifMiddleware
# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=["url('/assets/boostrap.css')"]
)

server = app.server

moesif_settings = {
    'APPLICATION_ID': 'eyJhcHAiOiI2MTc6MjIxIiwidmVyIjoiMi4wIiwib3JnIjoiMjA3OjIzNCIsImlhdCI6MTU3MTAxMTIwMH0.vL8LqwLnVjAhfpV9JIgn1ZkAPSatTsEVIk9v8mfzq3M',
    'CAPTURE_OUTGOING_REQUESTS': False, # Set to True to also capture outgoing calls to 3rd parties.
    'LOG_BODY': True,
}

server.wsgi_app = MoesifMiddleware(server.wsgi_app, moesif_settings)
