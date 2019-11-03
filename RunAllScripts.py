'''
Created on 26.06.2019

@author: fkluiben
'''
#from srcFlorian import srcFlorian.FKExamples    
#what advantage is it to create an abstract class XXXExamples and all our individual classes inherit from it:
from FKExamples import FKExamples
from srcAnja.AnjaExamples import AnjaExamples

#fkEx = FKExamples()
#How to create objects and instances such as Sammy?
#https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3

fk = FKExamples()
anja = AnjaExamples()

if __name__ == '__main__':
    fk.runAll()
    anja.runAll()
    #same thing for olli
    #