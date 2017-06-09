import random
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
random1 = random.randrange(10, 21)
random2 = random.randrange(5, 11)
random3 = random.randrange(2, 6)
random4 = random.randrange(-50, 51)

@app.route('/')
def main():
    gold = session['gold']
    result = ""
    return render_template('ninjagold.html', gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def points():
    session['location'] = request.form['building']
    if session['location'] == "farm":
        session['gold'] += random1
        session['result'] += "Earned " + str(random1) + " golds from the " + session['location'] + "\n"
    elif session['location'] == "cave":
        session['gold'] += random2
        session['result'] += "Earned " + str(random2) + " golds from the " + session['location'] + "\n"
    elif session['location'] == "house":
        session['gold'] += random3
        session['result'] += "Earned " + str(random3) + " golds from the " + session['location'] + "\n"
    elif session['location'] == "casino":
        session['gold'] += random4
        if random4 > 0:
            session['result'] += "Earned " + str(random4) + " golds from the " + session['location'] + "\n"
        if random4 < 0:
            session['result'] += "Entered a casino and lost " + str(random4) + "...Ouch." + "\n"
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['gold'] = 0
    session['result'] = ""
    return redirect('/')

app.run(debug=True)
