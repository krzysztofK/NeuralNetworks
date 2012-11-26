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
    
    def clear_values(self):
        for layer in self.layers:
            layer.clear_values()
    
    def calculte_answer(self, input_vector):
        self.clear_values()
        self.layers[0].copy_values_from_input_vector(input_vector)
        for layer in self.layers:
            layer.propagate()
        network_answer = []
        for node in self.layers[-1].nodes:
            network_answer.append(node.get_value())
        return network_answer
    
    def learn(self, input_vector, coefficient):
        #TODO:
        #Find a better way to store normalized weights vector
        for node in self.layers[-1].nodes:
            node.normize()
        result = self.calculte_answer(input_vector)
        self.layers[-1].learn(coefficient)
        for node in self.layers[-1].nodes:
            node.normize()
        return result
        
    