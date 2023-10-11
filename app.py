from flask import Flask, render_template, request, redirect, url_for
from firebaseConfig import *
from claseCliente import Cliente
from models.clienteModel import ClienteModel

app = Flask(__name__)
clientesModelo = ClienteModel()

@app.route('/')
def index():
    busqueda=True
    apellido = request.args.get('apellido')
    
    if apellido:
        # Si se proporciona un apellido, realiza la búsqueda
        resultadosClienteApellido = clientesModelo.obtenerClientePorApellido(apellido)
        if resultadosClienteApellido:
            # Si hay resultados, los mostramos
            return render_template('index.html', clientes=resultadosClienteApellido, search_term=apellido, busqueda=False)
        else:
            # Si no hay resultados, mostramos un mensaje
            return render_template('index.html', message="No se encontraron resultados para el apellido: " + apellido)
    else:
        # Si no se proporciona un apellido, muestra a todos los clientes
        clientesLista = clientesModelo.obtenerClientes() 
        if clientesLista:
            # Si hay clientes, los mostramos
            return render_template('index.html', clientes=clientesLista, busqueda=busqueda)
        else:
            # Si no hay clientes, mostramos un mensaje
            return render_template('index.html', message="No hay clientes en la base de datos. Agregue uno para visualizar.")

@app.route('/AnadirCliente', methods = ['GET','POST'])
def AnadirCliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        domicilio = request.form['domicilio']
        telefono = request.form['telefono']
        email = request.form['email']

        cliente = Cliente(nombre,apellido,domicilio,telefono,email)
        clientesModelo.crearCliente(nombre, apellido, domicilio, telefono, email)
        
        return redirect('/')
    else:  
        return render_template('anadirCliente.html')
    
@app.route('/ModificarCliente/<clienteid>', methods=['GET', 'POST'])
def ModificarCliente(clienteid):
    cliente = clientesModelo.obtenerClientePorId(clienteid)

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        domicilio = request.form['domicilio']
        telefono = request.form['telefono']
        email = request.form['email']
        clientesModelo.actualizarCliente(clienteid, nombre, apellido, domicilio, telefono, email)
        return redirect('/')
    else:
        return render_template('modificarCliente.html', cliente=cliente, clienteid=clienteid)

@app.route('/EliminarCliente/<clienteid>', methods=['GET', 'POST'])
def EliminarCliente(clienteid):
    clientesModelo.eliminarCliente(clienteid)
    return redirect('/')

@app.route('/buscarCliente')
def buscarCliente():
    apellido = request.args.get('apellido')
    return redirect(url_for('index', apellido=apellido))

if __name__ == '__main__':
    app.run(debug=True)