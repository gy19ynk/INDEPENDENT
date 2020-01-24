# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:24:56 2019

@author: Yankho Naomi Kalebe

Before the model is run, the environment,and drunks are initialised and enabled to move by the following code
"""

#builds drunks class, initialises them in a random location,and moves them
import random
class drunks:
    
    def __init__(self,environment): #initialises the environment
        self.environment=environment
        self.x = random.randint(149,150)
        self.y = random.randint(150,151)

    def move(self):                 #moves the drunks
        if random.random() < 0.5:
            self.x= (self.x+1)% 300
        else :
            self.x=(self.x-1)%300
        
        if random.random() < 0.5:
             self.y= (self.y+1) % 300
        else :
            self.y=(self.y-1) %300   
    

          




