# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:59:31 2017

@author: otila_000
"""

#%%
import numpy
from matplotlib import pyplot as plt
#%%
def linearconv(nx):
    nxf = float(nx) #Because python 2.7 is stupid
    dx = 2 /(nxf - 1) #Width of each step
    nt = 20 # nt is the number of timesteps we want
    dt = 0.025 #dt is the amount fo time each timestep cover (delta)* t
    c = 1
    
    u = numpy.ones(nx) # define a numpy array which is nx elements long with every element equal to 1
    u[int(.5/dx):int(1/ dx + 1)] = 2 # setting u = 2 between 0.5 and 1 as per our I.C's
    
    un = numpy.ones(nx) # initializing our placeholer array , un , to hold the values we calculate for the (n+1) timestep
    
    for n in range(nt): # itereate thought time
        un = u.copy()
        for i in range(1,nx):
            u[i] = un[i] - c * dt / dx * (un[i]-un[i-1])
            #plt.plot(numpy.linspace(0,2,nx),u)  
            
    plt.plot(numpy.linspace(0,2,nx),u)    