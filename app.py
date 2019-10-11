import dash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='qxtmarboumalkd',
                                                               pw='a70cd9ccf0b9b65bbb7d0da3bffe65c94f99c8b7c6d2a9cbfb2a24a15287074b',
                                                               url='ec2-107-20-173-227.compute-1.amazonaws.com,db=d7q3kba2rlkchv)',
                                                               db='d7q3kba2rlkchv')


server = Flask(__name__)
app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=["url('/assets/boostrap.css')"])
server.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)

