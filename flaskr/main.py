from flaskr import app
from flask import render_template

@app.route('/')
def index():

    test = {'name': 'Rino', 'age':'admin'}

    return render_template(
        'index.html',
        test=test
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )