'''
Created on 26-11-2012

@author: Tomasz
'''
from net_parser.parser import InputVectorParser, NetParser
COMMON_DIR_PREFIX = '../../resources/kohonen_networks/'
import unittest

def parseNetAndVector(net_name, vector_name):
    return (NetParser(COMMON_DIR_PREFIX+net_name).parse(), InputVectorParser(COMMON_DIR_PREFIX+vector_name).parse())

class Test(unittest.TestCase):

    #TODO:
    #Add more tests

    def testSilly(self):
        network, vector = parseNetAndVector("kohonen_network_lab2.xml", "input1.xml")
        for i in range(1, 10):
            network.learn(vector, 0.5 / float(i), 0.2)
            print(network)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()