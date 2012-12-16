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
    
    def printVector(self, columnSize):
        count = 0
        for node in sorted(self.__node_value_dict.keys()) :
            print(self.get_value_for_node(node), end='')
            count = count + 1
            if count == columnSize :
                count = 0
                print('')

class LearningVector(InputVector):
    
    def __init__(self, node_value_dict, expected_value_dict):
        InputVector.__init__(self, node_value_dict)
        self.expected_value_dict = expected_value_dict
