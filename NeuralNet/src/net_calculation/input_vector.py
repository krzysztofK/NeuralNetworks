'''
Created on 05-11-2012

@author: Tomasz
'''

class InputVector:
    '''
    classdocs
    '''

    def __init__(self, node_value_dict):
        self.__node_value_dict = node_value_dict
        
    def get_value_for_node(self, node_id):
        return self.__node_value_dict[node_id]
    
    def __str__(self):
        result = ''
        for node, value in self.__node_value_dict.items():
            result += 'Node {} has value {}\n'.format(node, value)
        return result
        