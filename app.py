from flask import Flask, render_template_string, request, jsonify
import sqlite3

app = Flask(__name__)

# Create table if not exists
def init_db():
    conn = sqlite3.connect('tasks.db')
    conn.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT)')
    conn.close()

@app.route('/')
def home():
    # Render HTML directly (no templates folder)
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/tasks', methods=['GET', 'POST', 'DELETE'])
def tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    if request.method == 'POST':
        title = request.json['title']
        c.execute('INSERT INTO tasks (title) VALUES (?)', (title,))
        conn.commit()
        return jsonify({'message': 'Task added!'})

    elif request.method == 'GET':
        c.execute('SELECT * FROM tasks')
        tasks = [{'id': row[0], 'title': row[1]} for row in c.fetchall()]
        return jsonify(tasks)

    elif request.method == 'DELETE':
        task_id = request.json['id']
        c.execute('DELETE FROM tasks WHERE id=?', (task_id,))
        conn.commit()
        return jsonify({'message': 'Task deleted!'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
