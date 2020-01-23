# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:16:11 2020

@author: gy19ynk
"""

import numpy as np
import matplotlib.pyplot
import agentframework
import matplotlib.animation



num_of_drunks = 25
drunks =[]
house=[]
start_coor=[]

#Reads the file "drunk.plan.txt"
Field = np.genfromtxt("drunk.plan.txt", delimiter= ',')


f = open('drunk.plan.txt')
environment = []
for row in f:
    parsed_row = str.split(row, ",")
    rowlist=[]
    for value in parsed_row:
            rowlist.append(float(value))
    environment.append(rowlist)
f.close()
for a in range (300):
    for b in range (300):
        if environment[a][b] == 1:
            environment[a][b]= 100


for i in range (num_of_drunks):
    drunks.append(agentframework.drunks(environment))
    
       
for i in range (num_of_drunks):    
    houselabel = (i+1)*10
    house.append(houselabel)


for i in range(num_of_drunks):
    while environment[drunks[i].x][drunks[i].y] != house[i]:
        drunks[i].move()
    print(drunks[i].x, drunks[i].y)    
    
    
matplotlib.pyplot.xlim(0,300)  #plots x values
matplotlib.pyplot.ylim(0,300) #plots y values
for i in drunks:    
    matplotlib.pyplot.scatter(i.y,i.x)
matplotlib.pyplot.imshow(environment) #plots environment
matplotlib.pyplot.show()
