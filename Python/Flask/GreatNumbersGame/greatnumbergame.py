import random
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
random = random.randrange(0, 101)

@app.route('/')
def main():
    return render_template('greatnumbergame.html')

@app.route('/result', methods=['POST'])
def result():
    session['number'] = request.form['number']
    number = session['number']
    print number
    print random
    if int(number) > random:
        session['result'] = 'is too high'
        color = "red"
    elif int(number) < random:
        session['result'] = 'is too low'
        color = "red"
    elif int(number) == random:
        session['result'] = 'was the right number!'
        color = "green"
    return render_template('greatnumbergameresult.html', color=color, result=session['result'], number=session['number'])

@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/')

app.run(debug=True)
