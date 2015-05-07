"""In this python module we try to simulate the behaviour of free moving bodies interacting only through gravitational force. It is composed by:
  -Class body, that simply stores information regarding a specific body with mass
  -Functions that calculate the next position of a list(body1,body2,...) given their current status

  G is the gravitational constant
"""
G = 0.49


class body(object):
    def __init__(self, mass, radius, color, position, speed):
        self.mass = mass         #type int
        self.radius = radius     #type int
        self.color = color       #type list(int,int,int) RGB
        self.position = position #type list(float x, float y, float z)
        self.speed = speed       #type list(float x, float y, float z)
                    

    
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
