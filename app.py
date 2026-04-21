from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        return render_template('gracias.html', nombre=nombre, email=email)
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)