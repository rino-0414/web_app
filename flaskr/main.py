from flask import Blueprint, render_template, request, redirect, url_for
import psycopg2
from datetime import date, timedelta

bp = Blueprint('main', __name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_user",
        password="your_password"
    )
    return conn

def create_tasks_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            due_date DATE NOT NULL
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

@bp.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks WHERE due_date >= %s ORDER BY due_date', (date.today(),))
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

@bp.route('/form')
def form():
    return render_template('form.html')

@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO tasks (title, description, due_date) VALUES (%s, %s, %s)',
                    (title, description, due_date))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('main.index'))
    
    return render_template('add.html')

@bp.route('/upcoming')
def upcoming():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks WHERE due_date BETWEEN %s AND %s ORDER BY due_date',
                (date.today(), date.today() + timedelta(days=7)))
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('upcoming.html', tasks=tasks)

@bp.route('/overdue')
def overdue():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks WHERE due_date < %s ORDER BY due_date', (date.today(),))
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('overdue.html', tasks=tasks)