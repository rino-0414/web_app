from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import psycopg2
from datetime import date
from dotenv import load_dotenv
import os

bp = Blueprint('main', __name__)

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
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
            due_date DATE NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT FALSE
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

# アプリケーションの起動時にテーブルを作成
create_tasks_table()

@bp.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks WHERE due_date >= %s AND completed = FALSE ORDER BY due_date', (date.today(),))
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

@bp.route('/get_tasks')
def get_tasks():
    date_str = request.args.get('date')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT title, description FROM tasks WHERE due_date = %s AND completed = FALSE', (date_str,))
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(tasks)

@bp.route('/get_all_tasks')
def get_all_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT due_date, title, description, id FROM tasks WHERE completed = FALSE')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(tasks)

@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO tasks (title, description, due_date) VALUES (%s, %s, %s)', (title, description, due_date))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('main.index'))
    return render_template('add.html')

@bp.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE tasks SET completed = TRUE WHERE id = %s', (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204

@bp.route('/incomplete_task/<int:task_id>', methods=['POST'])
def incomplete_task(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE tasks SET completed = FALSE WHERE id = %s', (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204

@bp.route('/task_list')
def task_list():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks WHERE completed = FALSE ORDER BY due_date')
    tasks = cur.fetchall()
    cur.execute('SELECT * FROM tasks WHERE completed = TRUE ORDER BY due_date')
    completed_tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('task_list.html', tasks=tasks, completed_tasks=completed_tasks, current_date=date.today())

@bp.route('/edit_task/<int:task_id>', methods=('GET', 'POST'))
def edit_task(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, title, description, due_date FROM tasks WHERE id = %s', (task_id,))
    task = cur.fetchone()
    cur.close()
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        
        cur = conn.cursor()
        cur.execute('UPDATE tasks SET title = %s, description = %s, due_date = %s WHERE id = %s',
                    (title, description, due_date, task_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('main.task_list'))
    
    return render_template('edit_task.html', task=task)

@bp.route('/delete_task/<int:task_id>', methods=('POST',))
def delete_task(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('main.task_list'))