import firebase_admin  
from firebase_admin import db

class ClienteModel:
    def __init__(self):
        # No es necesario inicializar Firebase en el método __init__,
        # ya que la inicialización de Firebase se ha realizado en el archivo 'firebaseconfig.py'.
        pass

    #Método encargado de recibir los datos del cliente y crearlo en la base de datos
    def crearCliente(self, nombre, apellido, domicilio, telefono, email):
        # Crea un nuevo cliente en Firebase
        ref = db.reference('/clientes')
        nuevoCliente = ref.push({
            'nombre': nombre,
            'apellido': apellido,
            'domicilio': domicilio,
            'telefono': telefono,
            'email': email
        })
        return nuevoCliente.key

    #Método encargado de obtener los datos de todos los clientes
    def obtenerClientes(self):
        # Lee todos los clientes desde Firebase
        ref = db.reference('/clientes')
        return ref.get()

    #Método encargado de obtener los datos de un cliente por su ID
    def obtenerClientePorId(self, clienteId):
        # Lee un cliente específico por su ID
        ref = db.reference('/clientes')
        return ref.child(clienteId).get()

    #Método encargado de actualizar los datos de un cliente
    def actualizarCliente(self, clienteId, nombre, apellido, domicilio, telefono, email):
        # Actualiza un cliente existente
        ref = db.reference('/clientes')
        ref.child(clienteId).update({
            'nombre': nombre,
            'apellido': apellido,
            'domicilio': domicilio,
            'telefono': telefono,
            'email': email
        })
    
    #Método encargado de eliminar los datos de un cliente
    def eliminarCliente(self, clienteId):
        # Elimina un cliente por su ID
        ref = db.reference('/clientes')
        ref.child(clienteId).delete()

    #Método encargado de obtener los datos de un cliente por su apellido
    def obtenerClientePorApellido(self, apellidoCliente):
        ref = db.reference('/clientes')
        # Realiza una consulta para buscar clientes por nombre
        resultados = ref.order_by_child('apellido').equal_to(apellidoCliente).get()
        return resultados