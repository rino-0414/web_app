from flaskr import app
from flask import render_template

@app.route('/')
def index():

    test = {
        'name': 'John',
        'age': 25
    }

    return render_template(
        'index.html',
        test=test
    )