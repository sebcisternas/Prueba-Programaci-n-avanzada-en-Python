from datetime import date  # importa el módulo date de la librería datetime
from error import LargoExcedidoException  # importa la clase LargoExcedidoException desde el módulo error

class Campaña:
    def __init__(self, nombre: str, anuncios: list, fecha_inicio: date = None, fecha_termino: date = None):
        # constructor de la clase Campaña con atributos privados
        self.__nombre = nombre  
        self.__anuncios = anuncios  
        self.__fecha_inicio = fecha_inicio  
        self.__fecha_termino = fecha_termino  

    @property
    def nombre(self):
        # getter del nombre de la campaña
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        # setter del nombre de la campaña
        if len(nuevo_nombre) > 250:
            raise LargoExcedidoException()  # lanza una excepción si el nuevo nombre excede los 250 caracteres
        else:
            self.__nombre = nuevo_nombre

    @property
    def fecha_inicio(self):
        # getter de la fecha de inicio de la campaña
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, nuevo_fecha_inicio):
        # setter de la fecha de inicio de la campaña
        self.__fecha_inicio = nuevo_fecha_inicio
        
    @property
    def fecha_termino(self):
        # getter de la fecha de término de la campaña
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, nuevo_fecha_termino):
        # setter de la fecha de término de la campaña
        self.__fecha_termino = nuevo_fecha_termino
        
    @property
    def anuncios(self):
        # getter de la lista de anuncios asociados a la campaña
        return self.__anuncios
        

    # método especial para representar la campaña como una cadena de texto
    def __str__(self):
        
        anuncios_por_tipo = self._contar_anuncios_por_tipo()
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {', '.join([f'{cantidad} {tipo}' for tipo, cantidad in anuncios_por_tipo.items()])}"
