import pygame
import math

width, height = 800, 400
vel = 0
acc = 0
out = False
length = 0
angle = 0

black = [0, 0, 0]
white = [255, 255, 255]

pygame.init()
background = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class ball(object):
    def __init__(self, XY, radius):
        self.x = XY[0]
        self.y = XY[1]
        self.radius = radius
    def draw(self, bg):
        pygame.draw.lines(bg, black, False, [(width/2, 50), (self.x, self.y)], 2)
        pygame.draw.circle(bg, black, [self.x, self.y], self.radius)

def angle_length(): # angle, length - iniciales
    length = math.sqrt(math.pow(pendulum.x-(width/2), 2) + math.pow(pendulum.y-50, 2))
    angle = math.asin((pendulum.x - width/2)/length)
    return(angle, length)
def trayectoria(angle0, length):
    pendulum.x = round(width/2 + length * math.sin(angle))
    pendulum.y = round(50 + length * math.cos(angle))

def redraw():
    background.fill(white)
    pendulum.draw(background)
    pygame.display.update()

pendulum = ball((int(width/2), -100), 5) # estas coordenadas no importan, hay que referirse a la clase por redraw().

while not out:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            out = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pendulum = ball(pygame.mouse.get_pos(), 5)
            angle, length = angle_length()
    acc = -0.005 * math.sin(angle)
    vel += acc
    vel *= 1
    angle += vel
    trayectoria(angle, length)
    redraw()

pygame.quit()