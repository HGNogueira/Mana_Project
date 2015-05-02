"""
A body is a simple abstraction that defines an object with mass and size whom can interact gravitationaly with other bodies. Geometrically they are all spherical and contain simple coloring.
This class contains the vital information regarding each body type object, that is:
-mass (in earth mass ratio, real_mass=mass*5.97219*10**24 kg
-radius (radius in earth radius ratio, real_radius = radius * 6371*10**3 m)
-color
-position (in a list with coordinates => list(x,y,z)
-speed ( "  "  "  " )
"""
G = 1



class object(object):
    def __init__(self, mass, radius, color, position, speed):
        self.mass = mass
        self.radius = radius
        self.color = color 
        self.position = position
        self.speed = speed
        
def eval_nextVel(objects, myBody_it):
    #This class returns velocity at time t+dt
    myBody=objects[myBody_it]
    idx = 0 
    
    for other in objects:
        #if idx == myBody_it: continue
        r = ((myBody.position[0] - other.position[0])**2 + (myBody.position[1] - other.position[1])**2 + (myBody.position[2] - other.position[2])**2)**(1./2.) #distance between myBody and other
        if(r != 0):
            myBody.speed[0] += -G*(other.mass)*(myBody.position[0] - other.position[0])/r
            myBody.speed[1] += -G*(other.mass)*(myBody.position[1] - other.position[1])/r
            myBody.speed[2] += -G*(other.mass)*(myBody.position[2] - other.position[2])/r
        idx +=1

    return myBody.speed

def next_pos(object):
    object.position[0]+=object.speed[0]
    object.position[1]+=object.speed[1]
    object.position[2]+=object.speed[2]
    return object.position


