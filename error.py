class Error(Exception): # clase base para las excepciones personalizadas
    pass 


class SubTipoInvalidoError(Error):
    def __init__(self, mensaje="El subtipo proporcionado no es válido para este tipo de anuncio"):
        self.mensaje = mensaje # mensaje de error predeterminado
        super().__init__(self.mensaje)# llamada al constructor de la clase base con el mensaje de error
        
        
class LargoExcedidoException(Error):
    def __init__(self, mensaje="El Nombre excede el largo permitido (250 caracteres)"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)