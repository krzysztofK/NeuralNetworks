'''
Created on 05-11-2012

@author: Tomasz
'''
import unittest
from net_parser.parser import NetParser, InputVectorParser

COMMON_DIR_PREFIX = '../../resources/integration_tests/'
TOLLERANCE = 0.05

class XorFunctionIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.networkFile = 'network_XOR_SIG.xml'
        self.network = NetParser(COMMON_DIR_PREFIX + self.networkFile).parse()
        

    def tearDown(self):
        pass


    def testWithSigmoidActivationFunction(self):
        input_vector = InputVectorParser(COMMON_DIR_PREFIX + 'input_0_0.xml').parse()
        value = self.network.calculte_answer(input_vector)
        print('f(0,0) = ', str(self.network.calculte_answer(input_vector)))
        self.assertAlmostEqual(0, value[0], 1)

        input_vector = InputVectorParser(COMMON_DIR_PREFIX + 'input_1_0.xml').parse()
        value = self.network.calculte_answer(input_vector)
        print('f(1,0) = ', str(self.network.calculte_answer(input_vector)))
        self.assertAlmostEqual(1, value[0], 1)

        input_vector = InputVectorParser(COMMON_DIR_PREFIX + 'input_0_1.xml').parse()
        value = self.network.calculte_answer(input_vector)
        print('f(0,1) = ', str(self.network.calculte_answer(input_vector)))
        self.assertAlmostEqual(1, value[0], 1)

        input_vector = InputVectorParser(COMMON_DIR_PREFIX + 'input_1_1.xml').parse()
        value = self.network.calculte_answer(input_vector)
        print('f(1,1) = ', str(self.network.calculte_answer(input_vector)))
        self.assertAlmostEqual(0, value[0], 1)
        
    def testWithThresholdActivationFunction(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
