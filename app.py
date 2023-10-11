from flask import Flask, render_template, request, redirect, url_for
from firebaseConfig import *
from claseCliente import Cliente
from models.clienteModel import ClienteModel
# flask instance creation
app = Flask(__name__)
clientesModelo = ClienteModel()

@app.route('/')
def index():
    
    clientesLista = clientesModelo.obtenerClientes()
    return render_template('index.html', clientes=clientesLista)

@app.route('/AnadirCliente', methods = ['GET','POST'])
def AnadirCliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        domicilio = request.form['domicilio']
        telefono = request.form['telefono']
        email = request.form['email']

        clientesModelo.crearCliente(nombre, apellido, domicilio, telefono, email)
        
        return redirect('/')
    else:  
        return render_template('anadirCliente.html')
    
if __name__ == '__main__':
    app.run(debug=True)