import math;

def fmt(value):
    return "%.3f" % value

period = 4
radius = 1.5
timestep = 0.02
maxtime = period*2
z = -1

with open('HelixUpDownFF.txt', 'w') as the_file:
    t=0;
    pastX = 0
    pastY = 0
    pastZ = 0
    pastVx = 0
    pastVy = 0
    pastVz = 0 

    while t <= maxtime/2:
        x = math.sin(t * 2 * math.pi / period) * radius;
        y = math.cos(t * 2 * math.pi / period) * radius; 
        the_file.write(fmt(t) + "," + fmt(x) + "," + fmt(y) + "," + fmt(z));

        vx = (x - pastX) / timestep
        vy = (y - pastY) / timestep
        vz = (z - pastZ) / timestep

        the_file.write("," + fmt(vx) + "," + fmt(vy) + "," + fmt(vz))

        accX = (vx - pastVx) / timestep
        accY = (vy - pastVy) / timestep
        accZ = (vz - pastVz) / timestep

        the_file.write("," + fmt(0.0) + "," + fmt(0.0) + "," + fmt(0.0))
        the_file.write("," + fmt(accX) + "," + fmt(accY) + "," + fmt(accZ))

        pastX = x
        pastY = y
        pastZ = z
        pastVx = vx
        pastVy = vy
        pastVz = vz

        the_file.write("\n")

        t += timestep;
        z -= 0.01
    while t>maxtime/2 and t <= maxtime:
        x = math.sin(t * 2 * math.pi / period) * radius;
        y = math.cos(t * 2 * math.pi / period) * radius; 
        the_file.write(fmt(t) + "," + fmt(x) + "," + fmt(y) + "," + fmt(z));

        vx = (x - pastX) / timestep
        vy = (y - pastY) / timestep
        vz = (z - pastZ) / timestep

        the_file.write("," + fmt(vx) + "," + fmt(vy) + "," + fmt(vz))

        accX = (vx - pastVx) / timestep
        accY = (vy - pastVy) / timestep
        accZ = (vz - pastVz) / timestep

        the_file.write("," + fmt(0.0) + "," + fmt(0.0) + "," + fmt(0.0))
        the_file.write("," + fmt(accX) + "," + fmt(accY) + "," + fmt(accZ))

        pastX = x
        pastY = y
        pastZ = z
        pastVx = vx
        pastVy = vy
        pastVz = vz 

        the_file.write("\n")

        t += timestep;
        z += 0.01

