'''
Created on 05-11-2012

@author: Tomasz
'''
import argparse
import random
from net_parser.parser import NetParser, InputVectorParser
from net_calculation.input_vector_factory import RandomInputVectorFactory

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    input_vector_group = argument_parser.add_mutually_exclusive_group(required=True)
    input_vector_group.add_argument("--vector_file", help="xml file with input vector", type=open)
    input_vector_group.add_argument("--vector_limits", metavar=('LOWER', 'UPPER'), help="lower and upper limit for input values", nargs=2, type=float)
    argument_parser.add_argument("--network", help="xml file with neural network", type=open, required=True)
    link_weights_group = argument_parser.add_mutually_exclusive_group()
    link_weights_group.add_argument('--random', metavar=('LOWER', 'UPPER'), help="lower and upper limit for random link weights", nargs=2, type=float)
    link_weights_group.add_argument('--zeros', action="store_true")
    args = argument_parser.parse_args()
    weight_function = None
    if args.random:
        print('Weight of links between nodes will be set to random values from range [{}; {}]'.format(args.random[0], args.random[1]))
        weight_function = lambda : random.uniform(args.random[0], args.random[1])
    elif args.zeros:
        print('Weight of links between nodes will be set to 0.')
        weight_function = lambda : 0.0
    network = NetParser(args.network).parse(weight_function)
    if args.vector_limits:
        input_vector = RandomInputVectorFactory.create_new(args.vector_limits[0], args.vector_limits[1], network.layers[0].get_nodes_ids())
        print('Generated vector with values from range [{}; {}]:\n{}'.format(args.vector_limits[0], args.vector_limits[1], input_vector))
    else:
        input_vector = InputVectorParser(args.vector_file).parse()
    print('Network response is:')
    print(network.calculte_answer(input_vector))
    