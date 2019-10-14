import dash
# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy


app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=["url('/assets/boostrap.css')"]
)

server = app.server
