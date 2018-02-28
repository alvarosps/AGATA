# -*- coding: utf-8 -*-

import json
import nltk
import re

class TextMining(object):
    def __init__(self, file_path, keywords):
        self._file_path = file_path
        self._keywords = keywords
        self._sentences = list()
        self._keyword_sentences = dict()
        
        self.lower_keywords()
        self.separete_file_sentences()
        
    def get_empty_keywords(self):
        keywords = list()
        for i in range(len(self._keywords)):
            if self._keywords[i] != "":
                keywords.append(self._keywords[i])
        self._keywords = keywords
    
    def lower_keywords(self):
        self.get_empty_keywords()
        for i in range(len(self._keywords)):
            self._keywords[i] = self._keywords[i].lower()
                
    def separete_file_sentences(self):
        with open(self._file_path, "r", encoding='utf-8') as text_file:
            file_text = text_file.read()
            sentences = nltk.tokenize.sent_tokenize(file_text)
                    
            for i in range(len(sentences)):
                if(len(sentences[i]) > 0):
                    self._sentences.append(sentences[i])
    
    def search_keywords_sentences(self, keyword):
        self._keyword_sentences[keyword] = []
        for sentence in self._sentences:
            if len( re.findall('\\b' + keyword + '\\b', sentence) ) > 0:
                self._keyword_sentences[keyword].append(sentence)
        
    
    def get_keywords_sentences(self):
        for keyword in self._keywords:
            self.search_keywords_sentences(keyword)
    
    
            
            