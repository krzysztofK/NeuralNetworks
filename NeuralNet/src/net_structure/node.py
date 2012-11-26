'''
Created on 02-11-2012

@author: Krzysztof
'''
from net_structure.link import Link
from net_parser.exception import ParseException
from net_structure.activation_function import ActivationFunctionFactory

class Node:
    '''
    classdocs
    '''

    def __init__(self, nodeId, links):
        self.nodeId = nodeId
        self.links = links
        self.backward_links = []
    
    def updateLinks(self, nodes):
        try :
            temp_links = []
            for (nodeId, weight) in self.links:
                link = Link(self, nodes[nodeId], weight)
                temp_links.append(link)
                nodes[nodeId].backward_links.append(link)
            self.links = temp_links
        except :
            raise ParseException('There is no node with specified identifier')
        
    def __str__(self):
        result = '\t-node ' + self.nodeId +'\n'
        for link in self.links :
            result = result + str(link)
        return result
    
    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = float(value)
    
    def clear_value(self):
        self.__value = 0.0
        
    def add_to_current_value(self, value_to_add):
        self.__value += value_to_add
        
    def propagate(self):
        postActivationValue = self.get_value()
        for link in self.links:
            link.to_node.add_to_current_value(postActivationValue * link.weight)

class Bias(Node):
    def get_value(self):
        return 1.0


class NeuronNode(Node) :
    
    def __init__(self, nodeId, links, activationFunction):
        Node.__init__(self, nodeId, links)
        self.activationFunction = ActivationFunctionFactory.get_activation_function(activationFunction)        
    
    def __str__(self):
        return self.activationFunction.__class__.__name__ + '-' + Node.__str__(self)
    
    def get_value(self):
        return self.activationFunction.calculate_value(super(NeuronNode, self).get_value())