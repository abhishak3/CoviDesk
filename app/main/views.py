from flask import render_template, session
from . import main

@main.route('/')
@main.route('/home')
def index():
    return render_template('index.html', name=session.get('name')), 200
