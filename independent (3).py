# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:16:11 2020

@author: gy19ynk

The model is run using drunks and the environment called and initialised in the agentframework. Matplotlib is used to plot the scatter 
plot of the drunks which are assembled in one place pub as a starting point. The coordinate values of the houses are also plotted using
matplotlib on the screen drawn of the environment. The drunks are enabled to move and the result is shown on the screen with each drunk
at a specific location.
"""

#import operator exports a set of functions used in the model
import numpy as np
import matplotlib.pyplot
import agentframework
import matplotlib.animation


#initiates variables used in the model
num_of_drunks = 25
drunks =[]
house=[]
start_coor=[]

#Reads the file "drunk.plan.txt"
Field = np.genfromtxt("drunk.plan.txt", delimiter= ',')

    
#Closes the file "drunk.plan.txt" so it is no longer read or written     
f.close()
for a in range (300):
    for b in range (300):
        if environment[a][b] == 1:
            environment[a][b]= 100

#Initiates the class 'drunks'
for i in range (num_of_drunks):
    drunks.append(agentframework.drunks(environment))
    

#adds a label to the 25 houses that belong to the drunks       
for i in range (num_of_drunks):    
    houselabel = (i+1)*10
    house.append(houselabel)


#locates the drunks houses and moves the drunks to find their homes
for i in range(num_of_drunks):
    while environment[drunks[i].x][drunks[i].y] != house[i]:
        drunks[i].move()
    print(drunks[i].x, drunks[i].y)    
    
 #plots the environment   
matplotlib.pyplot.xlim(0,300)  #plots x values
matplotlib.pyplot.ylim(0,300) #plots y values
for i in drunks:    
    matplotlib.pyplot.scatter(i.y,i.x)
matplotlib.pyplot.imshow(environment) #plots environment
matplotlib.pyplot.show()
