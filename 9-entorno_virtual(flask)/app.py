from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/"ever"')
def home(name=None):
    return render_template('index.html', name=name)

@app.route('/saludo', methods=['GET', 'POST'])
def saludo():
    nombre = request.form.get('nombre')
    edad = int(request.form.get('edad'))

    return render_template('saludo.html', name=nombre, age=edad)

app.run(debug=True)