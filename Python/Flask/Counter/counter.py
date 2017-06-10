from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def runCounter():
    try:
        session['count'] += 1
    except:
        session['count'] = 1
    return render_template('counter.html', count = session['count'])

@app.route('/plustwo', methods=['POST'])
def addTwo():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
