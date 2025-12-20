# definir clase
class MiClase:
    pass

clase = MiClase()

# métodos
class Metodos:
    def metodo(self):
        pass
    @classmethod
    def metodo_clase(cls): # siempre es necesario el parametro cls que hace referencia a la propia clase
        pass
    @staticmethod
    def metodo_estatico(): # el metodo estático no debe modificar el estado del objeto o la clase
        pass


# atributos
class Atributos:
    atributo_clase = 'Atributo' # comun a todas las instancias
    def encender(self):
        self.encendido = True
        self.__atributo_privado = 33


# metodo __init__ con atributos
class ConInit:
    def __init__(self):
        self.nombre = 'Un nombre'

# propiedades
class ConPropiedades:
    def __init__(self):
        self.edad = 33
    @property
    def mayor_edad(self) -> int:
        return self.edad >= 18



# sobrescribiendo operadores en las clases
# por ejemplo a == b -> __eq__
class EjemploOperadores:
    def __eq__(self, other):
        if isinstance(other, EjemploOperadores): # comprobamos primero si los dos objetos son de la misma clase!
            return self.nombre == other.nombre
        return False
# lista de operadores:
# == __eq__, != __ne__, < __lt__, > __gt__, <= __le__, >= __ge__
# + __add_, - __sub__, * __mul__, / __truediv__, % __mod__, x^n __pow__
# __str__

# herencia
class Vehiculo:
    def metodo(self):
        pass
class Moto(Vehiculo): # python soporta multiherencia, Moto(Vehiculo, OtraClasePadre)
    def metodo(self):
        pass
    def evitar_colision_metodos_clase_padre(self):
        super().metodo()

# modulos
import sys
from stats import mean as m
# paquetes: son ficheros .py Dentro del paquete estan los modulos, y dentro de los modulos las funciones


