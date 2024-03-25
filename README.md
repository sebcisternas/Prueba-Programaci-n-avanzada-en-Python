# Prueba-Programacion-avanzada-en-Python
Python 3.8.

## Descripción del Trabajo

Este proyecto consiste en la implementación de un sistema de gestión de campañas publicitarias en Python, utilizando programación orientada a objetos. Se han definido clases y atributos estáticos para representar diferentes tipos de anuncios, así como excepciones personalizadas para manejar errores específicos del sistema.

### Enunciado

El enunciado requiere:

1. **Creación de Clases y Atributos Estáticos:** Se deben definir clases para representar campañas y anuncios, con atributos estáticos para manejar los diferentes tipos de anuncios y subtipos disponibles.
   
2. **Sobrecarga de Funciones Especiales:** Se solicita la sobrecarga de funciones especiales como `__init__` y `__str__` para inicializar objetos y representarlos como cadenas de texto, respectivamente.

3. **Implementación de Especificación Técnica:** Se deben aplicar conceptos de herencia, definir métodos abstractos y propiedades con getter y setter según la especificación técnica proporcionada.

4. **Uso de Colaboración y Composición:** Se debe aplicar composición para crear componentes necesarios en las clases compuestas, así como colaboración entre clases para realizar ciertas operaciones.

5. **Flujos de Excepción y Escritura de Archivos:** Se requiere manejar flujos de excepción mediante la creación de clases de excepción personalizadas y escribir mensajes de error en un archivo `error.log` cuando sea necesario.

## Solución

Para resolver este proyecto, se han creado los siguientes archivos:

- **anuncio.py:** Contiene las clases `Anuncio`, `Video`, `Display` y `Social`, que representan los diferentes tipos de anuncios y sus subtipos. Se han definido atributos estáticos para los subtipos y métodos para la gestión de anuncios.

- **campaña.py:** Define la clase `Campaña` para representar campañas publicitarias. Se implementan propiedades con getter y setter para los atributos privados, así como métodos para contar anuncios por tipo y una representación en cadena de texto.

- **error.py:** Contiene las clases `Error`, `SubTipoInvalidoError` y `LargoExcedidoException` para manejar errores específicos del sistema.

- **demo.py:** Un script de demostración que crea una instancia de `Campaña` con un único anuncio de tipo `Video`, y permite al usuario modificar el nombre de la campaña y el subtipo del anuncio mediante la entrada de texto.

En la solución se han aplicado los conceptos de herencia, composición y colaboración entre clases según lo requerido en el enunciado. Además, se han manejado flujos de excepción para garantizar la integridad y robustez del sistema.