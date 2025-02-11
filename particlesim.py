import pygame
import random
import math
def summonWater(x,y, waterParticles):
    for i in range(100):
        posX = -500
        posY = -500
        while (not 0 < posX < 600) and (not 0 < posY < 600):
            r = math.sqrt(random.random())*25
            theta = random.uniform(0,2*math.pi)
            posX = r*math.cos(theta) + x
            posY = r*math.sin(theta) + y
        waterParticles.append([posX,posY, 0,0])
    return waterParticles
def drawWater(waterParticles, screen):
    for p in waterParticles:
        pygame.draw.circle(screen, (0, 120, 255), (p[0], p[1]), 1)
def physicsUpdate(waterParticles):
    for p in waterParticles:
        p[3] += .1
        if p[1] + p[3] > 599:
            p[3] = -0.8*p[3]
        p[1] += p[3]
        
    return waterParticles

waterParticles = []

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Particle Sim")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            summonWater(*event.pos,waterParticles)
            print(event.pos)
    screen.fill((255,255,255))
    drawWater(waterParticles,screen)
    pygame.display.flip()
    waterParticles = physicsUpdate(waterParticles)
    clock.tick(60)
pygame.quit()
