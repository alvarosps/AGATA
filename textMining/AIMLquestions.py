#coding: utf-8
from textMining.AIMLanswers import AIMLanswers
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

class AIMLquestions(AIMLanswers):
    #This class is only to be used if there's more than one question, for one question and many answers,
    #use AIMLanswers. The pre-defined category fits here
    
    #removed_phrases = ["FALE SOBRE O #", "O QUE SE PODE FAZER COM O #", "O QUE É O #", "O QUE FAZ O #"]
    pre_defined_phrases = ["FALE SOBRE #",  "#", "O QUE FAZ #", "O QUE O # FAZ", 
                           "* #", "# *", "* # *", "O QUE SE PODE FAZER COM #",
                           "O QUE É #", "DEFINA #"]
    
    def __init__(self, structure, typeOfAIML):
        '''
            structure = {
                "keywords" : [],
                "sentences" : [],
        '''
        super().__init__(structure)
        self.typeOfAIML = typeOfAIML
        self.questions = self.get_questions()
        
    def get_questions(self):
        questions = list()
        
        if self.typeOfAIML == "pre_defined":
            for i in range(len(self._structure["keywords"])):
                if i == 0:
                    pre_defined_phrases_keyword = self.replace_keywords(self._structure["keywords"][i], firstKeyword=True)
                else:
                    pre_defined_phrases_keyword = self.replace_keywords(self._structure["keywords"][i])
                for j in range(len(pre_defined_phrases_keyword)):
                    questions.append(pre_defined_phrases_keyword[j])
            
        
        return questions
    
    def create_aiml_questions(self):
        #only if len(questions) > 1
        for i in range(1, len(self.questions)):
            category = SubElement(self.aiml, "category")
            
            pattern = SubElement(category, "pattern")
            pattern.text = self.questions[i]
            
            template = SubElement(category, "template")
            
            srai = SubElement(template, "srai")
            srai.text = self.question
    
    def replace_keywords(self, keyword, firstKeyword = False):
        new_pre_defined_phrases = list()
        for i in range(len(self.pre_defined_phrases)):
            if firstKeyword == True:
                if self.pre_defined_phrases[i] != "#":
                    new_pre_defined_phrases.append(self.pre_defined_phrases[i].replace("#", keyword))
            else:
                new_pre_defined_phrases.append(self.pre_defined_phrases[i].replace("#", keyword))
        
        return new_pre_defined_phrases
    
    def create_aiml(self):
        #Begin the AIML, and Comment
        self.begin_aiml()
        #Root Question with one or many answers
        self.create_aiml_question()
        #Questions SRAI
        self.create_aiml_questions()
        
        return self.aiml
        
        