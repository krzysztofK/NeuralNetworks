'''
Created on 05-11-2012

@author: Tomasz
'''
import sys
import argparse
from net_parser.parser import NetParser, InputVectorParser
from net_structure.node import Node, Bias, NeuronNode
from net_structure.layer import Layer
from net_structure.link import Link
from net_structure.network import NeuralNetwork
from net_calculation.input_vector_factory import RandomInputVectorFactory

ARG_COMMENT = '''Please specify arguments properly:
python main.py network input_vector
where
network - xml file with neural network
input_vector - (optional) xml file with input vector
'''

def prompt_for_random_limits():
    print('The input vector file has not been specified. Input values will be generated randomly.')
    min_val = float(input('Lower limit for input values: '))
    max_val = float(input('Upper limit for input values: '))
    return min_val, max_val

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    input_vector_group = argument_parser.add_mutually_exclusive_group(required=True)
    input_vector_group.add_argument("--vector_file", help="xml file with input vector", type=open)
    input_vector_group.add_argument("--vector_limits", metavar=('LOWER', 'UPPER'), help="lower and upper limit for input values", nargs=2, type=float)
    argument_parser.add_argument("--network", help="xml file with neural network", type=open, required=True)
    args = argument_parser.parse_args()
    network = NetParser(args.network).parse()
    if(args.vector_limits):
        input_vector = RandomInputVectorFactory.create_new(args.vector_limits[0], args.vector_limits[1], network.layers[0].get_nodes_ids())
        print('Generated vector:\n{}'.format(input_vector))
    else:
        input_vector = InputVectorParser(args.vector_file).parse()
    print('Network response is:')
    print(network.calculte_answer(input_vector))
    