# -*- coding: utf-8 -*-

from textMining.AIMLgenerator import AIMLgenerator
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import re

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

    def create_aiml_question(self, with_media):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TO NO CRATE AIML QUESTION")
        category = SubElement(self.aiml, "category")

        pattern = SubElement(category, "pattern")
        pattern.text = self.question

        template = SubElement(category, "template")

        if len(self.answers) > 1:
            random = SubElement(template, "random")

            for i in range(len(self.answers)):
                if self.answers[i] != "":
                    li = SubElement(random, "li")
                    if (with_media):
                        self.answers[i] = re.sub('<a.*</a>', '', self.answers[i])
                        li.text = re.sub('<[^<].*?>', '', self.answers[i])
                        print("WITH MEDIA")
                    else:
                        li.text = self.answers[i]
                        print("WITHOUT MEDIA")
        elif len(self.answers) == 1:
            if (with_media):
                self.answers[0] = re.sub('<a.*</a>', '', self.answers[0])
                template.text = re.sub('<[^<].*?>', '', self.answers[0])
                print("WITH MEDIA")
            else:
                template.text = self.answers[0]
            #template.text = self.answers[0]
