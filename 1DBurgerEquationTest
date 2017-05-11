import numpy
from matplotlib import pyplot
# %matplotlib inline

nx = 41 #Number of steps in space(x)
dx = 2/(nx - 1) #Width of space step
nt = 25#Number of time steps
dt = 0.025 #
c  = 1 # Velocity of wave
u = numpy.ones(nx)
u[int(.5/dx):int(1/dx +1)] = 3
un = numpy.ones(nx) #initialize a temporary array

for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
    un = u.copy() ##copy the existing values of u into un
    for i in range(1, nx): ## you can try commenting this line and...
    #for i in range(nx): ## ... uncommenting this line and see what happens!
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])

pyplot.plot(numpy.linspace(0,2,nx),u) ##Plot the results
