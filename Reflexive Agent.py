# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 07:26:48 2018

@author: Sajid Shah
"""

import random


class Environment:
    def __init__(self):
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty
        self.locationCondition = {'A': 0, 'B': 0, 'C':0}

        # randomize conditions in locations A and B
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)
        self.locationCondition['C'] = random.randint(0, 1)

class Agent:
    def __init__(self,Environment):
        self.location = random.randint(0,2)
        
#    def definemove():
#        if(Environment.locationCondition['A'] == 0):
#            return 'C'
#        elif(Environment.locationCondition['C'] == 0):
#            return 'A'
#        else:
#            return ''
    
    def left_move(self,location):
        print("moving to location ",location)
        
    def right_move(self,location):
        print("moving to location ",location)
        
    def suck_dirt(self, location):
        if location ==0:
            print("Location A has been cleaned")
        elif(location == 1):
            print("Location B has been cleaned")
        else:
            print("Location C has been cleaned")
        

class SimpleReflexVacuum:
    def __init__(self, Agent,Environment):
        print(Environment.locationCondition)
        
        if Agent.location==0: #agent is at location A
            print("Agent is randomly placed at location A")
            if Environment.locationCondition['A']==1:
                Agent.suck_dirt(0)
                Environment.locationCondition['A']=0
                self.CheckFromA(Agent,Environment)
                
            else:
                self.CheckFromA(Agent,Environment)
                        
        elif Agent.location==1:
                print("Agent is randomly placed at location B")
                
                if Environment.locationCondition['B']==1:
                    Agent.suck_dirt(1)
                    Environment.locationCondition['B']=0
                    self.CheckFromB(Agent,Environment)
                else:
                    self.CheckFromB(Agent,Environment)
                    
        elif Agent.location==2:
                print("Agent is randomly placed at location C")
                if Environment.locationCondition['C']==1:
                    Agent.suck_dirt(1)
                    Environment.locationCondition['C']=0
                    self.CheckFromC(Agent,Environment)
                    
                else:
                    self.CheckFromC(Agent,Environment)
                
                
        print(Environment.locationCondition)

    def CheckFromA(self,Agent,Environment):
        Agent.right_move(location='B')
        if Environment.locationCondition['B']==1:
            Agent.suck_dirt(1)
            Environment.locationCondition['B']=0
            
            Agent.right_move(location='C')
            if(Environment.locationCondition['C']==1):
                Agent.suck_dirt(2)
                Environment.locationCondition['C']= 0
                
    def CheckFromB(self,Agent,Environment):
        Agent.left_move(location='A')
        if Environment.locationCondition['A']==1:
            Agent.suck_dirt(0)
            Environment.locationCondition['A']=0
            
        Agent.right_move(location='B')
        
        Agent.right_move(location='C')
        if(Environment.locationCondition['C']==1):
            Agent.suck_dirt(2)
            Environment.locationCondition['C']= 0
        
        
                
    def CheckFromC(self,Agent,Environment):
        Agent.left_move(location='B')
        if Environment.locationCondition['B']==1:
            Agent.suck_dirt(0)
            Environment.locationCondition['B']=0
            
            Agent.left_move(location='A')
            if Environment.locationCondition['A']==1:
                Agent.suck_dirt(0)
                Environment.locationCondition['A']=0
                
e = Environment()
a = Agent(e)
v = SimpleReflexVacuum(a,e)