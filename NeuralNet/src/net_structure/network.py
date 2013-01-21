'''
Created on 02-11-2012

@author: Krzysztof
'''
from net_structure.layer import KohonenLayer, GrossbergLayer

class NeuralNetwork :
    
    def __init__(self, layers, conscienceCoefficient=None):
        self.layers = layers
        self.conscienceCoefficient = conscienceCoefficient if conscienceCoefficient is not None else 0.0
        self.kohonenLayer = None
        self.grossbergLayer = None
        for layer in layers :
            if isinstance(layer, KohonenLayer) :
                self.kohonenLayer = layer
            elif isinstance(layer, GrossbergLayer) :
                self.grossbergLayer = layer
        
    def __str__(self):
        result = ''
        for layer in self.layers :
            result = result + str(layer)
        return result
    
    def clear_values(self):
        for layer in self.layers:
            layer.clear_values()
    
    def calculte_answer(self, input_vector, debug=False):
        self.clear_values()
        self.layers[0].copy_values_from_input_vector(input_vector)
        for layer in self.layers:
            layer.propagate(debug)
        network_answer = []
        for node in self.layers[-1].nodes:
            network_answer.append(node.get_value())
        return network_answer
    
    def learn(self, input_vector, coefficient, conscienceCoefficient, neighbourhoodWidth):
        #TODO:
        #Find a better way to store normalized weights vector
        for node in self.kohonenLayer.nodes:
            node.normize()
        result = self.calculte_answer(input_vector)
        self.kohonenLayer.learn(coefficient, conscienceCoefficient, neighbourhoodWidth)
        for node in self.kohonenLayer.nodes:
            node.normize()
        return result
        
    def learning_process(self, input_vectors, coefficient, coefficient_half_life, turns, neighbourhoodWidth):
        for i in range(1, turns):
            reducer = pow(0.5, i/coefficient_half_life) if coefficient_half_life is not None else 1.0
            for input_vector in input_vectors:
                self.learn(input_vector, coefficient * reducer, self.conscienceCoefficient * reducer, neighbourhoodWidth)
        print(self)

    def cp_learning_process(self, input_vectors, coefficient, coefficient_half_life, turns, neighbourhoodWidth, grossberg_coefficient, grossberg_coefficient_half_life):
        for input_vector in input_vectors :
            input_vector.normize()
        for i in range(1, turns):
            reducer = pow(0.5, i/coefficient_half_life) if coefficient_half_life is not None else 1.0
            grossberg_reducer = pow(0.5, i/grossberg_coefficient_half_life) if i > 2000 else 1.0
            reducer = reducer if i < 2000 else 0.0
            for input_vector in input_vectors:
                self.learn(input_vector, coefficient * reducer, self.conscienceCoefficient * reducer, neighbourhoodWidth)
                winner = self.kohonenLayer.winner
                #self.calculte_answer(input_vector)
                if winner is not None :
                    for link in winner.links :
                        nextNode = link.to_node
                        value = nextNode.get_value()
                        expected_value = input_vector.expected_value_dict[nextNode.nodeId]
                        winner.normize()
                        #nextNode.normize()
                        link.learn(value, expected_value, grossberg_coefficient * grossberg_reducer)
                        winner.normize()
                        #nextNode.normize()
    
    def backpropagate(self):
        pass
                       
    def backpropagation_learn(self, input_vectors, learning_rate, iterations):
        for i in range(iterations):
            error = 0.0
            for input_vector in input_vectors:
                self.calculte_answer(input_vector)
                self.backpropagate()