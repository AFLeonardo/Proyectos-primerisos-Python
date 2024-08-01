habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif sabe_python and habla_ingles == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")
