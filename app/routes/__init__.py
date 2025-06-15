from flask import Blueprint, render_template, redirect, url_for, request, session
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

main = Blueprint('main', __name__)

db = None  # Will be initialized from create_app()


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_pass_hash = generate_password_hash(request.form['password'])

        if main.db.users.find_one({"email": email}):
            return "Email already exists"

        main.db.users.insert_one({"username": username, "email": email, "password": password})
        return redirect(url_for('main.login'))
    return render_template('signup.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = main.db.users.find_one({"email": email})

        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user["_id"])
            return redirect(url_for('main.index'))
        else:
            return "Invalid credentials"

    return render_template('login.html')

@main.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.login'))


@main.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    tasks = main.db.tasks.find({"user_id": session['user_id']}).sort("created_at", -1)

    tasks = [{
        **task,
        "_id": str(task["_id"]),
        "created_at": task["created_at"].strftime("%Y-%m-%d %H:%M"),
        "done_at": task["done_at"].strftime("%Y-%m-%d %H:%M") if "done_at" in task and task["done_at"] else None
    } for task in tasks]

    return render_template('index.html', tasks=tasks)



@main.route('/add', methods=['POST'])
def add():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    task = request.form['task']

    main.db.tasks.insert_one({"task": task, "done": False, "user_id": session['user_id'], "created_at": datetime.utcnow() })
    return redirect(url_for('main.index'))    

from datetime import datetime

@main.route('/done/<task_id>', methods=['POST'])
def done(task_id):
    main.db.tasks.update_one({"_id": ObjectId(task_id), "user_id": session['user_id']},
                             {"$set": {"done": True, "done_at": datetime.utcnow()}})

    return redirect(url_for('main.index'))


@main.route('/undo/<task_id>', methods=['POST'])
def undo(task_id):
    main.db.tasks.update_one({"_id": ObjectId(task_id), "user_id": session['user_id']},
                             {"$set": {"done": False}})
    return redirect(url_for('main.index'))    

@main.route('/delete/<task_id>', methods=['POST'])
def delete(task_id):
    main.db.tasks.delete_one({"_id": ObjectId(task_id), "user_id": session['user_id']})
    return redirect(url_for('main.index'))    

@main.route('/edit/<task_id>', methods=['POST'])
def edit(task_id):
    new_task = request.form['new_task']

    main.db.tasks.update_one({"_id": ObjectId(task_id), "user_id": session['user_id']},
                             {"$set": {"task": new_task}})
    return redirect(url_for('main.index'))  
