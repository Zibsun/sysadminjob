from app import app
from app import db
from app.models import Hh_vacancy
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    v = Hh_vacancy.query.get(1)
    return render_template('index.html', title='Home', user=v.name)
