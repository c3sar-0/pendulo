import pygame, math
from timeit import default_timer as timer

width = 800
height = 400
                                # NECESITO UNA ESCALA
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
start = timer()
tiempo = 0

vel = 0
acc = 0
theta0 = 0
theta = 0
length = 0

class Ball(object):
    def __init__(self, XY, radio):
        self.x = XY[0] # x e y iniciales van a ser donde dé click, luego van a depender de theta()
        self.y = XY[1]
        self.radio = radio
    def drawball(self, bg):
        pygame.draw.lines(bg, (50, 50, 50), False, [(width/2,50), (self.x,self.y)], 2)
        pygame.draw.circle(bg, (100, 100, 100), (self.x, self.y), self.radio)
        pygame.draw.circle(bg, (170, 0, 0), (self.x, self.y), self.radio-2)

def lengthF(xy):
    length = math.sqrt(math.pow(xy[0]-width/2, 2) + math.pow(xy[1]-50, 2))
    return(length)

def theta0F(xy): 
    theta0 = math.atan((xy[0]-width/2)/(xy[1]-50)) # ANGULO INICIAL
    return(theta0)

def thetaF(lon): # ANGULO EN FUNCION DE t
    tiempo = timer()
    t = tiempo - start
    thetaFV = theta0 * math.sin(math.sqrt(lon/9.8) * t + theta0) # theta = theta0sin(wt + phi)
    return(thetaFV)

def trayectoria(lon, ang):
    xt = lon * math.sin(ang) # Valores de x e y para cada angulo (thetaF)
    yt = lon * math.cos(ang)
    pendulo.x = xt
    pendulo.y = yt

def actualizar():
    screen.fill((255, 255, 255))
    pendulo.drawball(screen)
    pygame.display.update()

pendulo = Ball([0, 1], 10) # valores random para iniciar la clase
out = False
inicio = True

"""start = timer()
def time():
    tiempo = timer()
    return(tiempo)"""

while not out:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            out = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pendulo = Ball(pygame.mouse.get_pos(), 10)
            theta = theta0F(pygame.mouse.get_pos())
            length = lengthF(pygame.mouse.get_pos())
    theta += thetaF(length)
    trayectoria(length, theta)
    actualizar()
pygame.quit()