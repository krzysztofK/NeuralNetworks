import unittest
from net_parser.parser import InputVectorParser, NetParser

COMMON_DIR_PREFIX = '../../resources/counter_propagation_parity/'
LEARNING_VECTOR_FILE_PREFIX = 'input'
NETWORK_FILE = 'counter_propagation_parity_net.xml'
NETWORK_FILE_WITH_6INPUTS='counter_propagation_parity_net_6inputs.xml'

class Test(unittest.TestCase):

    #TODO:
    #Add more tests

    def executeTest(self, indexRange, networkFile):
        inputVectors = [InputVectorParser(COMMON_DIR_PREFIX + LEARNING_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in indexRange]
        network = NetParser(COMMON_DIR_PREFIX + networkFile).parse()
        coefficient = 0.8
        coefficient_half_life = 1000
        grossberg_coefficient_half_life = 12000
        turns = 5000
        grossberg_coefficient = 0.4
        neighbourhoodWidth = 1
        network.cp_learning_process(inputVectors, coefficient, coefficient_half_life, turns, neighbourhoodWidth, grossberg_coefficient, grossberg_coefficient_half_life)

        inputVectors = [InputVectorParser(COMMON_DIR_PREFIX + LEARNING_VECTOR_FILE_PREFIX + str(i) + '.xml').parse() for i in range(1, 9)]
        for inputVector in inputVectors :
            self.printResult(network, inputVector)
            
    def printResult(self, network, vector):
        vector.printVector(3)
        vector.normize()
        print(network.calculte_answer(vector))

    def testCP(self):
        self.executeTest(range(1,9), NETWORK_FILE)
    
#    def testCPGenerlization(self):
#        indexRange = list(range(1, 9))
#        indexRange.remove(2)
#        indexRange.remove(5)
#        print(indexRange)
#        self.executeTest(indexRange, NETWORK_FILE)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
