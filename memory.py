import pygame, math
from timeit import default_timer as timer

width = 800
height = 400
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

b = 0.07
m = 0.3

length = 1
theta0 = 0
theta = 0
t = 0
axis = (width/2, 0)
xy = [1, 1]

class Ball(object):
	def __init__(self, xy):
		self.x = xy[0]
		self.y = xy[1]
	def draw(self):
		pygame.draw.lines(screen, (50,50,50), False, (axis, (self.x, self.y)))
		pygame.draw.circle(screen, (100, 100, 100), (self.x, self.y), 17)


def lengthF():
	lengthFV = math.sqrt(math.pow(xy[0]-axis[0], 2) + math.pow(xy[1]-axis[1], 2))
	return(lengthFV)

def theta0F():
	theta0FV = math.acos((xy[1]-axis[1]) / length)
	return(theta0FV)

def thetaF():
	thetaFV = theta0 * math.pow(math.e, (-b/(2*m))*t) * math.cos((math.sqrt(math.pow(9.8/(length/150), 2)-math.pow(b/(2*m), 2))) * t + theta0)
	#thetaFV = theta0 * math.sin(math.sqrt(9.8/(length/1000)) * t + theta0) # 150px = 1m
	return(thetaFV)

def getPosition():
	pendulum.x = length * math.sin(theta) + axis[0]
	pendulum.y = length * math.cos(theta) + axis[1]

def update():
	pendulum.draw()
	pygame.display.update()

def getInfo(text, position):
	font = pygame.font.SysFont("Arial", 16, True, False)
	surface = font.render(text, True, (0,0,0))
	screen.blit(surface, position)


pendulum = Ball([1, 1])
out = False
resetTimer = 0
startTimer = timer()

while not out:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			out = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			xy = pygame.mouse.get_pos()
			length = lengthF()
			theta0 = theta0F()
			resetTimer += t
	t = timer() - startTimer - resetTimer
	theta = thetaF()
	getPosition()
	screen.fill((255, 255, 255))
	getInfo(f"t(s) = {round(t, 2)}", (10, 10))
	getInfo(f"theta(º) = {round(theta*180/math.pi, 2)}", (10, 30))
	getInfo(f"length(m) = {round(length/150, 2)}", (10, 50))
	getInfo(f"m(kg) = {m}", (10, 70))
	getInfo(f"b = {b}", (10, 90))
	update()