import pygame, math
from timeit import default_timer as timer


##### IMPLEMENTACIÓN DE ESCALA Y CORRECIÓN DE LA ECUACIÓN DEL ÁNGULO (sqrt(g/l)) #####

width = 800
height = 400
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

axis = (400, 0)
xy = [0,0]
t = 0
theta0 = 0
theta = 0
length = 1


class Ball(object): # Péndulo
  def __init__(self, xy):
    self.x = xy[0]
    self.y = xy[1]
  
  def draw(self):
    pygame.draw.lines(screen, (50,50,50), False, (axis, (self.x, self.y)))
    pygame.draw.circle(screen, (100, 100, 100), (self.x, self.y), 17)


def lengthF(): # Longitud del Péndulo
  lengthFV = (math.sqrt(math.pow(xy[0]-axis[0],2) + math.pow(xy[1]-axis[1],2)))
  return(lengthFV)

def thetaF(t): # Ángulo en función del tiempo
  thetaFV = (theta0 * math.sin(math.sqrt(9.8/(length/1000)) * t + theta0)) # w = (sqrt(g/l)) ####################################
  return(thetaFV) # ESCALA: 1m = 1000px

def theta0F(y): # Ángulo inicial
  theta0FV = math.acos((y-axis[1])/length) # Si hago lengthFV / 100 esto da math domain error # es porque ej: y = 200 -> y/len = 2 -> acos(2) no existe
  return(theta0FV)                          ## TENDRIA QUE DIVIDIR "Y" TAMBIEN (por lo que no es necesario y basta con hacerlo en thetaF)

def update(): # Dibujar el péndulo y actualizar la pantalla
  pendulo.draw()
  pygame.display.update()

def get_position(): # x e y en función de theta (en función del tiempo)
  x = length * math.sin(theta) + axis[0] ########################### creo que tiene sentido
  y = length * math.cos(theta)
  return([x, y])

def move(): # Actualizar valores de x e y en el péndulo
  pendulo.x = xy[0]
  pendulo.y = xy[1]

def info(text, position): # Mostrar ángulo y longitud en pantalla
  font = pygame.font.SysFont("Arial", 24, True, False)
  surface = font.render(text, True, (0,0,0))
  screen.blit(surface, position)


pendulo = Ball([0,1])
out = False
startTimer = timer()


while not out:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      out = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      xy = pygame.mouse.get_pos()
      length = lengthF()
      theta0 = theta0F(xy[1])
  t = timer() - startTimer
  theta = thetaF(t)
  xy = get_position()
  screen.fill((255,255,255))
  info("Angle (º): " + str(round((theta*180/math.pi), 1)), (25,25))
  info("Length (m): " + str(round(length/1000, 2)), (25,55))
  info("Time (s): " + str(round(t, 1)), (25,85))
  update()
  move()