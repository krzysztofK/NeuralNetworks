'''
Created on 04-11-2012

@author: Krzysztof
'''
import math

class ActivationFunctionFactory:
    @staticmethod
    def get_activation_function(name):
        if name == 'threshold':
            return ThresholdFunction()
        elif name == 'sigmoid':
            return SigmoidFunction()
        else: #name == 'linear':
            return LinearFunction()
        
        

class ActivationFunction:        
    def calculate_value(self, input_value):
        pass
    
class LinearFunction(ActivationFunction):
    def calculate_value(self, input_value):
        return input_value
    
class ThresholdFunction(ActivationFunction):
    def calculate_value(self, input_value):
        return 0.0 if input_value < 0.0 else 1.0 
    
class SigmoidFunction(ActivationFunction):
    def calculate_value(self, input_value):
        return 1.0 / (1.0 + math.exp(-input_value))