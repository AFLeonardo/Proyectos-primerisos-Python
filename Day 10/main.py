import pygame
import random
import math
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Configurar pantalla
screen = pygame.display.set_mode((800, 600)) 

# Título e ícono
pygame.display.set_caption('Invasion vacuna')
icono = pygame.image.load('Day 10\\vaca.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Day 10\\fondo.jpg')

# Música de fondo
# Descomenta las siguientes líneas si tienes un archivo de música
# mixer.music.load('Day 10\\Musica.mp3')
# mixer.music.set_volume(0.3)
# mixer.music.play(-1)

# Variables del jugador
img_jugador = pygame.image.load('Day 10\\astronave.png')
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0
jugador_y_cambio = 0
puntaje = 0

# Variables de los enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 10

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('Day 10\\Enemigo.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# Variables de la bala
img_bala = pygame.image.load('Day 10\\bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# Función del jugador
def jugador(x, y):
    screen.blit(img_jugador, (x, y))

# Función del enemigo
def enemigo(x, y, i):
    screen.blit(img_enemigo[i], (x, y))

# Función de la bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    screen.blit(img_bala, (x + 16, y + 10))

# Función de colisión
def Colision(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia <= 27

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Fondo de pantalla
    screen.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            se_ejecuta = False
        
        # Movimiento del jugador
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.5
            elif evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5
            elif evento.key == pygame.K_UP:
                jugador_y_cambio = -0.5
            elif evento.key == pygame.K_DOWN:
                jugador_y_cambio = 0.5
            elif evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jugador_y_cambio = 0

    # Actualizar posición del jugador
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio

    # Limitar al jugador en los bordes
    jugador_x = max(0, min(jugador_x, 736))
    jugador_y = max(0, min(jugador_y, 536))

    # Movimiento de los enemigos
    for i in range(cantidad_enemigos):
        enemigo_x[i] += enemigo_x_cambio[i]
        if enemigo_x[i] <= 0:
            enemigo_x_cambio[i] = 0.3
            enemigo_y[i] += enemigo_y_cambio[i]
        elif enemigo_x[i] >= 736:
            enemigo_x_cambio[i] = -0.3
            enemigo_y[i] += enemigo_y_cambio[i]

        # Colisiones
        colision = Colision(enemigo_x[i], enemigo_y[i], bala_x, bala_y)
        if colision:
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[i] = random.randint(0, 736)
            enemigo_y[i] = random.randint(50, 200)
            print(puntaje)

        enemigo(enemigo_x[i], enemigo_y[i], i)

    # Movimiento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)
    
    pygame.display.update()
