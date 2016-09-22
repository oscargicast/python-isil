class Gato():

    def __init__(self, nombre, color='negro', tamano='pequeno'):
        self.nombre = nombre
        self.color = color
        self.tamano = tamano

    def saludar(self):
        print('Hola soy', self.nombre)

    def maullar(self):
        print('Miauu...')

    def maullar_n_veces(self, n):
        for _ in range(n):
            self.maullar()


def principal():
    felix = Gato(nombre='Felix')
    felix.saludar()
    felix.maullar()
    print(felix.tamano)
    print(felix.color)

    garfield = Gato(
        nombre='Garfield',
        color='naranja',
        tamano='mediano',
    )
    garfield.saludar()
    garfield.maullar_n_veces(5)

if __name__ == '__main__':
    principal()