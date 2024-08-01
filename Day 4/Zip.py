# Practica 1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

mix = list(zip(paises,capitales))

for paises,capitales in mix:
    print(f"La capital de {paises} es {capitales}")

# Practica 2
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = list(i % 2 == 0 for i in valores)
print(valores_pares)
