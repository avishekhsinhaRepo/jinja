from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
todos = [
    ('Learn Python', 'completed'),
    ('Build a Python App', 'pending'),
    ('Learn Flask', 'completed'),
    ('Build a Flask App', 'pending')
]


@app.template_filter('format_currency')
def format_currency(value, currency):
    return f"{currency}{value:.2f}"


@app.context_processor
def message():
    return {'message': 'Message for Context Processor'}


@app.get('/')
def todo():
    return render_template('home.html', todos=todos)


@app.get('/main')
def welcome():
    return render_template('main.html', title="My Custom Title")


htmlCode = """ 
<div>
    <h1>Welcome to Flask</h1>
    <p>Flask is a micro web framework written in Python.</p>
</div>
"""


@app.get('/jinja')
def jinja():
    return render_template('test.jinja2', htmlCode=htmlCode)


@app.get('/mainhtml')
def main_html():
    return render_template('test.html', htmlCode=htmlCode)


@app.get('/todos/<string:todo_item>')
def todo_item(todo_item: str):
    for todo_txt, status in todos:
        if todo_item == todo_txt:
            return render_template('todo.html', todo_txt=todo_txt, status=status)
        else:
            return render_template('not-found.html')


# data of student for the table
students = [
    {'id': 1, 'name': 'John Doe', 'age': 25, 'address': 'USA', 'marks': 80},
    {'id': 2, 'name': 'Jane Doe', 'age': 22, 'address': 'UK',   'marks': 75},
    {'id': 3, 'name': 'Tom Smith', 'age': 28 , 'address': 'Canada', 'marks': 90},
    {'id': 4, 'name': 'Jerry Lim', 'age': 30 ,  'address': 'Australia', 'marks': 85},
]
@app.get('/student')
def student():
    return render_template('student.html', students=students)


@app.get('/profile')
def profile():
    return render_template('profile.html', students=students)


