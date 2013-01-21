'''
Created on 02-11-2012

@author: Krzysztof
'''

class Link:
    '''
    classdocs
    '''


    def __init__(self, from_node, to_node, weight):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

    def __str__(self):
        return '\t\t-link(' + str(self.weight) + ') from ' + self.from_node.nodeId + ' to ' + self.to_node.nodeId + '\n' 
    
    def learn(self, value, expected_value, coefficient, k = 1.0):
        if self.to_node.activationFunction.get_name() == 'sigmoid':
            self.delta_learn(value, expected_value, coefficient, self.to_node.activationFunction, k = 1.0)
        else: 
            self.windrow_hoff_learn(value, expected_value, coefficient)
            
    def windrow_hoff_learn(self, value, expected_value, coefficient, k = 1.0):
        self.weight = self.weight + coefficient * (expected_value - value) * k
        
    def delta_learn(self, value, expected_value, coefficient, activation_function, k = 1.0):
        self.weight = self.weight + coefficient * (expected_value - value) * k * activation_function.derivative_value(value)
    
    def bp_learn(self, speed, delta):
        self.weight = self.weight + speed * self.from_node.get_value()