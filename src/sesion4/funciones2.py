def suma_mejorada(*args):
    return sum(args)

def multiplica(*args):
    resultado = 1
    for num in args:
        resultado = resultado * num
        # resultado *= num
    return resultado

def multiplica_5(num):
    print(list(range(0, num + 1, 5))[1:])
    secuencia = list(range(0, num + 1, 5))[1:]
    return multiplica(*secuencia)

def foo(nombre, *args, **kwargs):
    print(nombre)
    print(args)
    print(kwargs)

def principal():
    print(suma_mejorada(5, 5, 10))  # 20.
    print(multiplica(5, 2, 3))  # 30.
    print(multiplica_5(22)) # 5 * 10 * 15 * 20
    # foo('Oscar', 1, 2, 3, a='hola', b='chao')
    # foo('ISIL', 1)
    # foo(3, 5, 5, c='asdas')

if __name__ == '__main__':
    principal()