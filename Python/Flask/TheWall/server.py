from flask import Flask, render_template, request, redirect, flash, session
import re
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'This is secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'thewall')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    strQuery = "SELECT * FROM users"
    users = mysql.query_db(strQuery)
    return render_template("index.html", wall=users)

@app.route('/register', methods=['POST'])
def register():
    session['first_name'] = request.form['first_name']
    first_name = session['first_name']
    session['last_name'] = request.form['last_name']
    last_name = session['last_name']
    session['email'] = request.form['email']
    email = session['email']
    password = request.form['password']
    pwconfirm = request.form['pwconfirm']

    hash = bcrypt.generate_password_hash(password)

    email_query = "SELECT * FROM users WHERE email = :email"
    data = {'email': email}
    x = mysql.query_db(email_query, data)
    invalid = False
    if int(len(x)) == 0:

        if len(request.form['first_name']) < 1:
            flash("You must enter your first name!")
            invalid = True

        if request.form['first_name'].isalpha() == False:
            flash("First name must not contain any numbers.")
            invalid = True

        if len(request.form['last_name']) < 1:
            flash("You must enter your last name!")
            invalid = True

        if request.form['last_name'].isalpha() == False:
            flash("Last name must not contain any numbers.")
            invalid = True

        if len(request.form['email']) < 1:
            flash("You must enter an email address!")
            invalid = True

        if not EMAIL_REGEX.match(request.form['email']):
            flash('Invalid Email Address!')
            invalid = True

        if len(request.form['password']) < 1:
            flash("You must enter a password!")
            invalid = True

        if len(request.form['password']) < 8:
            flash("Password should be at least 8 characters")
            invalid = True

        if request.form['password'] != request.form['pwconfirm']:
            flash("Password and password confirm should match!")
            invalid = True

        if invalid:
            return redirect('/')

        else:
            flash("Thanks for submitting your information. You are now logged in.")
            query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())"
            data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": hash,
            }

            session['user_id'] = mysql.query_db(query, data)
            return redirect("/wall")

    elif int(len(x)) > 0:
        flash('That email already exists.  Please login.')
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    invalid = False
    if len(request.form['email']) < 1:
        flash("You must enter an email address!")
        invalid = True

    if len(request.form['password']) < 1:
        flash("You must enter a password!")
        invalid = True

    if invalid:
        return redirect('/')

    else:
        email = request.form['email']
        password = request.form['password']
        email_query = "SELECT * FROM users WHERE email = :email"
        data = {'email': email}
        x = mysql.query_db(email_query, data)
        if int(len(x)) == 0:
            flash('The email you submitted does not match our records.')
            return redirect('/')

        elif int(len(x)) > 0:
            user = mysql.query_db(email_query, data)
            if not bcrypt.check_password_hash(x[0]['password'], password):
                flash('Incorrect Password!')
                return redirect('/')

            else:
                flash("You have successfully logged in!")
                session['user_id'] = x[0]['id']
                return redirect("/wall")

@app.route('/wall')
def seeWall():
    message = mysql.query_db('SELECT messages.message, messages.id AS message_id, messages.created_at, messages.updated_at, users.first_name, users.last_name, users.id AS user_id FROM messages JOIN users ON messages.user_id = users.id')
    comment = mysql.query_db('SELECT comments.comment, comments.message_id, comments.user_id, comments.id AS comment_id, users.first_name, users.last_name, users.id AS user_id FROM comments LEFT JOIN users ON comments.user_id = users.id')
    query = 'SELECT users.first_name FROM users WHERE users.id = :user_id'
    data = {'user_id': session['user_id']}
    first_name_query = mysql.query_db(query, data)
    first_name = first_name_query[0]['first_name']
    print message
    print comment
    return render_template("wall.html", first_name = first_name, messages = message, comments = comment)

@app.route('/posts', methods = ["POST"])
def addPost():
    query = "INSERT INTO messages(message, created_at, updated_at, user_id) VALUES(:message, NOW(), NOW(), :user_id)"
    data = {
        'message': request.form['message'],
        'user_id': session['user_id']
    }
    mysql.query_db(query,data)
    return redirect("/wall")

@app.route('/comments/<message_id>', methods = ["POST"])
def addComment(message_id):
    query = "INSERT INTO comments (comment, message_id, user_id, created_at, updated_at) VALUES (:comment, :message_id, :user_id, NOW(), NOW())"
    data = {
        'user_id': session['user_id'],
        'message_id': message_id,
        'comment': request.form['comment']
    }
    print data
    mysql.query_db(query, data)
    return redirect("/wall")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

app.run(debug=True)
