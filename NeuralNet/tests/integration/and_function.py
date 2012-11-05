'''
Created on 05-11-2012

@author: Tomasz
'''
import unittest
from net_parser.parser import InputVectorParser, NetParser
COMMON_DIR_PREFIX = '../../resources/integration_tests/'

def parseNetAndVector(net_name, vector_name):
        return (NetParser(COMMON_DIR_PREFIX+net_name).parse(), InputVectorParser(COMMON_DIR_PREFIX+vector_name).parse())

class AndFunctionIntegrationTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testWithLinearActivationFunction(self):
        net, vector = parseNetAndVector('network_AND_LIN.xml','input_0_0.xml')
        print(net.calculte_answer(vector))

    def testWithSigmoidActivationFunction(self):
        pass
    
    def testWithThresholdActivationFunction(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()