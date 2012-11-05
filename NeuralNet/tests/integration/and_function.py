'''
Created on 05-11-2012

@author: Tomasz
'''
import unittest
from net_parser.parser import InputVectorParser, NetParser
COMMON_DIR_PREFIX = '../../resources/integration_tests/'

def parseNetAndVector(net_name, vector_name):
    return (NetParser(COMMON_DIR_PREFIX+net_name).parse(), InputVectorParser(COMMON_DIR_PREFIX+vector_name).parse())
    
def calculateAndReturnValue(net, vector):
    value = net.calculte_answer(vector)[0]
    print(value)
    return value

def getNetworkResponse(net_name, vector_name):
    n, v = parseNetAndVector(net_name,vector_name)
    return calculateAndReturnValue(n, v)
    
class AndFunctionIntegrationTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testWithLinearActivationFunction(self):
        self.assertAlmostEqual(-0.25, getNetworkResponse('network_AND_LIN.xml','input_0_0.xml'), 3)
        self.assertAlmostEqual(0.25, getNetworkResponse('network_AND_LIN.xml','input_0_1.xml'), 3)
        self.assertAlmostEqual(0.25, getNetworkResponse('network_AND_LIN.xml','input_1_0.xml'), 3)
        self.assertAlmostEqual(0.75, getNetworkResponse('network_AND_LIN.xml','input_1_1.xml'), 3)

    def testWithSigmoidActivationFunction(self):
        self.assertAlmostEqual(0, getNetworkResponse('network_AND_SIG.xml','input_0_0.xml'), 1)
        self.assertAlmostEqual(0, getNetworkResponse('network_AND_SIG.xml','input_0_1.xml'), 1)
        self.assertAlmostEqual(0, getNetworkResponse('network_AND_SIG.xml','input_1_0.xml'), 1)
        self.assertAlmostEqual(1, getNetworkResponse('network_AND_SIG.xml','input_1_1.xml'), 1)
    
    def testWithThresholdActivationFunction(self):
        self.assertAlmostEqual(0, getNetworkResponse('network_AND_THRESHOLD.xml','input_0_0.xml'), 3)
        self.assertAlmostEqual(0, getNetworkResponse('network_AND_THRESHOLD.xml','input_0_1.xml'), 3)
        self.assertAlmostEqual(0, getNetworkResponse('network_AND_THRESHOLD.xml','input_1_0.xml'), 3)
        self.assertAlmostEqual(1, getNetworkResponse('network_AND_THRESHOLD.xml','input_1_1.xml'), 3)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()