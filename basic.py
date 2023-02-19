import pygame
import random
import math

pygame.init()
pygame.display.set_caption("Dinosaur game by Vinh")
dinocolour = (0,0,0)
DINOHEIGHT = 40
DINOWIDTH = 20

class Dinosaur:
    def __init__(self, surfaceHeight):
        self.x = 60
        self.y = 0
        self.yvelocity = 0
        self.height = DINOHEIGHT
        self.width = DINOWIDTH
        self.surfaceHeight = surfaceHeight
    def jump(self): 
        if(self.y == 0):
            self.yvelocity = 300
    def update(self, deltaTime):
        self.yvelocity += -800*deltaTime 
        self.y += self.yvelocity * deltaTime
        if self.y < 0: 
            self.y = 0
            self.yvelocity = 0
    def draw(self,display):
        pygame.draw.rect(display,dinocolour,[self.x,self.surfaceHeight-self.y-self.height,self.width,self.height])
    

colour = (0,0,0)
class Obstacle:
    def __init__(self, x, size, GroundHeight):
        self.x = x
        self.size = size
        self.GroundHeight = GroundHeight

    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, colour, [self.x, self.GroundHeight-self.size, self.size, self.size])
    
    def update(self, deltaTime, velocity):
        self.x -= velocity*deltaTime

    def checkOver(self):
        if self.x < 0 :
            return True
        else:
            return False
    
    def checkCollision(self):
        if abs(dinosaur.x-self.x)<=10 and dinosaur.y<=20:
            return True
        else:
            return False
        
        
width= 640
height=480
size=(width,height)
gameDisplay= pygame.display.set_mode(size) #creates screen
xPos = 0
yPos = 0
blue = (255, 255, 255 )
GROUND_HEIGHT = height-100 

dinosaur = Dinosaur(GROUND_HEIGHT)

lastFrame = pygame.time.get_ticks() #get ticks returns current time in milliseconds

MINGAP = 200
VELOCITY = 300
MAXGAP = 600
obstacles = []
num_of_obstacles = 4
lastObstacle = width
obstaclesize = 20


for i in range(4):
    lastObstacle += MINGAP+(MAXGAP-MINGAP)*random.random() #Make distance between rocks random
    obstacles.append(Obstacle(lastObstacle, obstaclesize, GROUND_HEIGHT))
def close():
    pygame.quit()
    import menu

white = (0,0,0)
gameplay=True
score = 0
font = pygame.font.SysFont('Arial', 24)
while gameplay:
    t = pygame.time.get_ticks() 
    deltaTime = (t-lastFrame)/1000.0 
    lastFrame = t 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameplay=False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: 
                dinosaur.jump() 
    score += 2 
    finalscore = math.floor(score/10000)
    gameDisplay.fill(blue)
    dinosaur.update(deltaTime)
    dinosaur.draw(gameDisplay)

    for obs in obstacles:
        obs.update(deltaTime, VELOCITY)
        obs.draw(gameDisplay)
        if(obs.checkOver()):
            lastObstacle += MINGAP+(MAXGAP-MINGAP)*random.random()
            obs.x = lastObstacle
        if(obs.checkCollision()):
            close()

    lastObstacle -= VELOCITY*deltaTime
    score_txt = "score: {}".format(finalscore)
    text_surface = font.render(score_txt, True, (0,0,0))
    gameDisplay.blit(text_surface, (300, 100))


    pygame.draw.rect(gameDisplay,white, [0,GROUND_HEIGHT, width, height-GROUND_HEIGHT])
    pygame.draw.rect(gameDisplay, white, [xPos,yPos,40,50])
    xPos += 1 
    yPos += 1 
    pygame.display.update() 

pygame.quit()