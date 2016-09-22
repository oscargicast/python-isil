class Padre():

    apellido_paterno = None

    def get_apellido_paterno(self):
        return self.apellido_paterno

    def zapatos(self):
        print('Hola tengo zapatos')

class Madre():

    apellido_materno = None

    def __init__(self, apellido_materno):
        self.apellido_materno = apellido_materno

    def get_apellido_materno(self):
        return self.apellido_materno

    def muebles(self):
        print('Hola tengo muebles')


class Hijo(Padre, Madre):

    nombre = None

    def __init__(self, apellido_paterno, apellido_materno):
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno

    def get_full_name(self):
        return ' '.join([self.nombre, self.apellido_paterno, self.apellido_materno])

    def muebles(self):
        print('sobreescribiendo muebles')
        super(Hijo, self).muebles()

def principal():
    hijo = Hijo(apellido_paterno='Giraldo', apellido_materno='Castillo')
    hijo.nombre = 'Oscar'
    hijo.zapatos()
    hijo.muebles()
    print(hijo.get_full_name())


if __name__ == '__main__':
    principal()