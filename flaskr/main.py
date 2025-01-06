from flaskr import app
from flask import render_template

@app.route('/')
def index():

    test = {
        'name': 'Rino',
        'age': 20
    }

    return render_template(
        'index.html',
        test=test
    )