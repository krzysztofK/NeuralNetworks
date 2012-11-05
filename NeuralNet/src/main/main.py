'''
Created on 05-11-2012

@author: Tomasz
'''
import sys
from net_parser.parser import NetParser, InputVectorParser
from net_structure.node import Node, Bias, NeuronNode
from net_structure.layer import Layer
from net_structure.link import Link
from net_structure.network import NeuralNetwork

ARG_COMMENT = '''Please specify arguments properly:
python main.py network input_vector
where
network - xml file with neural network
input_vector - (optional) xml file with input vector
'''

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2 or argc > 3:
        print(ARG_COMMENT)
        sys.exit(1)
    elif argc == 2:
        network = NetParser(sys.argv[1]).parse()
        input_vector = None
    elif argc == 3:
        network = NetParser(sys.argv[1]).parse()
        input_vector = InputVectorParser(sys.argv[2]).parse()
    print('Network response is:')
    print(network.calculte_answer(input_vector))
    