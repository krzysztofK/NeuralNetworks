'''
Created on 02-11-2012

@author: Krzysztof
'''
from xml.dom.minidom import parse
from net_structure.node import Node, Bias, NeuronNode
from net_structure.layer import Layer
from net_parser.exception import ParseException
from net_structure.network import NeuralNetwork
from net_calculation.input_vector import InputVector

ROOT_NODE_NAME = 'neuralNet'
LAYER_NODE_NAME = 'layer'
NODE_NAME = 'node'
BIAS_NODE_NAME = 'bias'
LINK_NODE_NAME = 'link'
NODE_ID_ATTRUBUTE_NAME = 'id'
LINK_WEIGHT_ATTRIBUTE_NAME = 'weight'
ACTIVATION_ATTRIBUTE_NAME = 'activation'

INPUT_VECTOR_ROOT_NODE_NAME = 'inputVector'
VALUE_ATTRIBUTE_NAME = 'value'

class NetParser:
    '''
    classdocs
    '''


    def __init__(self, netFile):
        self.netFile = netFile
        
    def parse(self):
        net = parse(self.netFile)
        nodes = {}
        layers = []
        for element in net.getElementsByTagName(ROOT_NODE_NAME)[0].getElementsByTagName(LAYER_NODE_NAME):
            layerNodes = [NeuronNode(nodeElement.getAttribute(NODE_ID_ATTRUBUTE_NAME), self.parseLinks(nodeElement), nodeElement.getAttribute(ACTIVATION_ATTRIBUTE_NAME)) for nodeElement in element.getElementsByTagName(NODE_NAME)]
            layerNodes = layerNodes + [Bias(biasElement.getAttribute(NODE_ID_ATTRUBUTE_NAME), self.parseLinks(biasElement)) for biasElement in element.getElementsByTagName(BIAS_NODE_NAME)]
            for node in layerNodes :
                if not node.nodeId in nodes :
                    nodes[node.nodeId] = node
                else :
                    raise ParseException('Node identifier ' + node.nodeId + ' is not unique')
            layers.append(Layer(layerNodes))
        for layer in layers :
            for node in layer.nodes :
                node.updateLinks(nodes)
        return NeuralNetwork(layers)
    
    def parseLinks(self, node):
        return [(link.getAttribute(NODE_ID_ATTRUBUTE_NAME), float(link.getAttribute(LINK_WEIGHT_ATTRIBUTE_NAME)))  for link in node.getElementsByTagName(LINK_NODE_NAME)]

class InputVectorParser:
    def __init__(self, input_vector_file):
        self.input_vector_file = input_vector_file
        
    def parse(self):
        input_vector_xml = parse(self.input_vector_file)
        node_value_dict = {}
        for node_element in input_vector_xml.getElementsByTagName(INPUT_VECTOR_ROOT_NODE_NAME)[0].getElementsByTagName(NODE_NAME):
            node_value_dict[node_element.getAttribute(NODE_ID_ATTRUBUTE_NAME)] = node_element.getAttribute(VALUE_ATTRIBUTE_NAME)
        return InputVector(node_value_dict) 
        
        

if __name__ == "__main__":
    print(NetParser('../../resources/neuralNet.xml').parse())
    print(InputVectorParser('../../resources/inputVector.xml').parse())