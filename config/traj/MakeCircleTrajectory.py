import math;

def fmt(value):
    return "%.3f" % value

period = 4
radius = 1.5
timestep = 0.02
maxtime = period*3
z = -1

with open('CircleFF.txt', 'w') as the_file:
    t=0;
    pastX = 0
    pastY = 0
    pastVx = 0
    pastVy = 0
    while t <= maxtime:
        x = math.sin(t * 2 * math.pi / period) * radius;
        y = math.cos(t * 2 * math.pi / period) * radius;
        the_file.write(fmt(t) + "," + fmt(x) + "," + fmt(y) + "," + fmt(z));
        vx = (x - pastX) / timestep
        vy = (y - pastY) / timestep

        the_file.write("," + fmt(vx) + "," + fmt(vy))

        accX = (vx - pastVx) / timestep
        accY = (vy - pastVy) / timestep

        the_file.write("," + fmt(0.0) + "," + fmt(0.0) + "," + fmt(0.0))
        the_file.write("," + fmt(accX) + "," + fmt(accY) + "," + fmt(y))

        pastX = x
        pastY = y
        pastVx = vx
        pastVy = vy

        the_file.write("\n")

        t += timestep;
            
