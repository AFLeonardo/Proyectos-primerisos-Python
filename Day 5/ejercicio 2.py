def letra_unica(texto):
    letras = list(set(texto.lower()))
    n_letra = []
    #Pa quitar espacios

    for s in letras:
        if s == " ":
            pass
        else:
            n_letra.append(s)

    n_letra.sort()
    print(n_letra)

    # print(letras)

letra_unica("No me dijiste y sin mas nada...por que no se... pero fue...asi fueee")