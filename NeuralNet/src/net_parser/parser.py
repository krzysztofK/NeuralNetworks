'''
Created on 02-11-2012

@author: Krzysztof
'''
from xml.dom.minidom import parse
from net_structure.node import Node, Bias
from net_structure.layer import Layer
from net_parser.exception import ParseException
from net_structure.network import NeuralNetwork

ROOT_NODE_NAME = 'neuralNet'
LAYER_NODE_NAME = 'layer'
NODE_NAME = 'node'
BIAS_NODE_NAME = 'bias'
LINK_NODE_NAME = 'link'
NODE_ID_ATTRUBUTE_NAME = 'id'
LINK_WEIGHT_ATTRIBUTE_NAME = 'weight'
ACTIVATION_ATTRIBUTE_NAME = 'activation'
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
            layerNodes = [Node(nodeElement.getAttribute(NODE_ID_ATTRUBUTE_NAME), self.parseLinks(nodeElement)) for nodeElement in element.getElementsByTagName(NODE_NAME)]
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
        return [(link.getAttribute(NODE_ID_ATTRUBUTE_NAME), float(link.getAttribute(LINK_WEIGHT_ATTRIBUTE_NAME)), link.getAttribute(ACTIVATION_ATTRIBUTE_NAME))  for link in node.getElementsByTagName(LINK_NODE_NAME)]

if __name__ == "__main__":
    print(NetParser('../../resources/neuralNet.xml').parse())
