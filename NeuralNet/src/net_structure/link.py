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