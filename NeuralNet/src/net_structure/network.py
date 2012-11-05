'''
Created on 02-11-2012

@author: Krzysztof
'''

class NeuralNetwork :
    
    def __init__(self, layers):
        self.layers = layers
    
    def __str__(self):
        result = ''
        for layer in self.layers :
            result = result + str(layer)
        return result
    
    def calculte_answer(self, input_vector):
        pass