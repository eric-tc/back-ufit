from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY']='2c100f925d208d14d63a3938e7071d59'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.jinja_env.add_extension('jinja2.ext.do')
CORS(app, resources={r'/*': {'origins': '*'}})
db=SQLAlchemy(app)

# variabile che previene la creazione a db della scheda ongi volta che ricarico la pagina
generazione_scheda=0
# questo valore deve essere messo dopo la creazione di app per evitare circular import
# lo aggiungo per caricare le path
from ufit import routes

