'''
Created on 26.06.2019

@author: fkluiben
'''
#from srcFlorian import srcFlorian.FKExamples    
from Shark import Shark
from FKExamples import FKExamples

#fkEx = FKExamples()
#How to create objects and instances such as Sammy?
#https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3

sammy = Shark('Sammy')
fk = FKExamples()

if __name__ == '__main__':
    fk.runAll()
    sammy.swim()
    sammy.be_awesome()