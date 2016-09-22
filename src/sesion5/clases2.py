import requests

from clases1 import Gato


class PhotoGato(Gato):

    CHUNK_SIZE = 100
    EXTENSION = '.jpg'

    def __init__(self, nombre, ancho, largo):
        self.nombre = nombre
        self.ancho = ancho
        self.largo = largo

    def genera_url(self, ancho, largo):
        return 'https://placekitten.com/g/{}/{}'.format(ancho, largo)

    def genera_imagen(self, filename, response):
        with open(filename, 'wb') as fd:
            for chunk in response.iter_content(self.CHUNK_SIZE):
                fd.write(chunk)

    def obtener_imagen(self):
        r = requests.get(
            self.genera_url(ancho=self.ancho, largo=self.largo),
            stream=True,
        )
        filename = self.nombre + self.EXTENSION
        self.genera_imagen(filename, r)


def principal():
    felix = PhotoGato(nombre='Felix', ancho=500, largo=1000)
    felix.obtener_imagen()
    felix.maullar_n_veces(50)

if __name__ == '__main__':
    principal()