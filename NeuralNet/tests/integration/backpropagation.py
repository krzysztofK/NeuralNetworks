'''
Created on 21-01-2013

@author: Tomasz
'''
import unittest
import random
from net_parser.parser import InputVectorParser, NetParser

COMMON_DIR_PREFIX = '../../resources/backpropagation/'
LEARNING_VECTOR_FILE_PREFIX = 'input'
TEST_VECTOR_FILE_PREFIX = 'testInput'
NETWORK_FILE = 'backpropagation_net.xml'
class Test(unittest.TestCase):

    def test_backpropagation(self):
        input_vectors = [InputVectorParser(COMMON_DIR_PREFIX + LEARNING_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in range(1, 4)]
        for input_vec in input_vectors:
            print(input_vec)
        #testVectors = [InputVectorParser(COMMON_DIR_PREFIX + TEST_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in range(1, 4)]
        network = NetParser(COMMON_DIR_PREFIX + NETWORK_FILE).parse(lambda : random.uniform(-1.0, 1.0))
        learning_rate = 0.04
        iterations = 5000
        network.backpropagation_learn(input_vectors, learning_rate, iterations)
        print(network)
        for inputVector in input_vectors :
            self.print_results(network, inputVector)

#        print('---------------------------------------------------------------------')
#        
#        for testVector in testVectors :
#            self.print_results(network, testVector)
            
    def print_results(self, network, vector):
        vector.printVector(3)
        vector.normize()
        print(network.calculte_answer(vector, True))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
