import dash
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


DB_URL_HEROKU = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='qxtmarboumalkd',
                                                               pw='a70cd9ccf0b9b65bbb7d0da3bffe65c94f99c8b7c6d2a9cbfb2a24a15287074b',
                                                               url='ec2-107-20-173-227.compute-1.amazonaws.com,db=d7q3kba2rlkchv)',
                                                               db='d7q3kba2rlkchv')

DB_URL_LOCAL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='postgres',
                                                               pw='postgres',
                                                               url='localhost',
                                                               db='contacts')


server = Flask(__name__)
app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=["url('/assets/boostrap.css')"])


#app.config.from_object(os.environ['APP_SETTINGS'])
server.config['SQLALCHEMY_DATABASE_URI'] = DB_URL_HEROKU
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)
