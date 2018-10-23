# -*- coding: utf-8 -*-

from textMining.AIMLanswers import AIMLanswers
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

class AIMLquestions(AIMLanswers):
    #This class is only to be used if there's more than one question, for one question and many answers,
    #use AIMLanswers. The pre-defined category fits here

    #removed_phrases = ["FALE SOBRE O #", "O QUE SE PODE FAZER COM O #", "O QUE É O #", "O QUE FAZ O #"]
    pre_defined_phrases = ["#", "* #", "* # *", "# *", "FALE SOBRE #", "DEFINA #", "O QUE É #", "PARA QUE SERVE #", "O QUE * #", "COMO * #"]

    def __init__(self, structure, typeOfAIML):
        '''
            structure = {
                "keywords" : [],
                "sentences" : [],
                "extra" : [],
        '''
        super().__init__(structure)
        self.typeOfAIML = typeOfAIML
        self.questions = self.get_questions()

    def get_questions(self):
        questions = list()

        if self.typeOfAIML == "pre_defined":
            print("pegando questoes")
            print(len(self._structure["keywords"]))
            for i in range(len(self._structure["keywords"])):
                if i == 0:
                    pre_defined_phrases_keyword = self.replace_keywords(self._structure["keywords"][i], firstKeyword=True)
                else:
                    pre_defined_phrases_keyword = self.replace_keywords(self._structure["keywords"][i])
                for j in range(len(pre_defined_phrases_keyword)):
                    questions.append(pre_defined_phrases_keyword[j])


            related_keywords = self._structure["extra"].split(";")

            # correção do bug e-mail 22/7: coloquei esse if pq o split retornava uma lista com um item
            if related_keywords != ['']:
                print("pegando questoes extras")
                print(len(related_keywords))

                for i in range(len(related_keywords)):
                    pre_defined_phrases_keyword = self.replace_keywords(related_keywords[i])
                    for j in range(len(pre_defined_phrases_keyword)):
                        questions.append(pre_defined_phrases_keyword[j])

        print (questions)
        return questions

    def create_aiml_questions(self):
        #only if len(questions) > 1
        #criando as questoes para as palavras-chave normais
        print("normais de tamanho ")
        print(len(self.questions))
        for i in range(0, len(self.questions)):
            category = SubElement(self.aiml, "category")

            pattern = SubElement(category, "pattern")
            pattern.text = self.questions[i]

            template = SubElement(category, "template")

            srai = SubElement(template, "srai")
            srai.text = self.question
            print (pattern.text)

        #criando as questoes para as palavras-chave extras
        print("extra")
        print(self._structure["extra"])

        if self._structure["extra"] != "":
            related_keywords = self._structure["extra"].split(";")
            for i in range(0, len(related_keywords)):
                if related_keywords[i] != "":
                    category = SubElement(self.aiml, "category")

                    pattern = SubElement(category, "pattern")
                    pattern.text = related_keywords[i]

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

    def create_aiml(self, with_media):
        print("to no aiml questions criando o aiml")
        print(self._structure["keywords"])
        #Begin the AIML, and Comment
        self.begin_aiml()
        #Root Question with one or many answers
        self.create_aiml_question(with_media)
        #Questions SRAI
        self.create_aiml_questions()
        print(self._structure["keywords"])
        return self.aiml
