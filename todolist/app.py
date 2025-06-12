from flask import Flask, render_template, request, redirect, url_for
from to_do_list import ToDoList

app = Flask(__name__)
todo_list = ToDoList()

@app.route('/')
def index():
    return render_template('index.html', tasks=todo_list.tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todo_list.add_task(task)
    return redirect(url_for('index'))

@app.route('/remove/<task>')
def remove(task):
    todo_list.remove_task(task)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)