'''
Created on 26-11-2012

@author: Tomasz
'''
from net_parser.parser import InputVectorParser, NetParser
COMMON_DIR_PREFIX = '../../resources/kohonen_networks/'
import unittest

class Test(unittest.TestCase):

    #TODO:
    #Add more tests

    def testSilly(self):
        network = NetParser(COMMON_DIR_PREFIX+"kohonen_network_lab2.xml").parse()
        vector1 = InputVectorParser(COMMON_DIR_PREFIX+"input1.xml").parse()
        vector2 = InputVectorParser(COMMON_DIR_PREFIX+"input2.xml").parse()
        vector3 = InputVectorParser(COMMON_DIR_PREFIX+"input3.xml").parse()
        vector4 = InputVectorParser(COMMON_DIR_PREFIX+"input4.xml").parse()
        coefficient = 0.12
        conscience_coefficient = 0.0
        for i in range(1, 32000):
            reducer = pow(0.5, i/8000)
            network.learn(vector1, coefficient * reducer, conscience_coefficient * reducer,1)
            network.learn(vector2, coefficient * reducer, conscience_coefficient * reducer,1)
            network.learn(vector3, coefficient * reducer, conscience_coefficient * reducer,1)
            network.learn(vector4, coefficient * reducer, conscience_coefficient * reducer,1)
            if i % 8000 == 0:
                print(network)
                
        self.printResult(network, vector1)
        self.printResult(network, vector2)
        self.printResult(network, vector3)
        self.printResult(network, vector4)
        vector5 = InputVectorParser(COMMON_DIR_PREFIX+"input5.xml").parse()
        self.printResult(network, vector5)
        
    def printResult(self, network, vector):
        vector.printVector(3)
        print(network.calculte_answer(vector))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()