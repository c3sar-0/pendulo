import pygame, math
from timeit import default_timer as timer

width = 800
height = 400

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

axis = (400, 0)
xy = (0,0)
t = 0
v = 0
a = 0
theta0 = 0
theta = 0
length = 1


class Ball(object):
  def __init__(self, xy):
    self.x = xy[0]
    self.y = xy[1]
  
  def draw(self):
    pygame.draw.lines(screen, (50,50,50), False, (axis, (self.x, self.y)))
    pygame.draw.circle(screen, (100, 100, 100), (self.x, self.y), 5)


def lengthF():
  lengthFV = math.sqrt(math.pow(xy[0]-axis[0],2) + math.pow(xy[1]-axis[1],2))
  return(lengthFV)

def thetaF(t):
  thetaFV = (theta0 * math.sin(math.sqrt(length/9.8) * t + theta0)) # w = (sqrt(g/l)) ?
  return(thetaFV)

def theta0F(y): #cos0 = y/length
  theta0FV = math.acos((y-axis[1])/length)
  return(theta0FV)

def update():
  screen.fill((255,255,255))
  pendulo.draw()
  pygame.display.update()

def move():
  pendulo.x = xy[0]
  pendulo.y = xy[1]

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
  update()
  move()
  print(theta0) ## THETA0 ES MUY PEQUEÑO ##
  print(theta)
  #print(math.acos((xy[1]-axis[1])/length))