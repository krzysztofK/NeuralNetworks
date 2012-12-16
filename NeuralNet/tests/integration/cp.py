import unittest
from net_parser.parser import InputVectorParser, NetParser

COMMON_DIR_PREFIX = '../../resources/counter_propagation/'
LEARNING_VECTOR_FILE_PREFIX = 'input'
TEST_VECTOR_FILE_PREFIX = 'testInput'
NETWORK_FILE = 'counter_propagation_net.xml'
class Test(unittest.TestCase):

    #TODO:
    #Add more tests

    def testCP(self):
        inputVectors = [InputVectorParser(COMMON_DIR_PREFIX + LEARNING_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in range(1, 10)]
        testVectors = [InputVectorParser(COMMON_DIR_PREFIX + TEST_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in range(1, 4)]
        network = NetParser(COMMON_DIR_PREFIX + NETWORK_FILE).parse()
        coefficient = 0.05
        coefficient_half_life = 600
        grossberg_coefficient_half_life = 10000
        turns = 5000
        grossberg_coefficient = 0.4
        neighbourhoodWidth = 1
        network.cp_learning_process(inputVectors, coefficient, coefficient_half_life, turns, neighbourhoodWidth, grossberg_coefficient, grossberg_coefficient_half_life)

        inputVectors = [InputVectorParser(COMMON_DIR_PREFIX + LEARNING_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in range(1, 10)]
        for inputVector in inputVectors :
            self.printResult(network, inputVector)

        print('---------------------------------------------------------------------')
        
        for testVector in testVectors :
            self.printResult(network, testVector)
            
    def printResult(self, network, vector):
        vector.printVector(3)
        vector.normize()
        print(network.calculte_answer(vector))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
