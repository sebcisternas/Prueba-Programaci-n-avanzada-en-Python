from error import SubTipoInvalidoError

class Anuncio:
    formato={}
    SUB_TIPOS=() #atributo de clase sub-tipos, este se inicializara de una forma dependiendo del tipo de clase hija llamemos (video,display, o social)
    
    # constructor de la clase Anuncio
    def __init__(self,ancho: int, alto: int,url_archivo: str,url_click: str,sub_tipo: str) -> None:
        self.__ancho = ancho
        self.__alto  = alto
        self.__url_archivo= url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo # utilizamos el setter para validar el subtipo al inicializar el objeto
    
    
    # método estático para mostrar los formatos de anuncio disponibles
    @staticmethod
    def mostrar_formatos():
        print("Formatos de anuncio disponibles:")
        print("===============================")
        
        # mostrar formatos y subtipos de Video
        print("Video:")
        print("------")
        for subtipo in Video.SUB_TIPOS:
            print(f"- {subtipo}")
        
        # mostrar formatos y subtipos de Display
        print("\nDisplay:")
        print("--------")
        for subtipo in Display.SUB_TIPOS:
            print(f"- {subtipo}")
        
        # mostrar formatos y subtipos de Social
        print("\nSocial:")
        print("-------")
        for subtipo in Social.SUB_TIPOS:
            print(f"- {subtipo}")

      

        
            
    @property
    def ancho(self):
        return self.__ancho
        
    @ancho.setter
    def ancho(self,nuevo_ancho):
        if nuevo_ancho > 0 :
            self.__ancho = nuevo_ancho
        else:
            self.__ancho = 1
                
    @property
    def alto(self):
        return self.__alto
        
    @alto.setter
    def alto(self,nuevo_alto: int):
        if nuevo_alto > 0 :
            self.__alto= nuevo_alto
        else:
            self.__alto = 1     
        
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @property
    def url_click(self):
        return self.__url_click
    
    @url_archivo.setter
    def url_archivo (self, nuevo_url_archivo: str):
        self.__url_archivo = nuevo_url_archivo
        
    @url_click.setter
    def ulr_click(self, nuevo_url_click: str):
        self.__url_click = nuevo_url_click
        
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo: str):
        if nuevo_sub_tipo in self.SUB_TIPOS: # verifica si el nuevo subtipo está en la lista de subtipos del anuncio
            self.__sub_tipo = nuevo_sub_tipo
        else:
            raise SubTipoInvalidoError() #lanza una excepción si el subtipo no es válido

        
class Video(Anuncio):
    FORMATO = "Video" #formato del anuncio
    SUB_TIPOS=("instream","outstream") # subtipos disponibles para el anuncio de video

    def __init__(self, duracion: int, sub_tipo: str) -> None:
        super().__init__(ancho=1, alto=1, url_archivo="", url_click="", sub_tipo=sub_tipo)
        self.duracion = duracion # atributo duración del video

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, nueva_duracion):
        if nueva_duracion > 0:
            self._duracion = nueva_duracion
        else:
            self._duracion = 5 #si la duración es negativa o cero, se asigna un valor predeterminado de 5 segundos

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
        
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, nuevo_ancho):
        pass  # el setter no hace nada, ignorando cualquier intento de cambiar el valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, nuevo_alto):
        pass  # el setter no hace nada, ignorando cualquier intento de cambiar el valor
        
        
        
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    
   
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")
   
        
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook","linkedin")
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
        
    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
        
        
        
      
