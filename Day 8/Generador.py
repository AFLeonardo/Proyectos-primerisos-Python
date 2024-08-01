# def fn():
#     lista = []
#     for x in range(1,5):
#         lista.append(x * 10)
#     return lista
#
#
# def generador():
#     for x in range(1,5):
#         yield x * 10
#
#
# print(fn(), generador())
#
#
# g = generador()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

######################################################

def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


h = mi_generador()

print(next(h))
print(next(h))
print(next(h))