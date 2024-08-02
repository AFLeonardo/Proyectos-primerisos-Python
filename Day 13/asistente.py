import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# =============================================================================

# Id de voces
Zira = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'
David = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
Sabina = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0'

# Escuchar nuestro micro y devolver el audio como texto
def Transformar_audio_a_texto():
    """ Almacenar recognizer en variable"""
    r = sr.Recognizer()

    # Configurar el micro
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # Guardar lo que escuche
        audio = r.listen(origen)

        try:
            # Buscar en google 
            pedido = r.recognize_google(audio, language='es-mx')
            return pedido
        
        # En caso de no comprender el audio.
        except sr.UnknownValueError:
            print('Ups...no entendí')
            return 'sigo esperando'
        
        # En caso de no resolver el pedido
        except sr.RequestError:
            print("Ups, no hay servicio")
            return "sigo esperando"
        
        # Error inesperado
        except Exception as e:
            print(f'Ups, algo salió mal: {e}')
            return "sigo esperando"

# Funcion para que el asistente hable
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', Sabina)

    # Pronunciar
    engine.say(mensaje)
    engine.runAndWait()

# Informar el dia de la semana
def pedir_dia():
    """
    Nos dice el dia actual.
    """
    #Crear variables de datos hoy
    dia = datetime.date.today()

    # Crear variable para el dia de la semana
    dia_semana = dia.weekday()

    # Diccionario con nombres de dias
    calendario = {  0: 'Lunes',
                    1: 'Martes',
                    2: 'Miércoles',
                    3: 'Jueves',
                    4: 'Viernes',
                    5: 'Sábado',
                    6: 'Domingo'}
    
    # Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}, {dia.day} de {dia.strftime("%B")} del {dia.year}')

# Informar la hora
def pedir_hora():
    """
    Nos dice la hora actual.
    """
    # Variable con datos de hora
    hora = datetime.datetime.now()
    hablar(f'La hora actual son las {hora.hour} horas, con {hora.minute} minutos.')

def saludo_inicial():
    # Conocer la hora para ajustar el saludo.
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    hablar(f'Hola, {momento}. Te habla Vanesa, tu asistente. Si ocupas algo no dudes en decírmelo, carita feliz.')

# Funcion central del asistente
def pedir_cosas():
    # Saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # LOOP central
    while comenzar:
        # Activar el micro y guardar el pedido en un string
        pedido = Transformar_audio_a_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto papa, que buena eleccion')
            webbrowser.open('https://www.youtube.com')
        elif 'haciéndolo fino' in pedido:
            hablar('Uufff, te rifaste que buen disco. Aquí tienes jefe.')
            webbrowser.open('https://www.youtube.com/watch?v=yuotTX-Lya4&list=OLAK5uy_kWae1m6ALooInLTALPvh-LXrUnRAPbnHY&index=1')
        elif 'abre google' in pedido:
            hablar('Abriendo el navegador.')
            webbrowser.open('https://www.google.com.mx/?hl=es-419')
        elif 'qué día es hoy' in pedido:
            pedir_dia()
        elif 'qué hora es' in pedido:
            pedir_hora()
        elif 'cuéntame un chiste' in pedido:
            hablar(pyjokes.get_joke('es', "all"))
        elif 'adiós' in pedido or 'chao' in pedido:
            hablar('Hasta luego papito, que tengas un buen día.')
            comenzar = False
        

pedir_cosas()
