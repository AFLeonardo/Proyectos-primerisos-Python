def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    numeros = [num1, num2, num3]

    if suma > 15:
        return print(max(numeros))
    elif suma < 10:
        return print(min(numeros))
    else:
        numeros.reverse()
        return print(numeros[1])


devolver_distintos(7,4,1)
