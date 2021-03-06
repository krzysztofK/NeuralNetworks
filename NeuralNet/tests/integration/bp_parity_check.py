import unittest
import random
from net_parser.parser import InputVectorParser, NetParser

COMMON_DIR_PREFIX = '../../resources/back_propagation/'
LEARNING_VECTOR_FILE_PREFIX = 'input'
NETWORK_FILE = 'parity_check_bp_network.xml'

class Test(unittest.TestCase):

    #TODO:
    #Add more tests

    def executeTest(self, indexRange, networkFile):
        inputVectors = [InputVectorParser(COMMON_DIR_PREFIX + LEARNING_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in indexRange]
        network = NetParser(COMMON_DIR_PREFIX + networkFile).parse(lambda : random.uniform(-1.0, 1.0))
        speed = 0.5
        momentum = 0.15
        iterations = 5000

        network.backpropagation_learn(inputVectors, speed, iterations, momentum)

        inputVectors = [InputVectorParser(COMMON_DIR_PREFIX + LEARNING_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in range(1, 9)]
        for inputVector in inputVectors :
            self.printResult(network, inputVector)

    def printResult(self, network, vector):
        vector.printVector(3)
        print(network.calculte_answer(vector))

    def testGP(self):
        self.executeTest(range(1,9), NETWORK_FILE)

if __name__ == "__main__":
    unittest.main()
