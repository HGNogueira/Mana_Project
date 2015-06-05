"""In this python module we try to simulate the behaviour of free moving bodies interacting only through gravitational force. It is composed by:
  -Class body, that simply stores information regarding a specific body with mass
  -Functions that calculate the next position of a list(body1,body2,...) given their current status

  G is the gravitational constant
"""
G = 0.49
#G = 1
#G=6.6738*10**(-11)

class body(object):
    def __init__(self, mass, radius, color, position, speed):
        self.mass = mass         #type int
        self.radius = radius     #type int
        self.color = color       #type list(int,int,int) RGB
        self.position = position #type list(float x, float y, float z)
        self.speed = speed       #type list(float x, float y, float z)
                    

def nextpos_restricted(bodies, step):
    r = get_distance(bodies[0],bodies[1])

    v1 = (bodies[0].speed[0]**2 + bodies[0].speed[1]**2)**0.5
    v2 = (bodies[1].speed[0]**2 + bodies[1].speed[1]**2)**0.5

    y1 = bodies[0].position[1]
    y2 = bodies[1].position[1]
    x1 = bodies[0].position[0]
    x2 = bodies[1].position[0]

    bodies[0].position[0] += v1*(y1-y2)/r*step
    bodies[0].position[1] -= v1*(x1-x2)/r*step 
    bodies[1].position[0] -= v1*(y1-y2)/r*step 
    bodies[1].position[1] += v1*(x1-x2)/r*step 

    nextValues_restricted_m3(bodies, step)

def nextValues_restricted_m3(bodies, step):
    r13 = get_distance(bodies[0],bodies[2])
    r23 = get_distance(bodies[1],bodies[2])

    y1 = bodies[0].position[1]
    y2 = bodies[1].position[1]
    y3 = bodies[2].position[1]
    x1 = bodies[0].position[0]
    x2 = bodies[1].position[0]
    x3 = bodies[2].position[0]

    m1 = bodies[0].mass
    m2 = bodies[1].mass

    bodies[2].speed[0] += -step*G*(m1*(x3-x1)/r13**3 + m2*(x3-x2)/r23**3)
    bodies[2].speed[1] += -step*G*(m1*(y3-y1)/r13**3 + m2*(y3-y2)/r23**3) 

    bodies[2].position[0] += bodies[2].speed[0]*step
    bodies[2].position[1] += bodies[2].speed[1]*step

def a(x,it,ncoord,step,bodies):
      
    ac = 0
    for i in range(3):
        if i == it: continue
        r = ((x[it][0]-x[i][0])**2 + (x[it][1]-x[i][1])**2 + (x[it][2]-x[i][2])**2)**(0.5)
        if r>=0:
            ac += -G*(bodies[i].mass)*(x[it][ncoord] - x[i][ncoord])/r**3
        i+=1

    return ac
            

def RK4(bodies,step):

    x = [[bodies[0].position[0],bodies[0].position[1],bodies[0].position[2]]
         ,[bodies[1].position[0],bodies[1].position[1],bodies[1].position[2]]
         ,[bodies[2].position[0],bodies[2].position[1],bodies[2].position[2]]]
    v = [[bodies[0].speed[0],bodies[0].speed[1],bodies[0].speed[2]]
         ,[bodies[1].speed[0],bodies[1].speed[1],bodies[1].speed[2]]
         ,[bodies[2].speed[0],bodies[2].speed[1],bodies[2].speed[2]]]

    x1 = [[x[0][0],x[0][1],x[0][2]]
          ,[x[1][0],x[1][1],x[1][2]]
          ,[x[2][0],x[2][1],x[2][2]]]
    v1 = [[v[0][0],v[0][1],v[0][2]]
          ,[v[1][0],v[1][1],v[1][2]]
          ,[v[2][0],v[2][1],v[2][2]]]
    a1 = [[a(x1,0,0,step,bodies),a(x1,0,1,step,bodies),a(x1,0,2,step,bodies)]
          ,[a(x1,1,0,step,bodies),a(x1,1,1,step,bodies),a(x1,1,2,step,bodies)]
          ,[a(x1,2,0,step,bodies),a(x1,2,1,step,bodies),a(x1,2,2,step,bodies)]]
 
    x2 = [[x[0][0] + 0.5*v1[0][0]*step, x[0][1] + 0.5*v1[0][1]*step, x[0][2] + 0.5*v1[0][2]*step],[x[1][0] + 0.5*v1[1][0]*step, x[1][1] + 0.5*v1[1][1]*step, x[1][2] + 0.5*v1[1][2]*step],[x[2][0] + 0.5*v1[2][0]*step, x[2][1] + 0.5*v1[2][1]*step, x[2][2] + 0.5*v1[2][2]*step]]
    v2 = [[v[0][0] + 0.5*a1[0][0]*step,v[0][1] + 0.5*a1[0][1]*step,v[0][2] + 0.5*a1[0][2]*step],[v[1][0] + 0.5*a1[1][0]*step,v[1][1] + 0.5*a1[1][1]*step,v[1][2] + 0.5*a1[1][2]*step],[v[2][0] + 0.5*a1[2][0]*step,v[2][1] + 0.5*a1[2][1]*step,v[2][2] + 0.5*a1[2][2]*step]]
    a2 = [[a(x2, 0,0, step/2.0,bodies),a(x2, 0, 1,step/2.0,bodies),a(x2, 0,2, step/2.0,bodies)],[a(x2, 1,0, step/2.0,bodies),a(x2, 1, 1,step/2.0,bodies),a(x2, 1,2, step/2.0,bodies)],[a(x2, 2,0, step/2.0,bodies),a(x2, 2, 1,step/2.0,bodies),a(x2, 2,2, step/2.0,bodies)]]

    x3 = [[x[0][0] + 0.5*v2[0][0]*step,x[0][1] + 0.5*v2[0][1]*step,x[0][2] + 0.5*v2[0][2]*step],[x[1][0] + 0.5*v2[1][0]*step,x[1][1] + 0.5*v2[1][1]*step,x[1][2] + 0.5*v2[1][2]*step],[x[2][0] + 0.5*v2[2][0]*step,x[2][1] + 0.5*v2[2][1]*step,x[2][2] + 0.5*v2[2][2]*step]]
    v3 = [[v[0][0] + 0.5*a2[0][0]*step,v[0][1] + 0.5*a2[0][1]*step,v[0][2] + 0.5*a2[0][2]*step],[v[1][0] + 0.5*a2[1][0]*step,v[1][1] + 0.5*a2[1][1]*step,v[1][2] + 0.5*a2[1][2]*step],[v[2][0] + 0.5*a2[2][0]*step,v[2][1] + 0.5*a2[2][1]*step,v[2][2] + 0.5*a2[2][2]*step]]
    a3 = [[a(x3, 0,0, step/2.0,bodies),a(x3, 0, 1,step/2.0,bodies),a(x3, 0, 2,step/2.0,bodies)],[a(x3, 1,0, step/2.0,bodies),a(x3, 1, 1,step/2.0,bodies),a(x3, 1, 2,step/2.0,bodies)],[a(x3, 2,0, step/2.0,bodies),a(x3, 2, 1,step/2.0,bodies),a(x3, 2, 2,step/2.0,bodies)]]

    x4 = [[x[0][0] + v3[0][0]*step,x[0][1] + v3[0][1]*step,x[0][2] + v3[0][2]*step],[x[1][0] + v3[1][0]*step,x[1][1] + v3[1][1]*step,x[1][2] + v3[1][2]*step],[x[2][0] + v3[2][0]*step,x[2][1] + v3[2][1]*step,x[2][2] + v3[2][2]*step]]
    v4 = [[v[0][0] + a3[0][0]*step,v[0][1] + a3[0][1]*step,v[0][2] + a3[0][2]*step],[v[1][0] + a3[1][0]*step,v[1][1] + a3[1][1]*step,v[1][2] + a3[1][2]*step],[v[2][0] + a3[2][0]*step,v[2][1] + a3[2][1]*step,v[2][2] + a3[2][2]*step]]
    a4 = [[a(x4, 0,0,step,bodies),a(x4, 0,1,step,bodies),a(x4, 0,2,step,bodies)],[a(x4, 1,0,step,bodies),a(x4, 1,1,step,bodies),a(x4, 1,2,step,bodies)],[a(x4, 2,0,step,bodies),a(x4, 2,1,step,bodies),a(x4, 2,2,step,bodies)]]


    for it in range(len(bodies)):
        for j in range(3):
            bodies[it].position[j] += (step/6.0)*(v1[it][j] + 2*v2[it][j] + 2*v3[it][j] + v4[it][j])
            bodies[it].speed[j] += (step/6.0)*(a1[it][j] + 2*a2[it][j] + 2*a3[it][j] + a4[it][j])
            #bodies[it].speed[j] += (step)*(a1[it][j])
            #bodies[it].position[j] += (step)*(bodies[it].speed[j])
            j+=1
        it+=1


def nextVel_with_steps(bodies, step):#already called by nextpos
    """ This functions takes a list of multiple type body changes their velocities to the next iterative value"""
    
    for it in range(len(bodies)):#double iteration
        for idx in range(len(bodies)):# for speed replacement
            if it == idx: continue 
            r = get_distance(bodies[it], bodies[idx])
            if r>= bodies[it].radius + bodies[idx].radius:
               bodies[it].speed[0] += -step*G*(bodies[idx].mass)*(bodies[it].position[0] - bodies[idx].position[0])/r**3
               bodies[it].speed[1] += -step*G*(bodies[idx].mass)*(bodies[it].position[1] - bodies[idx].position[1])/r**3
               bodies[it].speed[2] += -step*G*(bodies[idx].mass)*(bodies[it].position[2] - bodies[idx].position[2])/r**3
            #else:
                #del bodies[idx]
                #del bodies[it]
            idx+=1
        it+=1
            
def next_pos_with_steps(bodies, step):
    """This function calculates the next iterative position using steps computing, it automatically calls for the function nextVel_with_steps """
    if len(bodies) > 0:
        nextVel_with_steps(bodies, step)
        for body in bodies:
            body.position[0]+=step*body.speed[0]
            body.position[1]+=step*body.speed[1]
            body.position[2]+=step*body.speed[2]


def get_centerOfMass(bodies):
    """This Function returns the center of mass of a given list of body's"""
    if len(bodies) > 0:
        posCM = [0,0,0]
        mTotal = 0
        for body in bodies:
            posCM[0]+=body.position[0]*body.mass
            posCM[1]+=body.position[1]*body.mass
            posCM[2]+=body.position[2]*body.mass
            mTotal+=body.mass
    
        posCM[0]=posCM[0]/mTotal
        posCM[1]=posCM[1]/mTotal
        posCM[2]=posCM[1]/mTotal

    return posCM

def get_distance(body1, body2):
    r = ((body1.position[0] - body2.position[0])**2 + (body1.position[1] - body2.position[1])**2 + (body1.position[2] - body2.position[2])**2)**(1./2.)
    return r
