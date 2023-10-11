class Persona:
    def _init_(self, nombre, apellido, domicilio, telefono, email):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__domicilio = domicilio
        self.__telefono = telefono 
        self.__email = email
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido
    
    def setApellido(self, apellido):
        self.__apellido = apellido

    def getDomicilio(self):
        return self.__domicilio
    
    def setDomicilio(self, domicilio):
        self.__domicilio = domicilio

    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, telefono):
        self.__telefono = telefono
    
    def getEmail(self):
        return self.__email 
    
    def setEmail(self, email):
        self.__email = email