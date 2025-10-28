from flask import Flask, render_template, url_for, redirect, request, flash, session
app = Flask(__name__)

app.config['SECRET_KEY']="Jose_Miguel7" 
USUARIOS_REGISTRADOS ={
    'admin@gmail.com':{
        'password': 'admin123',
        'nombre':'Admistrador',
        'fecha_nacimineto':'2008-04-06'
    }    
}

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
    return render_template("sesion.html")

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('index'))


@app.route("/validalogin", methods=['GET', 'POST'])
def validalogin():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        if not email or not password:
            flash('Por favor ingrese su correo y contraseña.', 'danger')
            return render_template('sesion.html')

        usuario = USUARIOS_REGISTRADOS.get(email)
        if not usuario:
            flash('Usuario no encontrado.', 'danger')
            return render_template('sesion.html')

        if password != usuario['password']:
            flash('Contraseña incorrecta.', 'danger')
            return render_template('sesion.html')

        
        session['usuario_email'] = email
        session['usuario_nombre'] = usuario['nombre']
        session['logueado'] = True
        flash(f'Bienvenido {usuario["nombre"]}!', 'success')
        return redirect(url_for('index'))

    
    return render_template('sesion.html')




@app.route('/facebook', methods=['GET', 'POST'])
def facebook():
    if request.method == 'POST':
        nombre = request.form.get("firstName", "").strip()
        apellido = request.form.get("lastName", "").strip()
        email = request.form.get("email", "").strip()
        contrasena = request.form.get("password", "")
        confirmar = request.form.get("confirm_password", "")

        if not contrasena or len(contrasena) < 6:
            flash('La contraseña debe tener al menos 6 caracteres.', 'danger')
            return render_template('facebook.html', nombre=nombre, apellido=apellido, email=email)

        if contrasena != confirmar:
            flash('Las contraseñas no coinciden.', 'danger')
            return render_template('facebook.html', nombre=nombre, apellido=apellido, email=email)

        flash(f'Cuenta creada para {nombre} {apellido} con el email {email}!', 'success')
        return redirect(url_for('index'))

    return render_template('facebook.html')



@app.route('/acerca')
def acerca():
    return render_template('acerca.html') 

if __name__ == '__main__':
    app.run(debug=True)
