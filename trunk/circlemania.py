import pygame
import pygame.gfxdraw
import math
import random

WIDTH=800
HEIGHT=500


# Base class for graphical objects that are shaped like circles
class Circle:
    def __init__(self,rect,color):
        self.x,self.y,self.width,self.height=rect
        self.color=color
    def Draw(self,surface):
        pygame.gfxdraw.filled_circle(surface,self.x+self.width/2,self.y+self.height/2,self.GetRadius(),\
        (self.color.r,self.color.g,self.color.b))
    def GetCenter(self):
        return (self.x+self.width/2.0,self.y+self.height/2.0)
    def GetRadius(self):
        return (self.width+self.height)/4.0
    # The overloaded & operator is used to check collision
    def __and__(self,other):
        x1,y1=self.GetCenter()
        x2,y2=other.GetCenter()
        r1,r2=self.GetRadius(),other.GetRadius()
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)<=(r1+r2)
    def Explode(self,pieces):
        particles=[]
        for i in range(pieces):
            inst=Particle((self.x+self.width/2.0,self.y+self.height/2.0,2,2),(math.cos(i/10.0)*3,math.sin(i/10.0)*3),self.color)
            particles.append(inst)
        return particles



# Small circle that moves. Fast.
class Particle (Circle):
    def __init__(self,rect,direction,color):
        Circle.__init__(self,rect,color)
        self.xdir,self.ydir=direction
    def Move(self):
        self.x+=self.xdir
        self.y+=self.ydir

class Shot(Circle):
    pass

class Enemy(Circle):
    pass

class Player(Circle):
    pass

class Game:
    pass

class Interface:
    pass




pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))

c1=Circle((WIDTH/2,HEIGHT/2,10,10),pygame.Color((0x00ff00)))




clock=pygame.time.Clock()

running=True
while running:
    for event in pygame.event.get():
        #print event
        if event.type==pygame.QUIT:
            running=False
    screen.fill(0)
    c1.Draw(screen)


    pygame.display.flip()
    clock.tick(25)


pygame.quit()




