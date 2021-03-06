import math;

def fmt(value):
    return "%.3f" % value

period = [4, 2, 4]
radius = 1.5
timestep = 0.02
maxtime = max(period)*3
timemult = [1.00, 1.00, 1.00]
phase=[0,0,0]
amp = [1,0.4,.5]
center = [0, 0, -2]

with open('FigureEightFF.txt', 'w') as the_file:
    t=0
    pastX = 0
    pastY = 0
    pastZ = 0
    pastVx = 0
    pastVy = 0
    pastVz = 0 

    while t <= maxtime:
        x = math.sin(t * 2 * math.pi / period[0] * timemult[0] + phase[0]) * radius * amp[0] + center[0]
        y = math.sin(t * 2 * math.pi / period[1] * timemult[1] + phase[1]) * radius * amp[1] + center[1]
        z = math.sin(t * 2 * math.pi / period[2] * timemult[2] + phase[2]) * radius * amp[2] + center[2]
        the_file.write(fmt(t) + "," + fmt(x) + "," + fmt(y) + "," + fmt(z))

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
        
        t += timestep
            
