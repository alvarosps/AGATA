# -*- coding: utf-8 -*-


from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree

class AIMLgenerator(object):
    def __init__(self, structure):
        '''
            structure = {
                "keywords" : [],
                "sentences" : [],
        '''
        self._structure = structure
        self.aiml = Element('aiml')
    
    def begin_aiml(self):        
        self.aiml.attrib["version"] = "3.0"
        self.aiml.attrib["encoding"] = "UTF-8"
        
        comment = Comment(     "Copyright 2018 - AGATA\n" +
                        "URL: http://agata.pgie.ufrgs.br\n" +
                        "Powered by\n" +
                        "Aliane Loureiro Krassmann < alkrassmann at gmail.com >\n" +
                        "João Marcos Flach < joaoflach at gmail.com >\n" +
                        "Project coordinator: Liane Margarida Rockenbach Tarouco < liane at penta.ufrgs.br >"
        )
        self.aiml.append(comment)
        
    
    def save_aiml(self, root):
        tree = ElementTree(root)
        
        return tree
        
