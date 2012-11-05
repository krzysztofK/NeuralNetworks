'''
Created on 05-11-2012

@author: Tomasz
'''
from net_parser.parser import NetParser, InputVectorParser
from net_structure.node import Node, Bias, NeuronNode
from net_structure.layer import Layer
from net_structure.link import Link
from net_structure.network import NeuralNetwork

if __name__ == '__main__':
    network = NetParser('../../resources/neuralNet.xml').parse()
    input_vector = InputVectorParser('../../resources/inputVector.xml').parse()
    print(network.calculte_answer(input_vector))
    