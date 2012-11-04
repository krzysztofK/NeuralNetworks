'''
Created on 02-11-2012

@author: Krzysztof
'''

class Link:
    '''
    classdocs
    '''


    def __init__(self, node, weight, activationFunction):
        self.weight = weight
        self.node = node
        self.activationFunction = activationFunction

    def __str__(self):
        return '\t\t-link ' + self.activationFunction.function + '(' + str(self.weight) + ') to ' + self.node.nodeId + '\n' 