from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'Hello, World!'

@bp.route('/form')
def form():
    return render_template('form.html')