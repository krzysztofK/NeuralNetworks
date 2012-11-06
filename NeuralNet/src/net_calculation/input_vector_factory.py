'''
Created on 06-11-2012

@author: Tomasz
'''
import random
from net_calculation.input_vector import InputVector

class RandomInputVectorFactory:
    @staticmethod
    def create_new(min_val, max_val, node_names):
        node_values_dict = {}
        for node_name in node_names:
            node_values_dict[node_name] = random.uniform(min_val, max_val)
        return InputVector(node_values_dict)