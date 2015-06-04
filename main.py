import pygame
import gSim
import sys
import pyglet


from pygame.locals import *
import time
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, sqrt
import random


""" Main script with all the drawing methods and main loop"""

G = 0.49
#G = 1
#G=6.6738*10**(-11)

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
    x_rot_matrix=[ [1, 0, 0],
                   [0, cos(-theta[0]), sin(-theta[0])],
                   [0, sin(-theta[0]), cos(-theta[0])]]
    
    y_rot_matrix=[ [cos(-theta[1]), 0, sin(-theta[1])],
                   [0, 1, 0],
                   [-sin(-theta[1]), 0, cos(-theta[1])]]


    z_rot_matrix=[ [cos(-theta[2]), -sin(-theta[2]), 0],
                   [sin(-theta[2]), cos(-theta[2]), 0],
                   [0, 0, 1]]
    if len(bodies) == 3:
        gSim.RK4(bodies,step)
    else:
        gSim.next_pos_with_steps(bodies,step)

    for body in bodies:
        draw_pos = matrix_vec_mult(z_rot_matrix, body.position)
        draw_pos = matrix_vec_mult(y_rot_matrix, draw_pos)
        draw_pos = matrix_vec_mult(x_rot_matrix, draw_pos)
        pygame.draw.circle(screen,body.color,[int(draw_pos[0] + WIDTH/2),int(draw_pos[1] + HEIGHT/2)],1)

def draw_next_restricted(bodies,step,screen,theta):
    x_rot_matrix=[ [1, 0, 0],
                   [0, cos(-theta[0]), sin(-theta[0])],
                   [0, sin(-theta[0]), cos(-theta[0])]]
    
    y_rot_matrix=[ [cos(-theta[1]), 0, sin(-theta[1])],
                   [0, 1, 0],
                   [-sin(-theta[1]), 0, cos(-theta[1])]]


    z_rot_matrix=[ [cos(-theta[2]), -sin(-theta[2]), 0],
                   [sin(-theta[2]), cos(-theta[2]), 0],
                   [0, 0, 1]]

    gSim.nextpos_restricted(bodies,step)
    for body in bodies:
        draw_pos = matrix_vec_mult(z_rot_matrix, body.position)
        draw_pos = matrix_vec_mult(y_rot_matrix, draw_pos)
        draw_pos = matrix_vec_mult(x_rot_matrix, draw_pos)
        pygame.draw.polygon(screen,body.color,[[int(draw_pos[0])-5+WIDTH/2,int(draw_pos[1])+HEIGHT/2],[int(draw_pos[0])+5+WIDTH/2,int(draw_pos[1])+HEIGHT/2],[int(draw_pos[0])+WIDTH/2,int(draw_pos[1])+5+HEIGHT/2]])
        
def draw_centerOfMass(bodies, screen, theta):
    x_rot_matrix=[ [1, 0, 0],
                   [0, cos(-theta[0]), sin(-theta[0])],
                   [0, sin(-theta[0]), cos(-theta[0])]]
    
    y_rot_matrix=[ [cos(-theta[1]), 0, sin(-theta[1])],
                   [0, 1, 0],
                   [-sin(-theta[1]), 0, cos(-theta[1])]]


    z_rot_matrix=[ [cos(-theta[2]), -sin(-theta[2]), 0],
                   [sin(-theta[2]), cos(-theta[2]), 0],
                   [0, 0, 1]]

    if len(bodies) == 3:
        posCM = gSim.get_centerOfMass((bodies[0],bodies[1],bodies[2]))
        posCM = matrix_vec_mult(z_rot_matrix, posCM)
        posCM = matrix_vec_mult(y_rot_matrix, posCM)
        posCM = matrix_vec_mult(x_rot_matrix, posCM)

        
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

        #print "Potential = " + str(potential)
        totalEnergy =potential + kinetic
        print "Total = " + str(totalEnergy)      
        f.write(str(iteration) + " " + str(kinetic) + " " + str(potential) + " " + str(totalEnergy) + "\n")
        
        plt.scatter(iteration, abs(totalEnergy))
        plt.draw()

def double_draw_totalEnergy(bodies,bodies2,screen, f, iteration):
    if len(bodies)>0:
        kinetic = 0
        potential = 0
        for body in bodies:#calc kinetic energy
            kinetic+=body.mass*1./2.*(body.speed[0]**2+body.speed[1]**2+body.speed[2]**2)
        #print "Kinetic = " + str(kinetic)
        
        for i in range(len(bodies)):
            for it in range(len(bodies)):
                if i == it: continue #passa a frente para a prox it
                r = gSim.get_distance(bodies[i], bodies[it])
                potential-=G*bodies[i].mass*bodies[it].mass/r

        #print "Potential = " + str(potential)
        totalEnergy =potential + kinetic
        #print "Total = " + str(totalEnergy)      
        #f.write(str(iteration) + " " + str(kinetic) + " " + str(potential) + " " + str(totalEnergy) + "\n")
        
        plt.scatter(iteration, abs(totalEnergy))
        #plt.scatter(iteration, abs(potential))

    if len(bodies2)>0:
        kinetic = 0
        potential = 0
        for body in bodies2:#calc kinetic energy
            kinetic+=body.mass*1./2.*(body.speed[0]**2+body.speed[1]**2+body.speed[2]**2)
        #print "Kinetic = " + str(kinetic)
        
        for i in range(len(bodies2)):
            for it in range(len(bodies2)):
                if i == it: continue #passa a frente para a prox it
                r = gSim.get_distance(bodies2[i], bodies2[it])
                potential-=G*bodies2[i].mass*bodies2[it].mass/r

        #print "Potential = " + str(potential)
        totalEnergy =potential + kinetic
        #print "Total = " + str(totalEnergy)      
        #f.write(str(iteration) + " " + str(kinetic) + " " + str(potential) + " " + str(totalEnergy) + "\n")
        
        plt.scatter(iteration, abs(totalEnergy), color = 'red')
        #plt.scatter(iteration, abs(potential),color = 'red')

        plt.draw()

#funcao apenas para 3 corpos
def draw_momentum(bodies,screen, f, iteration):
    Lx = [0,0,0]
    Ly = [0,0,0]
    Lz = [0,0,0]
    L = 0

    CM = gSim.get_centerOfMass(bodies)

    i=0
    for body in bodies:
        Lx[i] = (body.position[1]-CM[1])*body.speed[2] - (body.position[2]-CM[2])*body.speed[1]
        Ly[i] = (body.position[2]-CM[2])*body.speed[0] - (body.position[0]-CM[0])*body.speed[2]
        Lz[i] = (body.position[0]-CM[0])*body.speed[1] - (body.position[1]-CM[1])*body.speed[0]
        mod = (Lx[i]**2 + Ly[i]**2 + Lz[i]**2)**0.5*bodies[i].mass
        L += mod
        i+=1

    plt.scatter(iteration, L,color = 'blue')

    plt.draw()

def reset_bodies(indice = 0):

    ##Comparacao com a aproximacao dos restricted	
    #body0 = gSim.body(10**10,5,(255,0,0),[250,0, 0],[0.,-2236.594,0.])
    #body1 = gSim.body(10**10,5,(255,123,187),[-250,0,0.],[0.,2236.594,0.])
    #body2 = gSim.body(5*10**7, 5, (203,180,240),[100.,0.,0.],[0.,3459.,0.])

    ##Ponto de Lagrange

    if indice == 0:
	M=10**10#massa corpo grande
    	m=10**7#massa corpo que orbita o grande (corpo m)
    	mm=0.0005#massa do corpo no ponto de lagrange
    	R=260#distancia do corpo m ao grande
    	v=sqrt(G*(M+m)/R)#velocidade do corpo m
    	ratio=0.9323089895#fracao de R em que se encontra o ponto de lagrange
    	RR=ratio*R #ponto de lagrange
    	vv=RR/R*v #vel do ponto de lagrange 

        body0 = gSim.body(M,5,(255,0,0),[0,0, 0],[0.,0.,0.])
        body1 = gSim.body(m,5,(255,123,187),[R,0,0.],[0.,v,0.])
        body2 = gSim.body(mm, 5, (203,180,240),[RR,0.,0.],[0.,vv,0.])


    elif indice == 1:
	M=10**10#massa corpo grande
    	m=10**7#massa corpo que orbita o grande (corpo m)
    	mm=0.5#massa do corpo no ponto de lagrange
    	R=260#distancia do corpo m ao grande
    	v=sqrt(G*(M+m)/R)#velocidade do corpo m

	body0 = gSim.body(M,5,(255,0,0),[0,0, 0],[0.,0.,0.])
        body1 = gSim.body(m,5,(255,123,187),[R,0,0.],[0.,v,0.])
        body2 = gSim.body(mm, 5, (203,180,240),[R/2,-3**0.5/2*R,0.],[v*3**0.5/2,v/2,0.])

    ##Triangulo equilatero - Pila murcha
    elif indice == 2:
        body0 = gSim.body(8*10**9,5,(255,0,0),[-290,-502.2947/2+100, 0],[1000.,-1732.05808,0.])
        body1 = gSim.body(8*10**9,5,(255,123,187),[290,-502.2947/2+100,0.],[1000.,1732.050808,0.])
        body2 = gSim.body(8*10**9, 5, (203,180,240),[0.,502.2947/2+100,0.],[-2000.,0.,0.])

    ##Triangulo equilatero - Pila hirta!
    elif indice == 3:
        body0 = gSim.body(10**10,5,(255,0,0),[-150,0, 0],[2015.5,-3490.948,0.])
        body1 = gSim.body(10**10,5,(255,123,187),[150,0,0.],[2015.5,3490.948,0.])
        body2 = gSim.body(10**10, 5, (203,180,240),[0.,259.808,0.],[-4031.,0.,0.])

    ##Such 8!!!!!!!!!!!!!!!!
    elif indice == 4:
        body0 = gSim.body(2.05*10**6,5,(255,0,0),[0.97000436*100,-0.24308753*100, 0],[0.5*0.93240737*100,0.5*0.86473146*100,0.])
        body1 = gSim.body(2.05*10**6,5,(255,123,187),[-0.97000436*100,0.24308753*100,0.],[0.5*0.93240737*100,0.5*0.86473146*100,0.])
        body2 = gSim.body(2.05*10**6, 5, (203,180,240),[0.,0.,0.],[-0.93240737*100,-0.86473146*100,0.])


    ##Such triangulo equilatero eliptico - Pila hirta!	    
    elif indice == 5:
        body0 = gSim.body(10**10,5,(255,0,0),[-150,0, 0],[2017.5,-3494.413,1000.])
        body1 = gSim.body(10**10,5,(255,123,187),[150,0,0.],[2017.5,3494.413,1000.])
        body2 = gSim.body(10**10, 5, (203,180,240),[0.,259.808,0.],[-4035.,0.,1000.])

    ##Such 8 eliptic!!!!!!!!!!!!!!!
    elif indice == 6:
        body0 = gSim.body(2.05*10**6,5,(255,0,0),[0.97000436*100,-0.24308753*100, 0],[0.5*0.93240737*100,0.5*0.86473146*100,1000.])
        body1 = gSim.body(2.05*10**6,5,(255,123,187),[-0.97000436*100,0.24308753*100,0.],[0.5*0.93240737*100,0.5*0.86473146*100,1000.])
        body2 = gSim.body(2.05*10**6, 5, (203,180,240),[0.,0.,0.],[-0.93240737*100,-0.86473146*100,0.])


    bodies =[body0, body1, body2]
    return bodies

def mouse_over_button(y_pos, screen = 0):
    if pygame.mouse.get_pos()[0] < 80 and pygame.mouse.get_pos()[0] > 10:
        if  pygame.mouse.get_pos()[1] < y_pos+20 and pygame.mouse.get_pos()[1] > y_pos:
            if screen:
                pygame.draw.rect(screen, [200, 120, 120], [10, y_pos, 70, 20])
            return True
    else:
        return False

def main():
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 15)

    f = open("data.txt", "w")
    f.write("#iteration || Kinetic || Potential || Mechanical \n")
    iteration = 0
    
    
    FPS = 80
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    menu = pyglet.window.Window(visible = False)
    CLOCK = pygame.time.Clock()
    REALTIMEGRAPH = False
    DISPLAYING_MENU = False
    Trail = False
    theta = [0, 0, 0]
    BREAK = False
    
    down = False
    up = False
    right = False
    left = False

    plt.axis([0,1000,10**10,3*10**10])
    plt.ylabel('Energies')
    plt.xlabel("Iterations from start")
    plt.ion()
    plt.show
    
    #restricted bodies
    #rbody1 = gSim.body(10**10,5,(255,123,255),[WIDTH/2 + 150,HEIGHT/2,0.],[0.,-3000.,0.])
    rbody1 = gSim.body(10**10,5,(255,0,0),[250,0, 0],[0.,-2236.594,0.])
    rbody2 = gSim.body(10**10,5,(255,123,187),[-250,0,0.],[0.,2236.594,0.])
    rbody3 = gSim.body(5*10**7, 5, (203,180,240),[100.,0.,0.],[0.,3459.,0.])
        
    rbodies = [rbody1,rbody2,rbody3] #Assume-se que o rbody3 e o que tem a massa menor!

    #bodies
    bodies = reset_bodies()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    Trail = False
                    down = not down
                if event.key == pygame.K_UP:
                    Trail = False
                    up = not up
                if event.key == pygame.K_RIGHT:
                    Trail = False
                    right = not right
                if event.key == pygame.K_LEFT:
                    Trail = False
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
                for indice in range(7):
                    if pygame.mouse.get_pos()[0] < 80 and pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[1] < 600 + indice*30 + 20 and pygame.mouse.get_pos()[1] > 600 + indice*30:
                        bodies = reset_bodies(indice)
                        theta = [45,0 , 45]
                        BREAK = True
                        break
                if BREAK:
                    BREAK = False
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
        pygame.draw.rect(screen, [120, 120, 120], [10, 300+300, 70, 20])
        pygame.draw.rect(screen, [120, 120, 120], [10, 330+300, 70, 20])
        pygame.draw.rect(screen, [120, 120, 120], [10, 360+300, 70, 20])
        pygame.draw.rect(screen, [120, 120, 120], [10, 390+300, 70, 20])
        pygame.draw.rect(screen, [120, 120, 120], [10, 420+300, 70, 20])
        pygame.draw.rect(screen, [120, 120, 120], [10, 450+300, 70, 20])

        pygame.draw.line(screen, (255,0,0), [10,50], [50,50], 1)
        xaxis = myfont.render("x axis", 1, (255, 0, 0))
        pygame.draw.line(screen, (0,255,0), [10,60], [50,60], 1)
        yaxis = myfont.render("y axis", 1, (0, 255, 0))
        pygame.draw.line(screen, (0,0,255), [10,70], [50,70], 1)
        zaxis = myfont.render("z axis", 1, (0, 0, 255))
        screen.blit(xaxis, (60, 35))                      
        screen.blit(yaxis, (60, 50))
        screen.blit(zaxis, (60, 65))

        mouse_over_button(600, screen)
        mouse_over_button(630, screen)
        mouse_over_button(660, screen)
        mouse_over_button(690, screen)
        mouse_over_button(720, screen)
        mouse_over_button(750, screen)
    
        L1 = myfont.render("L1",1, (255,255,255))
        L4 = myfont.render("L4",1, (255,255,255))
        M1 = myfont.render("8 Mov",1, (255,255,255))
        M2 = myfont.render("Mov 2",1, (255,255,255))
        M3 = myfont.render("Mov 3",1, (255,255,255))
        M4 = myfont.render("Mov 4",1, (255,255,255))
        M5 = myfont.render("Mov 5",1, (255,255,255))
        screen.blit(L1, (12, 602))
        screen.blit(L4, (12, 632))
        screen.blit(M1, (12, 662))
        screen.blit(M2, (12, 692))
        screen.blit(M3, (12, 722))
        screen.blit(M4, (12, 752))
	screen.blit(M4, (12, 782))
        ##### GUI#####

        draw_axis(theta, screen)
        draw_next_with_steps(bodies, 0.0004, screen, theta)
        #draw_next_restricted(rbodies, 0.0001, screen, theta) #new function - recebe sempre 3 bodies
        #draw_centerOfMass(rbodies,screen)
        draw_centerOfMass(bodies,screen, theta)
        #draw_totalEnergy(bodies,screen, f, iteration)
        #draw_momentum(bodies,screen,f,iteration)#apenas para 3 corpos
        #double_draw_totalEnergy(rbodies,bodies,screen, f, iteration)#A vermelho o restricted e preto o real - eu pus para desenhar o potencial em vez de a energia total
        pygame.display.flip()
        CLOCK.tick(FPS)
        iteration +=1


main()
