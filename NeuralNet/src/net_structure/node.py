'''
Created on 02-11-2012

@author: Krzysztof
'''
from net_structure.link import Link
from net_parser.exception import ParseException

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

class Bias(Node):
    pass
