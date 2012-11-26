'''
Created on 02-11-2012

@author: Krzysztof
'''
from net_structure.neighbourhood_function import NeighbourhoodFucntion

class Layer:
    '''
    classdocs
    '''


    def __init__(self, nodes, bias):
        '''
        Constructor
        '''
        self.nodes = nodes
        self.bias = bias
    
    def __str__(self):
        result = '-layer - ' + self.__class__.__name__ + '\n'
        for node in self.nodes :
            result = result + str(node)
        return result
    
    def copy_values_from_input_vector(self, input_vector):
        for node in self.nodes:
            node.set_value(input_vector.get_value_for_node(node.nodeId))
            
    def propagate(self):
        for node in self.nodes:
            node.propagate()
        self.bias.propagate()
            
    def clear_values(self):
        for node in self.nodes:
            node.clear_value()
            
    def get_nodes_ids(self):
        resp = []
        for node in self.nodes:
            resp.append(node.nodeId)
        return resp

class KohonenLayer(Layer):
    
    def __init__(self, nodes, bias, neighbourhoodType, rows, columns, conscience):
        Layer.__init__(self, nodes, bias)
        self.neighbourhoodType = neighbourhoodType
        self.rows = rows
        self.columns = columns
        self.conscience = conscience
        self.neighbourhoodFunction = NeighbourhoodFucntion()
        
    def __str__(self):
        return Layer.__str__(self) + '- dimension - ' + str(self.rows) + ' x ' + str(self.columns)
    
    def learn(self, coefficient):
        maximum = None
        for node in self.nodes:
            current_value = node.get_value()
            if (maximum is None) or (current_value > maximum[0]):
                maximum = (current_value, node)
        if self.conscience:
            #TODO:
            #Change maximum(winner node) if it wins too often
            pass
        
        if self.neighbourhoodType:
            winnerIndex = self.nodes.index(maximum[1])
            for nodeIndex in range(len(self.nodes)) :
                if winnerIndex != nodeIndex :
                    self.nodes[nodeIndex].learn(coefficient * self.neighbourhoodFunction.calculate(self.distance(nodeIndex, winnerIndex)))
        maximum[1].learn(coefficient)
    
    def distance(self, nodeIndex, winnerIndex):
        return abs(self.row(nodeIndex) - self.row(winnerIndex)) + abs(self.column(nodeIndex) - self.column(winnerIndex))
        
    def row(self, index):
        return index / self.rows
    
    def column(self, index):
        return index % self.rows
    