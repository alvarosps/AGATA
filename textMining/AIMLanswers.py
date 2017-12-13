#coding: utf-8
from textMining.AIMLgenerator import AIMLgenerator
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

class AIMLanswers(AIMLgenerator):
    
    def __init__(self, structure):
        '''
            structure = {
                "keywords" : [],
                "sentences" : [],
        '''
        super().__init__(structure)
        self.question = self.get_root_question()
        self.answers = self.get_answers()
    
    def get_root_question(self):
        return self._structure["keywords"][0]

    def get_answers(self):
        return self._structure["sentences"]
    
    def create_aiml_question(self):
        category = SubElement(self.aiml, "category")
        
        pattern = SubElement(category, "pattern")
        pattern.text = self.question
        
        template = SubElement(category, "template")
        
        if len(self.answers) > 1:
            random = SubElement(template, "random")
            
            for i in range(len(self.answers)):
                li = SubElement(random, "li")
                li.text = self.answers[i]
        elif len(self.answers) == 1:
            template.text = self.answers[0]
        
        