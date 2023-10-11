from clasePersona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, domicilio, telefono, email, idUsuario):
        super().__init__(nombre, apellido, domicilio, telefono, email)
        self.__idUsuario = None

    def getIdUsuario(self):
        return self.__idUsuario
    
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

        