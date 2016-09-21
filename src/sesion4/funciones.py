def suma(a, b, c, d=0, e=0):
    return a + b + c + d + e

def suma_cuadrado(a, b, c):
    return a ** 2 + b ** 2 + c ** 2

def print_n(frase, n=1):
    print((frase + ' ') * n)

def principal():
    resultado = suma(5, 6.5, 9.35, 67)
    print(resultado)

    resultado = suma(a=5, b=6.5, c=9.35, d=67)
    print(resultado)

    resultado = suma_cuadrado(5, 6.5, 9.35)
    print(resultado)

    print_n(frase="hola", n=5)
    # hola hola hola hola

if __name__ == '__main__':
    principal()