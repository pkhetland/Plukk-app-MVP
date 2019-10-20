import dash_html_components as html

from app import app
from apps import layout
from apps import resources

body = layout.body  # Get layout from layout.py

app.layout = html.Div([body])  # Define layout


if __name__ == "__main__":  # Run program
    app.run_server(debug=True)
