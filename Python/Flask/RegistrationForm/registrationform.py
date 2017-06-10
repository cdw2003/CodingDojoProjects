from flask import Flask, render_template, request, redirect, flash
import re
app = Flask(__name__)
app.secret_key = 'This is secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/submit', methods=['POST'])
def createuser():
    if len(request.form['firstname']) < 1:
        flash("First name must be entered!")
        return redirect('/')

    if len(request.form['lastname']) < 1:
        flash("Last name must be entered!")
        return redirect('/')

    if request.form['firstname'].isalpha() == False or request.form['lastname'].isalpha() == False:
        flash("First and Last name must not contain any numbers.")
        return redirect('/')

    if len(request.form['email']) < 1:
        flash("Email must be entered!")
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!')
        return redirect('/')

    if len(request.form['password']) < 1:
        flash("Password must be entered!")
        return redirect('/')

    if len(request.form['password']) < 8:
        flash("Password should be at least 8 characters")
        return redirect('/')

    countint = 0
    for i in request.form['password']:
        if i.isnumeric() == True:
            countint += 1

    if countint == 0:
        flash("Your password must have at least 1 number!")
        return redirect('/')

    countupper = 0
    for i in request.form['password']:
        if i.isupper() == True:
            countupper += 1

    if countupper == 0:
        flash("Your password must have at least 1 uppercase character!")
        return redirect('/')

    if len(request.form['pwconfirm']) < 1:
        flash("You must confirm your password!")
        return redirect('/')

    if request.form['password'] != request.form['pwconfirm']:
        flash("Password and password confirm should match!")
        return redirect('/')

    else:
        flash("Thanks for submitting your information.")
        return redirect('/')

app.run(debug=True)
