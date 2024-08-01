"""
Aqui colocaremos los generadores y los decoradores.
"""


def turnos_perfumeria():
    x = 1
    while True:
        yield f'P - {x}'
        x += 1


def turnos_enfermeria():
    x = 1
    while True:
        yield f'E - {x}'
        x += 1


def turnos_cosmeticos():
    x = 1
    while True:
        yield f'C - {x}'
        x += 1

p = turnos_perfumeria()
e = turnos_enfermeria()
c = turnos_cosmeticos()

def Mostrar_turno(fn):

    print("\n" + "*" * 23)
    print('Su numero es:')
    if fn == 1:
        print(next(p))
    elif fn == 2:
        print(next(e))
    else:
        print(next(c))
    print('Aguarda y sera antendido.')
    print("\n" + "*" * 23)

