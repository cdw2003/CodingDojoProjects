from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form():
  return render_template('colorpicker.html')

@app.route('/', methods=['POST'])
def changeColor():
   red = request.form['red']
   green = request.form['green']
   blue = request.form['blue']
   print red
   return render_template('colorpicker.html', red=red, green=green, blue=blue)

app.run(debug=True)
