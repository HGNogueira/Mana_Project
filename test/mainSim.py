import pygame, gSim, sys
from pygame.locals import *

""" Main script with all the drawing methods and main loop"""

G = 6.67*10**-11

def draw_next_with_steps(bodies, step,screen):
    gSim.next_pos_with_steps(bodies, step)
    for body in bodies:
        pygame.draw.circle(screen,body.color,[int(body.position[0]),int(body.position[1])],body.radius)
        

def draw_centerOfMass(bodies, screen):
    posCM = gSim.get_centerOfMass(bodies)
    pygame.draw.circle(screen,(255,255,255),(int(posCM[0]),int(posCM[1])),1)

def print_totalEnergy(bodies,screen, f, iteration):
    kinetic = 0
    potential = 0

    for body in bodies:#calc kinetic energy
        kinetic+=body.mass*1./2.*float(body.mass)*(body.speed[0]**2+body.speed[1]**2+body.speed[2]**2)
    print "Kinetic = " + str(kinetic)
    
    for i in range(len(bodies)):
        for it in range(len(bodies)):
            if i == it: continue
            r = gSim.get_distance(bodies[i], bodies[it])
            potential-=G*bodies[i].mass*bodies[it].mass/r

    print "Potential = " + str(potential)
    totalEnergy =potential + kinetic
    print "Total = " + str(totalEnergy)      
    f.write(str(iteration) + " " + str(kinetic) + " " + str(potential) + " " + str(totalEnergy) + "\n")

def new_body_click(bodies):
    mouseDown = pygame.mouse.get_pos()
    mouseUp = []
    wait = True
    while wait:
        for event in pygame.event.get(): 
            if event.type == MOUSEBUTTONUP:
                mouseUp = pygame.mouse.get_pos()
                wait = False
                break
                
    newSpeed = [0,0]
    newSpeed[0] = float(10*(mouseUp[0]-mouseDown[0]))
    newSpeed[1] = float(10*(mouseUp[1]-mouseDown[1]))
    print newSpeed
    
    newbody = gSim.body(6*10**2,1,(0,255,0),[mouseDown[0],mouseDown[1],0.],[newSpeed[0],newSpeed[1],0.])
    bodies.append(newbody)


def main():
    pygame.init()
    f = open("data.txt", "w")
    f.write("#iteration || Kinetic || Potential || Mechanical \n")
    iteration = 0
    RATIO = 9./12.
    WIDTH = 700
    HEIGHT = int(WIDTH*RATIO)
    FPS = 60
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    CLOCK = pygame.time.Clock()

    body0 = gSim.body(6*10**16,10,(255,0,0),[380.,200.,0.],[0.,000.,0.])
    body1 = gSim.body(6*10**4,1,(255,123,187),[400.,200.,0.],[0.,3000.,0.])

    bodies =[body0, body1]
    while True:
        for event in pygame.event.get():
            #print str(event)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                new_body_click(bodies)

        draw_next_with_steps(bodies, 0.0001, screen)
        draw_centerOfMass(bodies,screen)
        print_totalEnergy(bodies,screen, f, iteration)

        pygame.display.flip()
        CLOCK.tick(30)
        iteration +=1
main()
