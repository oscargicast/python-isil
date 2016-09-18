# Para ejecutar este programa escribirdesde la terminal:
# python hola.py Isil

# Importamos los modulos que necesitamos usar.
# sys es uno muy estandard.
import sys

# Juntamos todo nuestro codigo en la funcion principal.
def principal():
    # Los argumentos escritos en la linea de comandos estan en:
    # sys.argv[1], sys.argv[2] ...
    print('Hola', sys.argv[1])
    # sys.argv[0] es el nombre del script que estamos ejecutando.
    print('Soy el modulo', sys.argv[0])

# Para llamar a nuestra funcion principal para iniciar el
# programa usamos lo siguiente.
if __name__ == '__main__':
    principal()