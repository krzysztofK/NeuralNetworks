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
        conscience_coefficient = 1.0
        for i in range(1, 32000):
            reducer = pow(0.5, i/8000)
            network.learn(vector1, coefficient * reducer, conscience_coefficient * reducer)
            network.learn(vector2, coefficient * reducer, conscience_coefficient * reducer)
            network.learn(vector3, coefficient * reducer, conscience_coefficient * reducer)
            network.learn(vector4, coefficient * reducer, conscience_coefficient * reducer)
            if i % 8000 == 0:
                print(network)
        print(network.calculte_answer(vector1))
        print(network.calculte_answer(vector2))
        print(network.calculte_answer(vector3))
        print(network.calculte_answer(vector4))
        vector5 = InputVectorParser(COMMON_DIR_PREFIX+"input5.xml").parse()
        print(network.calculte_answer(vector5))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()