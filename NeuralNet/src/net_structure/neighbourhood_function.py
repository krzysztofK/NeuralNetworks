'''
Created on 26-11-2012

@author: Krzysztof
'''
import math

class NeighbourhoodFucntion:
            
    def calculate(self, distance, neighbourhoodWidth):
        if neighbourhoodWidth >= distance :
            return math.exp(-1.0 * distance ** 2.0)
        else :
            return 0.0
