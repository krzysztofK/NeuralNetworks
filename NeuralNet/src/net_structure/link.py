'''
Created on 02-11-2012

@author: Krzysztof
'''

class Link:
    '''
    classdocs
    '''


    def __init__(self, node, weight):
        self.weight = weight
        self.node = node

    def __str__(self):
        return '\t\t-link(' + str(self.weight) + ') to ' + self.node.nodeId + '\n'