from campaña import Campaña  # importamos la clase Campaña desde el archivo campaña.py
from anuncio import Video  # importamos la clase Video desde el archivo anuncio.py
from error import LargoExcedidoException, SubTipoInvalidoError  # importamos las clases de excepciones desde error.py

try:
    # crear una instancia de Video
    video = Video(duracion=30, sub_tipo="instream")

    # crear una instancia de Campaña con un único anuncio de tipo Video
    campaña = Campaña("Campaña de ejemplo", [video])

    # solicitar al usuario un nuevo nombre para la campaña
    nuevo_nombre = input("Ingrese el nuevo nombre para la campaña: ")

    # solicitar al usuario un nuevo subtipo para el anuncio
    nuevo_subtipo = input("Ingrese el nuevo subtipo para el anuncio: ")

    # intentar modificar el nombre de la campaña y el subtipo del anuncio
    campaña.nombre = nuevo_nombre
    campaña.anuncios[0].sub_tipo = nuevo_subtipo

except LargoExcedidoException as e:
    # en caso de excepción de LargoExcedidoException, añadir el mensaje al archivo error.log
    with open("error.log", "a") as file:
        file.write(str(e) + "\n")

except SubTipoInvalidoError as e:
    # en caso de excepción de SubTipoInvalidoError, añadir el mensaje al archivo error.log
    with open("error.log", "a") as file:
        file.write(str(e) + "\n")

except Exception as e:
    # en caso de cualquier otra excepción, añadir el mensaje al archivo error.log
    with open("error.log", "a") as file:
        file.write(str(e) + "\n")