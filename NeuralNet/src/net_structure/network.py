'''
Created on 02-11-2012

@author: Krzysztof
'''

class NeuralNetwork :
    
    def __init__(self, layers, conscienceCoefficient=None):
        self.layers = layers
        self.conscienceCoefficient = conscienceCoefficient if conscienceCoefficient is not None else 0.0
    
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
    
    def learn(self, input_vector, coefficient, conscienceCoefficient):
        #TODO:
        #Find a better way to store normalized weights vector
        for node in self.layers[-1].nodes:
            node.normize()
        result = self.calculte_answer(input_vector)
        self.layers[-1].learn(coefficient, conscienceCoefficient)
        for node in self.layers[-1].nodes:
            node.normize()
        return result
        
    def learning_process(self, input_vectors, coefficient, coefficient_half_life, turns):
        for i in range(1, turns):
            reducer = pow(0.5, i/coefficient_half_life) if coefficient_half_life is not None else 1.0
            for input_vector in input_vectors:
                self.learn(input_vector, coefficient * reducer, self.conscienceCoefficient * reducer)
        print(self)
    