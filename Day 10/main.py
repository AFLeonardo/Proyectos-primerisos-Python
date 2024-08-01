import pygame
import random
import math
from pygame import mixer

pygame.init() # Inicializar Pygame

screen = pygame.display.set_mode((800, 600)) # Se coloca la resolucion de la venta donde se muestra el juego.

se_ejecuta = True

#Titulo e icono
pygame.display.set_caption('Invasion vacuna')
icono = pygame.image.load('Day 10\\vaca.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Day 10\\fondo.jpg')

# AGREGAMOS MUSICA
mixer.music.load()
mixer.music.set_volume(0.3)
mixer.music.play(-1) # -1 PARA QUE SE REPITA INFINITAMENTE

# Variables del Jugador
img_jugador = pygame.image.load('Day 10\\astronave.png')
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0
jugador_y_cambio = 0
Puntaje = 0

# Variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio =[]
enemigo_y_cambio = []
cantidad_enemigos = 10

for e in range(cantidad_enemigos):
    img_enemigo = pygame.image.load('Day 10\\Enemigo.png')
    enemigo_x = random.randint(0,736)
    enemigo_y = random.randint(50,200)
    enemigo_x_cambio = 0.3
    enemigo_y_cambio = 50

# Variables bala
img_bala = pygame.image.load('Day 10\\bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# Funcion del jugador
def jugador(x, y):
    """
    Funcion que permite mover al jugador.
    """
    screen.blit(img_jugador, (x, y))

# Funcion del enemigo
def enemigo(x, y):
    """
    Funcion que permite mover al enemigo.
    """
    screen.blit(img_enemigo, (x, y))

#Funcion de bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    screen.blit(img_bala, (x + 16, y + 10))

#Funcion de distancia
def Colision(x1, x2, y1, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if distancia <= 27:
        return True
    else:
        return False
    

#Loop del juego
while se_ejecuta:
    # RGB 
    # Se pasan los parametros en tuplas
    screen.blit(fondo,(0,0))
    
    for evento in pygame.event.get():
        # QUIT es el evento cuando se hace clic en la cruz de cerrar ventanas.
        if evento.type == pygame.QUIT: 
            se_ejecuta = False
        
        # DENTRO DE PYGAME TODO ES UN EVENTO
        # EL PRESIONAR UNA TECLA ES UN EVENTO
        # DETECTAMOS EL PRESIONAR UNA TECLA Y AJUSTAMOS LA POSION DEL JUGADOR
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = - 0.5
            elif evento.key == pygame.K_RIGHT:
                jugador_x_cambio =  0.5
            elif evento.key == pygame.K_UP:
                jugador_y_cambio =  - 0.5
            elif evento.key == pygame.K_DOWN:
                jugador_y_cambio =  0.5
            elif evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # MOVER AL JUGADOR
        if evento.type == pygame.KEYUP:
            # EN EJE X
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
            # EN EJE Y
            elif evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jugador_y_cambio = 0

    # ACTULIZACION DE POSICION DEL JUGADOR
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio

    # LIMITACION DE BORDES DEL JUGADOR
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
    elif jugador_y <= 0:
        jugador_y = 0
    elif jugador_y >= 536:
        jugador_y = 536

    # ACTULIZACION DE POSION DEL ENEMIGO
    for e in cantidad_enemigos:
        enemigo_x += enemigo_x_cambio

        # Rebotar al enemigo horizontalmente y descender
        if enemigo_x <= 0:
            enemigo_x_cambio = 0.3
            enemigo_y += enemigo_y_cambio
        elif enemigo_x >= 736:
            enemigo_x_cambio = -0.3
            enemigo_y += enemigo_y_cambio

    # MOVIMIENTO BALA
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Limitar el enemigo en la pantalla verticalmente
    if enemigo_y >= 536:  # 600 (alto de la pantalla) - 64 (alto de la imagen del enemigo)
        enemigo_y = 536

    # Colisiones
    colision = Colision(enemigo_x, enemigo_y, bala_x, bala_y)
    if colision:
        sonido = mixer.Sound('')
        sonido.play()
        bala_y = 500
        bala_visible = False
        Puntaje += 1
        enemigo_x = random.randint(0,736)
        enemigo_y = random.randint(50,200)
        print(Puntaje)


    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)
    
    

    # ACTUALIZAR
    pygame.display.update()

