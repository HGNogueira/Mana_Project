import sys, pygame, random, body
from pygame.locals import *


def draw_next(objects, screen):
    idx = 0
    for object in objects:
        object.position = body.next_pos(object)
        pygame.draw.circle(screen,object.color,[int(object.position[0]),int(object.position[1])],object.radius)
        
        object.speed = body.eval_nextVel(objects, idx)
        idx += 1

def draw_centerOfMass(objects, screen):
    idx = 0 
    posCM = [0,0,0]
    mTotal = 0
    for object in objects:
        posCM[0]+=object.position[0]*object.mass
        posCM[1]+=object.position[1]*object.mass
        posCM[2]+=object.position[2]*object.mass
        mTotal+=object.mass
    


    posCM[0]=posCM[0]/mTotal
    posCM[1]=posCM[1]/mTotal
    
    #print posCM
    
    pygame.draw.circle(screen, (0,0,0), [int(posCM[0]), int(posCM[1])], 1)

def totalEnergy(objects):
    G=1
    total_energy = 0
    kinetic = 0

    for body in objects:
        kinetic+= 1./2.*float(body.mass)*(body.speed[0]**2+body.speed[1]**2+body.speed[2]**2)

    
    potential = 0
    for idx in range(len(objects)):
        for i in range(len(objects)):
            if(i  == idx): continue
            r=((objects[idx].position[0] - objects[i].position[0])**2 + (objects[idx].position[1] - objects[i].position[1])**2 + (objects[idx].position[2] - objects[i].position[2])**2)**(1./2.)
            if r!= 0:
                potential-=objects[i].mass*objects[idx].mass*G/r
    

    print "Kinetic = " + str(10000*kinetic)
    print "Potential= " + str(10000*potential)
    print "Total Energie = " + str(10000*kinetic+10000*potential)

def main():
    pygame.init()

    RATIO = 9./12.
    WIDTH = 700
    HEIGHT = int(WIDTH*RATIO)
    FPS = 60
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    CLOCK = pygame.time.Clock()

    body0 = body.object(1000,7,(255,0,0),[400,200,0],[0,-100,0])
    body1 = body.object(1000,7,(0,255,0),[200,200,0],[0,100,0])
    body2 = body.object(0.01,7,(0,0,255),[300,200,0],[0,0,0])

    bodies =[body1, body2, body0]
    while True:
        for event in pygame.event.get():
            #print str(event)
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255,255,255))
        draw_next(bodies, screen)
        draw_centerOfMass(bodies,screen)
        totalEnergy(bodies)
        
        pygame.display.flip()
        CLOCK.tick(60)

main()
