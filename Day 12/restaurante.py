from tkinter import *
import time
import datetime
import random
from tkinter import filedialog, messagebox


operador = ''
# Lista de precios para comidas
precios_comidas = [
    10.0,  # Pizza
    8.0,   # Hamburguesa
    7.0,   # Ensalada
    12.0,  # Sushi
    6.0,   # Tacos
    9.0,   # Pasta
    15.0,  # Pollo asado
    5.0,   # Sopa de verduras
    4.5,   # Sandwich
    7.0,   # Arroz con frijoles
    13.0,  # Ceviche
    10.0,  # Lasagna
    6.0,   # Quesadillas
    11.0,  # Curry
    14.0   # Paella
]

# Lista de precios para bebidas
precios_bebidas = [
    1.0,   # Agua
    2.0,   # Café
    1.5,   # Té
    3.0,   # Jugo de naranja
    2.5,   # Refresco
    1.5,   # Leche
    4.0,   # Batido de frutas
    5.0,   # Cerveza
    8.0,   # Vino
    2.5,   # Limonada
    5.0,   # Smoothie
    3.0,   # Chocolate caliente
    2.5,   # Agua de coco
    6.0,   # Mojito
    2.0    # Soda
]

# Lista de precios para postres
precios_postres = [
    4.0,   # Helado
    5.0,   # Pastel de chocolate
    4.5,   # Tarta de manzana
    6.0,   # Cheesecake
    3.5,   # Brownies
    2.0,   # Galletas
    5.5,   # Mousse de chocolate
    4.0,   # Flan
    3.0,   # Pudín
    6.5,   # Macarons
    5.0,   # Crema catalana
    3.5,   # Churros
    6.0,   # Tiramisu
    4.5,   # Panna cotta
    3.0    # Cupcakes
]

def clic_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    borrar()
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    # COMIDAS
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == 0:
                cuadros_comida[x].delete(0,END)
            texto_comida[x].set('1')
            cuadros_comida[x].focus()
        else: 
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    # BEBIDAS
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == 0:
                cuadros_bebida[x].delete(0,END)
            texto_bebida[x].set('1')
            cuadros_bebida[x].focus()
        else: 
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    # POSTRES
    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == 0:
                cuadros_postres[x].delete(0,END)
            texto_postres[x].set('1')
            cuadros_postres[x].focus()
        else: 
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

# FUNCION PARA CREAR DISTINTAS ETIQUETAS
def Etiquetas(Nombre_etiqueta, Variable, fila, columna):
    """
    Funcion que nos permite crear etiquetas
    """
    # Etiquetas de costo y campos de entrada
    etiqueta = Label(panel_costos,
                            text= Nombre_etiqueta,
                            font=('Dosis', 13, 'bold'),
                            bg='azure4',
                            fg='white')

    etiqueta.grid(row = fila, column = columna, padx=10, pady=5)

    texto = Entry(panel_costos,
                           font=('Dosis', 13, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable= Variable)

    texto.grid(row= fila, column= columna + 1, padx=10, pady=5)


def total():
    #COMIDAS
    sub_tota_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_tota_comida += (float(cantidad.get()) * precios_comidas[p])
        p += 1
    

    #BEBIDA
    sub_tota_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_tota_bebida += (float(cantidad.get()) * precios_bebidas[p])
        p += 1
    

    #POSTRES
    sub_tota_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_tota_postres += (float(cantidad.get()) * precios_postres[p])
        p += 1
    

    sub_total = sub_tota_comida + sub_tota_bebida + sub_tota_postres
    impuesto = sub_total * 0.07
    total = sub_total - impuesto

    var_costo_comida.set(f'$ {round(sub_tota_comida,2)}')
    var_costo_bebida.set(f'$ {round(sub_tota_bebida,2)}')
    var_costo_postre.set(f'$ {round(sub_tota_postres,2)}')
    var_subtotal.set(f'$ {round(sub_total,2)}')
    var_impuesto.set(f'$ {round(impuesto,2)}')
    var_total.set(f'$ {round(total,2)}')
    

def recibo():

    texto_recibo.delete(1.0,END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now( )
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{comidas[x]}\t\t{comida.get()}\t'
                                      f'$ {int(comida.get()) * precios_comidas[x]}\n')
        x += 1
    
    x = 0
    for drink in texto_bebida:
        if drink.get() != '0':
            texto_recibo.insert(END, f'{bebidas[x]}\t\t{drink.get()}\t'
                                      f'$ {int(drink.get()) * precios_bebidas[x]}\n')
        x += 1

    x = 0
    for postr in texto_postres:
        if postr.get() != '0':
            texto_recibo.insert(END, f'{postres[x]}\t\t{postr.get()}\t'
                                      f'$ {int(postr.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de las bebidas: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'\tTotal: \t{var_total.get()}\n')
    texto_recibo.insert(END, f'Lo esperamos pronto\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion','Su recibo ha sido guardado.')


def Resetear():
    texto_recibo.delete(1.0,END)
    # ELIMINAR LOS CHECKBOX
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    # DESACTIVAR CHECKBOX
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED) 

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_total.set('')
    var_impuesto.set('')

    

# Iniciar tkinder
app = Tk()

# Tamano de la ventana
app.geometry('1020x630+0+0')
# El mas es para especificar donde queremos que se establesca la ventana cuando se inicie. En que cordenadas de la pantalla.
# Primero en eje de las x y despues en eje de las Y.

# Evitar maximizar
app.resizable(0, 0)

# Titulo de ventana
app.title('Restaurante - Sistema de facturacion')

# Color de fondo
app.config(bg='bisque1')

# Panel superior
panel_superior = Frame(app, bd= 1, relief = FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de facturacion', fg='azure4',
                        font=('Dosis', 50), bg= 'burlywood', width= 27)

etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(app, bd=1, relief= FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=60)
panel_costos.pack(side=BOTTOM)

# Panel de comidas
panel_comidas = LabelFrame(panel_izquierdo, text= 'Comida',font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text= 'Bebidas',font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text= 'Postres',font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(app, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
# SINO TIENE NADA EL PACK POR DEFAULT SE COLOCA ARRIBA
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
# SINO TIENE NADA EL PACK POR DEFAULT SE COLOCA ARRIBA
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
# SINO TIENE NADA EL PACK POR DEFAULT SE COLOCA ARRIBA
panel_botones.pack()

#########################

# LISTA DE PRODUCTOS
comidas = [
    "Pizza",
    "Hamburguesa",
    "Ensalada",
    "Sushi",
    "Tacos",
    "Pasta",
    "Pollo asado",
    "Sopa de verduras",
    "Sandwich",
    "Arroz con frijoles",
    "Ceviche",
    "Lasagna",
    "Quesadillas",
    "Curry",
    "Paella"
]

bebidas = [
    "Agua",
    "Café",
    "Té",
    "Jugo de naranja",
    "Refresco",
    "Leche",
    "Batido de frutas",
    "Cerveza",
    "Vino",
    "Limonada",
    "Smoothie",
    "Chocolate caliente",
    "Agua de coco",
    "Mojito",
    "Soda"
]

postres = [
    "Helado",
    "Pastel de chocolate",
    "Tarta de manzana",
    "Cheesecake",
    "Brownies",
    "Galletas",
    "Mousse de chocolate",
    "Flan",
    "Pudín",
    "Macarons",
    "Crema catalana",
    "Churros",
    "Tiramisu",
    "Panna cotta",
    "Cupcakes"
]

# Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

for comida in comidas:
    # Crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                        text=comida.title(),
                        font=('Dosis', 10, 'bold'),
                        onvalue=1, 
                        offvalue=0,
                        variable= variables_comida[contador],
                        command=revisar_check)
    comida.grid(row=contador,
                column=0, 
                sticky=W)
    
    # Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                    font=('Dosis', 10, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador]
                                    )
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1


# Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0

for bebida in bebidas:
    # Crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, 
                        text=bebida.title(), 
                        font=('Dosis', 10, 'bold'),
                        onvalue=1, 
                        offvalue=0, 
                        variable= variables_bebida[contador],
                        command=revisar_check)
    bebida.grid(row=contador,
                column=0, 
                sticky=W)
    
    # Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                    font=('Dosis', 10, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_bebida[contador]
                                    )
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1
    

# Generar items postres
variables_postres = []
cuadros_postres = []
texto_postres= []
contador = 0

for postre in postres:
    # Crear checkbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres, 
                        text=postre.title(), 
                        font=('Dosis', 10, 'bold'),
                        onvalue=1, 
                        offvalue=0, 
                        variable= variables_postres[contador],
                        command=revisar_check)
    postre.grid(row=contador,column=0, sticky=W)
    
    # Crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                    font=('Dosis', 10, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_postres[contador]
                                    )
    cuadros_postres[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Varibales
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


Etiquetas('Costo comida', var_costo_comida, 0, 0)
Etiquetas('Costo bebida', var_costo_bebida, 0, 2)
Etiquetas('Costo postre', var_costo_postre, 1, 0)
Etiquetas('Subtotal', var_subtotal, 1, 2)
Etiquetas('Impuestos', var_impuesto, 2, 0)
Etiquetas('Total', var_total, 2, 2)

# Botones
botones = ['Total', 'Recibo', 'Guardar' ,'Reset']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',13,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=2,
                   width=9)
    
    botones_creados.append(boton)

    boton.grid(row=0,
               column= columnas)
    
    columnas += 1

botones_creados[0].config(command= total)
botones_creados[1].config(command= recibo)
botones_creados[2].config(command= guardar)
botones_creados[3].config(command= Resetear)

# Area recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width= 42,
                    height=10)

texto_recibo.grid(row=0,
                  column=0)

#Calculadora
visor_calculadora = Entry(panel_calculadora,
                        font=('Dosis', 16, 'bold'),
                        width= 32,
                        bd=1)

#GRID permite establecer donde se coloca el visor de la calculadora 
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+',
                        '4', '5', '6', '-',
                        '1', '2', '3', 'x',
                        'R', 'B', '0', '/']

botones_guardados = []

fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    
    botones_guardados.append(boton)
    
    boton.grid(row= fila,
               column= columna)
    
    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0
    
botones_guardados[0].config(command=lambda : clic_boton('7'))
botones_guardados[1].config(command=lambda : clic_boton('8'))
botones_guardados[2].config(command=lambda : clic_boton('9'))
botones_guardados[3].config(command=lambda : clic_boton('+'))
botones_guardados[4].config(command=lambda : clic_boton('4'))
botones_guardados[5].config(command=lambda : clic_boton('5'))
botones_guardados[6].config(command=lambda : clic_boton('6'))
botones_guardados[7].config(command=lambda : clic_boton('-'))
botones_guardados[8].config(command=lambda : clic_boton('1'))
botones_guardados[9].config(command=lambda : clic_boton('2'))
botones_guardados[10].config(command=lambda : clic_boton('3'))
botones_guardados[11].config(command=lambda : clic_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : clic_boton('0'))
botones_guardados[15].config(command=lambda : clic_boton('/'))



# Evitar que la pantalla se cierre.
app.mainloop()