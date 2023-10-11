from clasePersona import Persona
#Clase CLIENTE hereda de PERSONA, la cual actua como superclase
class Cliente(Persona):
    def __init__(self, nombre, apellido, domicilio, telefono, email):
        super().__init__(nombre, apellido, domicilio, telefono, email)
        self.__idUsuario = None
    #ABSTRACCION Y ENCAPSULAMIENTO
    def getIdUsuario(self):
        return self.__idUsuario
    
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    #POLIMORFISMO: tanto la clase Cliente como la clase Persona poseen un metodo llamado obtenerDatos, pero este se comporta de manera distinta.
    def obtenerDatos(self):
        return self.getNombre(), self.getApellido(), self.getDomicilio(), self.getTelefono(), self.getEmail(), self.getIdUsuario()
        