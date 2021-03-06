'''
Created on 02-11-2012

@author: Krzysztof
'''
from xml.dom.minidom import parse
from net_structure.node import Node, Bias, NeuronNode
from net_structure.layer import Layer, KohonenLayer, GrossbergLayer
from net_parser.exception import ParseException
from net_structure.network import NeuralNetwork
from net_calculation.input_vector import InputVector, LearningVector

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

KOHONEN_LAYER_NODE_NAME = 'KohonenLayer'
ROWS_ATTRIBUTE_NAME = 'rows'
COLUMNS_ATTRIBUTE_NAME = 'columns'
NEIGHBOURHOOD_ATTRIBUTE_NAME = 'neighbourhood'
NEIGHBOURHOOD_VALUE_1D = '1D'
NEIGHBOURHOOD_VALUE_2D = '2D'
CONSCIENCE_ATTRIBUTE_NAME = 'conscience'
CONSCIENCE_COEFF_ATTRIBUTE_NAME = 'conscience_coefficient'

GROSSBERG_LAYER_NODE_NAME = 'GrossbergLayer'
RESULT_NODE_NAME = 'result'

class NetParser:
    '''
    classdocs
    '''


    def __init__(self, netFile):
        self.netFile = netFile
        
    def parse(self, weightFunction=None):
        net = parse(self.netFile)
        nodes = {}
        layers = []
        rootElement = net.getElementsByTagName(ROOT_NODE_NAME)[0]
        conscience_coeff = None
        for element in rootElement.getElementsByTagName(LAYER_NODE_NAME) + rootElement.getElementsByTagName(KOHONEN_LAYER_NODE_NAME) + rootElement.getElementsByTagName(GROSSBERG_LAYER_NODE_NAME):
            layerNodes = [NeuronNode(nodeElement.getAttribute(NODE_ID_ATTRUBUTE_NAME),\
                                     self.parseLinks(nodeElement, weightFunction),\
                                     nodeElement.getAttribute(ACTIVATION_ATTRIBUTE_NAME))\
                          for nodeElement in element.getElementsByTagName(NODE_NAME)]
            biases = element.getElementsByTagName(BIAS_NODE_NAME)
            bias = Bias(biases[0].getAttribute(NODE_ID_ATTRUBUTE_NAME), self.parseLinks(biases[0], weightFunction))\
                        if biases is not None and len(biases) == 1\
                        else Bias('mock', [])
            for node in layerNodes :
                if not node.nodeId in nodes :
                    nodes[node.nodeId] = node
                else :
                    raise ParseException('Node identifier ' + node.nodeId + ' is not unique')
            networkType = element.tagName
            if networkType == KOHONEN_LAYER_NODE_NAME :
                neighbourhoodType = element.getAttribute(NEIGHBOURHOOD_ATTRIBUTE_NAME)
                conscience = True if element.getAttribute(CONSCIENCE_ATTRIBUTE_NAME) == 'true' else False
                conscience_coeff = float(element.getAttribute(CONSCIENCE_COEFF_ATTRIBUTE_NAME))
                rows = 1
                columns = len(layerNodes)
                if neighbourhoodType == NEIGHBOURHOOD_VALUE_1D :
                    pass
                elif neighbourhoodType == NEIGHBOURHOOD_VALUE_2D :
                    rows = int(element.getAttribute(ROWS_ATTRIBUTE_NAME))
                    columns = int(element.getAttribute(COLUMNS_ATTRIBUTE_NAME))
                layers.append(KohonenLayer(layerNodes, bias, neighbourhoodType, rows, columns, conscience))
            elif networkType == GROSSBERG_LAYER_NODE_NAME :
                layers.append(GrossbergLayer(layerNodes, bias))                
            else :
                layers.append(Layer(layerNodes, bias))
        for layer in layers :
            for node in layer.nodes :
                node.updateLinks(nodes)
            if layer.bias is not None:
                layer.bias.updateLinks(nodes)
        return NeuralNetwork(layers, conscience_coeff)
    
    def parseLinks(self, node, weightFunction=None):
        links = []
        for link in node.getElementsByTagName(LINK_NODE_NAME):
            if weightFunction is not None:
                weight = weightFunction()
            else:
                weight = float(link.getAttribute(LINK_WEIGHT_ATTRIBUTE_NAME))
            links.append((link.getAttribute(NODE_ID_ATTRUBUTE_NAME), weight))
        return links  

class InputVectorParser:
    def __init__(self, input_vector_file):
        self.input_vector_file = input_vector_file
        
    def parse(self):
        input_vector_xml = parse(self.input_vector_file)
        node_value_dict = {}
        for node_element in input_vector_xml.getElementsByTagName(INPUT_VECTOR_ROOT_NODE_NAME)[0].getElementsByTagName(NODE_NAME):
            node_value_dict[node_element.getAttribute(NODE_ID_ATTRUBUTE_NAME)] = float(node_element.getAttribute(VALUE_ATTRIBUTE_NAME))
            
        expected_value_dict = {}
        for node_element in input_vector_xml.getElementsByTagName(INPUT_VECTOR_ROOT_NODE_NAME)[0].getElementsByTagName(RESULT_NODE_NAME):
            expected_value_dict[node_element.getAttribute(NODE_ID_ATTRUBUTE_NAME)] = float(node_element.getAttribute(VALUE_ATTRIBUTE_NAME))
        if expected_value_dict :
            return LearningVector(node_value_dict, expected_value_dict)
        return InputVector(node_value_dict) 
             
if __name__ == "__main__":
    print(NetParser('../../resources/neuralNet.xml').parse())
    print(InputVectorParser('../../resources/inputVector.xml').parse())
    print(NetParser('../../resources/kohonen_networks/kohonen_network_lab2.xml').parse())
