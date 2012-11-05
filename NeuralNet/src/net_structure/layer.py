'''
Created on 02-11-2012

@author: Krzysztof
'''

class Layer:
    '''
    classdocs
    '''


    def __init__(self, nodes):
        '''
        Constructor
        '''
        self.nodes = nodes
    
    def __str__(self):
        result = '-layer\n'
        for node in self.nodes :
            result = result + str(node)
        return result
    
    def copy_values_from_input_vector(self, input_vector):
        for node in self.nodes:
            node.set_value(input_vector.get_value_for_node(node.nodeId))
            
    def propagate(self):
        for node in self.nodes:
            node.propagate()
            
    def clear_values(self):
        for node in self.nodes:
            node.clear_value()