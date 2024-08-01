def contar_primos(num):
    # Mostar en pantalla todos los numeros primos exsistentes
    pares = []
    cantidad_encontrada = 0
    for n in range(2, num+2):
        if n == 0 or n == 1:
            pass
        elif n % 2 == 0:
            pares.append(n)
            cantidad_encontrada += 1
        else:
            pass

    print(f"Los numeros pares encontrados fueron {pares}.")
    return cantidad_encontrada


contar_primos(0)
