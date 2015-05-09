import pygame, gSim, sys

from pygame.locals import *
import time
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin
import random


""" Main script with all the drawing methods and main loop"""

G = 0.49

RATIO = 9./12.
WIDTH = 1100
HEIGHT = int(WIDTH*RATIO)

def matrix_vec_mult(matrix, vec):
    new_vec = []
    new_value = 0
    for line in matrix:
        it = 0
        for column in line:
            new_value += column* vec[it]
            it +=1
        new_vec.append(new_value)
        new_value = 0
    return new_vec

def draw_x_axis(theta, screen):
    start_axis = [-500, 0 , 0]
    end_axis = [500, 0, 0]
    x_rot_matrix=[ [1, 0, 0],
                   [0, cos(-theta[0]), sin(-theta[0])],
                   [0, sin(-theta[0]), cos(-theta[0])]]

    y_rot_matrix=[ [cos(-theta[1]), 0, sin(-theta[1])],
                   [0, 1, 0],
                   [-sin(-theta[1]), 0, cos(-theta[1])]]

    z_rot_matrix=[ [cos(-theta[2]), -sin(-theta[2]), 0],
                   [sin(-theta[2]), cos(-theta[2]), 0],
                   [0, 0, 1]]

    start_axis = matrix_vec_mult(z_rot_matrix, start_axis)
    start_axis = matrix_vec_mult(y_rot_matrix, start_axis)
    start_axis = matrix_vec_mult(x_rot_matrix, start_axis)
    
    end_axis = matrix_vec_mult(z_rot_matrix, end_axis)
    end_axis = matrix_vec_mult(y_rot_matrix, end_axis)
    end_axis = matrix_vec_mult(x_rot_matrix, end_axis)

    pygame.draw.line(screen, (255,0,0), [int(start_axis[0] + WIDTH/2), int(start_axis[1] + HEIGHT/2)] ,[int(end_axis[0] + WIDTH/2), int(end_axis[1] + HEIGHT/2)], 1)

def draw_y_axis(theta, screen):
    start_axis = [0 , -500 , 0]
    end_axis = [0, 500, 0]
    x_rot_matrix=[ [1, 0, 0],
                   [0, cos(-theta[0]), sin(-theta[0])],
                   [0, sin(-theta[0]), cos(-theta[0])]]

    y_rot_matrix=[ [cos(-theta[1]), 0, sin(-theta[1])],
                   [0, 1, 0],
                   [-sin(-theta[1]), 0, cos(-theta[1])]]

    z_rot_matrix=[ [cos(-theta[2]), -sin(-theta[2]), 0],
                   [sin(-theta[2]), cos(-theta[2]), 0],
                   [0, 0, 1]]

    start_axis = matrix_vec_mult(z_rot_matrix, start_axis)
    start_axis = matrix_vec_mult(y_rot_matrix, start_axis)
    start_axis = matrix_vec_mult(x_rot_matrix, start_axis)
    
    end_axis = matrix_vec_mult(z_rot_matrix, end_axis)
    end_axis = matrix_vec_mult(y_rot_matrix, end_axis)
    end_axis = matrix_vec_mult(x_rot_matrix, end_axis)

    pygame.draw.line(screen, (0,255,0), [int(start_axis[0] + WIDTH/2), int(start_axis[1] + HEIGHT/2)] ,[int(end_axis[0] + WIDTH/2), int(end_axis[1] + HEIGHT/2)], 1)

def draw_z_axis(theta, screen):
    start_axis = [0, 0 , -500]
    end_axis = [0, 0, 500]
    x_rot_matrix=[ [1, 0, 0],
                   [0, cos(-theta[0]), sin(-theta[0])],
                   [0, sin(-theta[0]), cos(-theta[0])]]

    y_rot_matrix=[ [cos(-theta[1]), 0, sin(-theta[1])],
                   [0, 1, 0],
                   [-sin(-theta[1]), 0, cos(-theta[1])]]

    z_rot_matrix=[ [cos(-theta[2]), -sin(-theta[2]), 0],
                   [sin(-theta[2]), cos(-theta[2]), 0],
                   [0, 0, 1]]

    start_axis = matrix_vec_mult(z_rot_matrix, start_axis)
    start_axis = matrix_vec_mult(y_rot_matrix, start_axis)
    start_axis = matrix_vec_mult(x_rot_matrix, start_axis)
    
    end_axis = matrix_vec_mult(z_rot_matrix, end_axis)
    end_axis = matrix_vec_mult(y_rot_matrix, end_axis)
    end_axis = matrix_vec_mult(x_rot_matrix, end_axis)

    pygame.draw.line(screen, (0,0,255), [int(start_axis[0] + WIDTH/2), int(start_axis[1] + HEIGHT/2)] ,[int(end_axis[0] + WIDTH/2), int(end_axis[1] + HEIGHT/2)], 1)

def draw_axis(theta, screen):
    draw_x_axis(theta, screen)
    draw_z_axis(theta, screen)
    draw_y_axis(theta, screen)

def draw_next_with_steps(bodies, step,screen, theta):
    gSim.next_pos_with_steps(bodies, step)
    x_rot_matrix=[ [1, 0, 0],
                   [0, cos(-theta[0]), sin(-theta[0])],
                   [0, sin(-theta[0]), cos(-theta[0])]]
    
    y_rot_matrix=[ [cos(-theta[1]), 0, sin(-theta[1])],
                   [0, 1, 0],
                   [-sin(-theta[1]), 0, cos(-theta[1])]]


    z_rot_matrix=[ [cos(-theta[2]), -sin(-theta[2]), 0],
                   [sin(-theta[2]), cos(-theta[2]), 0],
                   [0, 0, 1]]


    for body in bodies:
        draw_pos = matrix_vec_mult(z_rot_matrix, body.position)
        draw_pos = matrix_vec_mult(y_rot_matrix, draw_pos)
        draw_pos = matrix_vec_mult(x_rot_matrix, draw_pos)
        pygame.draw.circle(screen,body.color,[int(draw_pos[0] + WIDTH/2),int(draw_pos[1] + HEIGHT/2)],body.radius)
        
def draw_centerOfMass(bodies, screen):
    if len(bodies) > 0:
        posCM = gSim.get_centerOfMass(bodies)
        pygame.draw.circle(screen,(255,255,255),(int(posCM[0] + WIDTH/2),int(posCM[1] + HEIGHT/2)),1)

def draw_current(bodies, screen):
    if len(bodies) > 0:
        for body in bodies:
            pygame.draw.circle(screen,body.color,[int(body.position[0] + WIDTH/2),int(body.position[1] + HEIGHT/2)],body.radius)

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



def reset_bodies():
    body0 = gSim.body(5*10**9,5,(255,0,0),[0, 0, 0],[0.,0.,0.])
    body1 = gSim.body(10**4,5,(255,123,187),[-50,0,0.],[0.,-6000.,0.])
    body2 = gSim.body(10**10, 5, (203,180,240),[100.,200.,0.],[0.,3000.,0.])
    bodies =[body0, body1]
    return bodies

def main():
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 15)

    f = open("data.txt", "w")
    f.write("#iteration || Kinetic || Potential || Mechanical \n")
    iteration = 0
    
    
    FPS = 60
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    CLOCK = pygame.time.Clock()
    REALTIMEGRAPH = False
    Trail = False
    theta = [0, 0, 0]
    
    down = False
    up = False
    right = False
    left = False

    plt.axis([0,1000,0,0.5*10**10])
    plt.ylabel('Energies')
    plt.xlabel("Iterations from start")
    plt.ion()
    plt.show
    
    bodies = reset_bodies()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    down = not down
                if event.key == pygame.K_UP:
                    up = not up
                if event.key == pygame.K_RIGHT:
                    right = not right
                if event.key == pygame.K_LEFT:
                    left = not left

            if event.type == pygame.KEYDOWN:       
                if event.key == pygame.K_f:
                    Trail = not Trail
                if event.key == pygame.K_e:
                    if len(bodies) > 0:
                        del bodies[len(bodies)-1]
            if event.type == pygame.QUIT:
                return 0
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] < 80 and pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[1] < 30 and pygame.mouse.get_pos()[1] > 10:
                    bodies = reset_bodies()
                    theta = [45,0 , 45]
                    break
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
                newbody = gSim.body(6*10**8,5,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),[mouseDown[0] - WIDTH/2,mouseDown[1] - HEIGHT/2,0.],[newSpeed[0],newSpeed[1],0.])
                bodies.append(newbody)
                
        if not Trail:
            screen.fill((0,0,0)) 
        if up:
            theta[0] -= 0.01
        if down:
            theta[0] += 0.01
        if right:
            theta[2] -= 0.01
        if left:
            theta[2] += 0.01    

        ##### GUI#####
        pygame.draw.rect(screen, [120, 120, 120], [10, 10, 70, 20])
        label = myfont.render("Restart", 1, (255,255,255))
        if pygame.mouse.get_pos()[0] < 80 and pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[1] < 30 and pygame.mouse.get_pos()[1] > 10:# if mouseover rectangle
            pygame.draw.rect(screen, [200, 120, 120], [10, 10, 70, 20])
        screen.blit(label, (12, 12))
        pygame.draw.line(screen, (255,0,0), [10,50], [50,50], 1)
        xaxis = myfont.render("x axis", 1, (255, 0, 0))
        pygame.draw.line(screen, (0,255,0), [10,60], [50,60], 1)
        yaxis = myfont.render("y axis", 1, (0, 255, 0))
        pygame.draw.line(screen, (0,0,255), [10,70], [50,70], 1)
        zaxis = myfont.render("z axis", 1, (0, 0, 255))
        screen.blit(xaxis, (60, 35))                      
        screen.blit(yaxis, (60, 50))
        screen.blit(zaxis, (60, 65))
        ##### GUI#####



        draw_axis(theta, screen)
        draw_next_with_steps(bodies, 0.0001, screen, theta)
        #draw_centerOfMass(bodies,screen)
        #draw_totalEnergy(bodies,screen, f, iteration)
        pygame.display.flip()
        CLOCK.tick(60)
        iteration +=1
main()
