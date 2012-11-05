'''
Created on 02-11-2012

@author: Krzysztof
'''
from net_structure.link import Link
from net_parser.exception import ParseException
from net_structure.activation_function import ActivationFunction

class Node:
    '''
    classdocs
    '''

    def __init__(self, nodeId, links):
        self.nodeId = nodeId
        self.links = links
    
    def updateLinks(self, nodes):
        try :
            self.links = [Link(nodes[nodeId], weight) for (nodeId, weight) in self.links]
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
        self.__value = value
        
    def add_to_current_value(self, value_to_add):
        self.__value += value_to_add

class Bias(Node):
    pass


class NeuronNode(Node) :
    
    def __init__(self, nodeId, links, activationFunction):
        Node.__init__(self, nodeId, links)
        self.activationFunction = ActivationFunction(activationFunction)        
    
    def __str__(self):
        return self.activationFunction.function + '-' + Node.__str__(self)