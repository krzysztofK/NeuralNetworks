'''
Created on 02-11-2012

@author: Krzysztof
'''

class ParseException(Exception):
    '''
    classdocs
    '''


    def __init__(self, description):
        self.description = description