import pygame
import sys
import random

pygame.init()

ANCHO, ALTO = 400, 300
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa el objetivo")

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Jugador
x, y = 200, 150
tamaño = 30
velocidad = 5

# Objetivo
objetivo_x = random.randint(0, ANCHO - tamaño)
objetivo_y = random.randint(0, ALTO - tamaño)

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: x -= velocidad
    if teclas[pygame.K_RIGHT]: x += velocidad
    if teclas[pygame.K_UP]: y -= velocidad
    if teclas[pygame.K_DOWN]: y += velocidad

    # Detectar colisión
    if abs(x - objetivo_x) < tamaño and abs(y - objetivo_y) < tamaño:
        objetivo_x = random.randint(0, ANCHO - tamaño)
        objetivo_y = random.randint(0, ALTO - tamaño)

    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, AZUL, (x, y, tamaño, tamaño))
    pygame.draw.rect(pantalla, VERDE, (objetivo_x, objetivo_y, tamaño, tamaño))

    pygame.display.flip()
    reloj.tick(60)

