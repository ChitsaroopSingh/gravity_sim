import math
from physics.body import Body

def handle_collisions(bodies):
    to_remove=set()
    to_add=[]
    for i in range(len(bodies)):
            for j in range(i+1,len(bodies)):
                body1=bodies[i]
                body2=bodies[j]

                dx=body2.position[0]-body1.position[0]
                dy=body2.position[1]-body1.position[1]

                distance=math.sqrt(dx**2 + dy**2) 

                if distance < body1.radius + body2.radius :
                    new_mass = body1.mass + body2.mass
                    #formulas for centre of mass and velocities
                    new_x = ((body1.position[0])*(body1.mass)+(body2.position[0])*(body2.mass)) / new_mass
                    new_y = ((body1.position[1])*(body1.mass)+(body2.position[1])*(body2.mass)) / new_mass

                    new_vx = ((body1.velocity[0])*(body1.mass)+(body2.velocity[0])*(body2.mass)) / new_mass
                    new_vy = ((body1.velocity[1])*(body1.mass)+(body2.velocity[1])*(body2.mass)) / new_mass
                    merged = Body(new_mass,(new_x,new_y),(new_vx,new_vy),color="white")
                
                    to_remove.add(body1)
                    to_remove.add(body2)

                    to_add.append(merged)
    
    bodies=[b for b in bodies if b not in to_remove]
    bodies.extend(to_add)
    
    
    return bodies
