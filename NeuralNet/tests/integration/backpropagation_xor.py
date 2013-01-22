'''
Created on 21-01-2013

@author: Tomasz
'''
import unittest
import random
from net_parser.parser import InputVectorParser, NetParser

COMMON_DIR_PREFIX = '../../resources/backpropagation_xor/'
LEARNING_VECTOR_FILE_PREFIX = 'input'
TEST_VECTOR_FILE_PREFIX = 'testInput'
NETWORK_FILE = 'backpropagation_net.xml'
class Test(unittest.TestCase):

    def test_backpropagation(self):
        input_vectors = [InputVectorParser(COMMON_DIR_PREFIX + LEARNING_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in range(1, 5)]
        for input_vec in input_vectors:
            print(input_vec)
        #testVectors = [InputVectorParser(COMMON_DIR_PREFIX + TEST_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in range(1, 4)]
        network = NetParser(COMMON_DIR_PREFIX + NETWORK_FILE).parse()#lambda : random.uniform(-1.0, 1.0))
        learning_rate = 0.7
        momentum = 0.1
        iterations = 2000
        network.backpropagation_learn(input_vectors, learning_rate, iterations, momentum)
        print(network)
        error = 0.0
        for inputVector in input_vectors :
            inputVector.printVector(3)
            outputDict = []
            answer = network.calculte_answer(inputVector, False, outputDict)
            print(answer)
            for id, val in outputDict:
                error = error + 0.5*(inputVector.expected_value_dict[id]-val)**2
        print(error)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
