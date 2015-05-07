import pygame, gSim, sys
from pygame.locals import *
import time
import numpy as np
import matplotlib.pyplot as plt
import math
import random


""" Main script with all the drawing methods and main loop"""

G = 0.49

def draw_next_with_steps(bodies, step,screen):
    gSim.next_pos_with_steps(bodies, step)
    for body in bodies:
        pygame.draw.circle(screen,body.color,[int(body.position[0]),int(body.position[1])],body.radius)
        

def draw_centerOfMass(bodies, screen):
    if len(bodies) > 0:
        posCM = gSim.get_centerOfMass(bodies)
        pygame.draw.circle(screen,(255,255,255),(int(posCM[0]),int(posCM[1])),1)

def draw_current(bodies, screen):
    if len(bodies) > 0:
        for body in bodies:
            pygame.draw.circle(screen,body.color,[int(body.position[0]),int(body.position[1])],body.radius)


def draw_totalEnergy(bodies,screen, f, iteration):
    if len(bodies)>0:
        kinetic = 0
        potential = 0
        for body in bodies:#calc kinetic energy
            kinetic+=body.mass*1./2.*(body.speed[0]**2+body.speed[1]**2+body.speed[2]**2)
        print "Kinetic = " + str(kinetic)
        
        for i in range(len(bodies)):
            for it in range(len(bodies)):
                if i == it: continue
                r = gSim.get_distance(bodies[i], bodies[it])
                potential-=0.49*G*bodies[i].mass*bodies[it].mass/r

        print "Potential = " + str(potential)
        totalEnergy =potential + kinetic
        print "Total = " + str(totalEnergy)      
        f.write(str(iteration) + " " + str(kinetic) + " " + str(potential) + " " + str(totalEnergy) + "\n")
        
        plt.scatter(iteration, abs(totalEnergy))
        plt.draw()

def main():
    pygame.init()
    f = open("data.txt", "w")
    f.write("#iteration || Kinetic || Potential || Mechanical \n")
    iteration = 0
    RATIO = 9./12.
    WIDTH = 1100
    HEIGHT = int(WIDTH*RATIO)
    FPS = 60
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    CLOCK = pygame.time.Clock()
    REALTIMEGRAPH = False
    Trail = False

    plt.axis([0,1000,0,0.5*10**10])
    plt.ylabel('Energies')
    plt.xlabel("Iterations from start")
    plt.ion()
    plt.show
    
    # na ordem dos 10**10 para sentir aquela atraction
    body0 = gSim.body(5*10**8,5,(255,0,0),[WIDTH/2,HEIGHT/2,0.],[0.,0.,0.])
    #body1 = gSim.body(10**10,5,(255,123,187),[500.,199.,0.],[0.,-3000.,0.])
    #body2 = gSim.body(10**10, 5, (203,180,240),[100.,200.,0.],[0.,3000.,0.])
        

    bodies =[body0]

    while True:
        for event in pygame.event.get():
            #print str(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    Trail = not Trail
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        del bodies[len(bodies)-1]
            if event.type == pygame.QUIT:
                return 0
            if event.type == MOUSEBUTTONDOWN:
                mouseDown = pygame.mouse.get_pos()
                mouseUp = []
                wait = True
                while wait:
                    screen.fill((0,0,0)) 
                    pygame.draw.line(screen, (100,100,100), mouseDown, pygame.mouse.get_pos(), 1)
                    draw_current(bodies, screen)
                    draw_centerOfMass(bodies,screen)
                    pygame.display.flip()
                    for event in pygame.event.get(): 
                        if event.type == MOUSEBUTTONUP:
                            mouseUp = pygame.mouse.get_pos()
                            wait = False
                            break
                
                newSpeed = [0,0]
                newSpeed[0] = float(100*(mouseUp[0]-mouseDown[0]))
                newSpeed[1] = float(100*(mouseUp[1]-mouseDown[1]))
    
                newbody = gSim.body(6*10**8,5,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),[mouseDown[0],mouseDown[1],0.],[newSpeed[0],newSpeed[1],0.])
                bodies.append(newbody)
                
        if not Trail:
            screen.fill((0,0,0)) 

        draw_next_with_steps(bodies, 0.0001, screen)
        draw_centerOfMass(bodies,screen)
        #draw_totalEnergy(bodies,screen, f, iteration)
        pygame.display.flip()
        CLOCK.tick(60)
        iteration +=1
main()
