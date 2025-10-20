
import os
from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'dev-secreto-cambiar')  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

@app.route('/sesion')
def sesion():
    return render_template('sesion.html')

@app.route('/auto')
def carro():
    return '''
<h1>hola</h1>
<video src="static/img/video/autos_antiguos.mp4"></video>
'''

@app.route('/facebook', methods=['GET', 'POST'])
def facebook():
    if request.method == 'POST':
        
        nombre = request.form["firstName"]
        apellido = request.form["lastName"]
        email = request.form["email"]
        contrasena = request.form["password"]
        Confir_password = request.form["Confirmar Cotraseña"]

        
        if not contrasena or len(contrasena) < 6:
            flash('La contraseña debe tener al menos 6 caracteres.', 'danger')
            return render_template('facebook.html', nombre=nombre, apellido=apellido, email=email)

        flash(f'Cuenta creada para {nombre} {apellido} con el email {email}!', 'success')
        return redirect(url_for('facebook'))

    return render_template('facebook.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html') 

if __name__ == '__main__':
    app.run(debug=True)
