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