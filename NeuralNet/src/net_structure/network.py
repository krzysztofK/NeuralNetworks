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
        for node in self.kohonenLayer.nodes:
            node.normize()
        result = self.calculte_answer(input_vector)
        self.kohonenLayer.learn(coefficient, conscienceCoefficient)
        for node in self.kohonenLayer.nodes:
            node.normize()
        return result
        
    def learning_process(self, input_vectors, coefficient, coefficient_half_life, turns):
        for i in range(1, turns):
            reducer = pow(0.5, i/coefficient_half_life) if coefficient_half_life is not None else 1.0
            for input_vector in input_vectors:
                self.learn(input_vector, coefficient * reducer, self.conscienceCoefficient * reducer)
        print(self)

    def cp_learning_process(self, input_vectors, coefficient, coefficient_half_life, turns, grossberg_coefficient):
        for i in range(1, turns):
            reducer = pow(0.5, i/coefficient_half_life) if coefficient_half_life is not None else 1.0
            grossberg_reducer = 0.0 if turns < 2000 else 1.0
            for input_vector in input_vectors:
                self.learn(input_vector, coefficient * reducer, self.conscienceCoefficient * reducer)
                result = self.calculte_answer(input_vector)
                max_value = 0.0
                winner = None
                for node in self.kohonenLayer.nodes :
                    if node.get_value() > max_value :
                        max_value = node.get_value()
                        winner = node
                for node in self.grossbergLayer.nodes :
                    value = result[0]
                    result = result[1:]
                    expected_value = input_vector.expected_value_dict[node.nodeId]
                    for link in node.backward_links :
                        if link.from_node is winner :
                            link.windrow_hoff_learn(value, expected_value, grossberg_coefficient * grossberg_reducer * reducer)
                            