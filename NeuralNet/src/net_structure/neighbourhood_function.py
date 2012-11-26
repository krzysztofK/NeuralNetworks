'''
Created on 26-11-2012

@author: Krzysztof
'''
import math

class NeighbourhoodFucntion:
            
    def calculate(self, distance):
        return math.exp(-1.0 * distance ** 2.0)