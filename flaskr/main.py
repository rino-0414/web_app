from flask import Blueprint, render_template
from flaskr import app

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'Hello, World!'

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )