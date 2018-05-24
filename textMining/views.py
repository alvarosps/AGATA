# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from xml.etree.ElementTree import tostring
from xml.etree import ElementTree
from bs4 import BeautifulSoup
from xml.dom import minidom
from textMining.forms import FormKeywords
from textMining.TextMining import TextMining

import time
import os
import json
from textMining.AIMLquestions import AIMLquestions
import re

def index(request):
    return render(request, 'textMining/index.html')

def tutorial(request):
    return render(request, 'textMining/tutorial.html')

def aiml(request):
    forms = FormKeywords()

    return render(request, 'textMining/aiml.html', {'form': forms})

def select_text(request):
    book_file = request.FILES['book']
    fs = FileSystemStorage()
    file_name = fs.save(book_file.name, book_file)
    uploaded_file_url = fs.url(file_name)
    print(uploaded_file_url)

    keywords = [
        request.POST['keyword_1'],
        request.POST['keyword_2'],
        request.POST['keyword_3'],
    ]

    blank_optional_keywords = {
        'keyword_2' : False,
        'keyword_3' : False
    }

    if keywords[1] == "":
        blank_optional_keywords['keyword_2'] = True
    if keywords[2] == "":
        blank_optional_keywords['keyword_3'] = True

    request.session["blank_optional_keywords"] = blank_optional_keywords

    file_name = "LivroMA4_P1_formatado(1).txt"

    #file_path = get_file_path(file_name, 'text')

    file_path = get_file_path(uploaded_file_url, 'upload')

    text_mining = TextMining(file_path, keywords)
    text_mining.get_keywords_sentences()

    sentences = text_mining._keyword_sentences

    sentences_info = generate_sentences_info(sentences)

    request.session["sentences_info"] = sentences_info

    return render(request, 'textMining/selecttext.html', {'sentences_info': sentences_info})

def edit_text(request):

    sentences_info = request.session["sentences_info"]
    keywords_sentences = [
        request.POST.getlist('keyword0')
    ]

    if request.session["blank_optional_keywords"]["keyword_2"] == False:
        keywords_sentences.append(request.POST.getlist('keyword1'))
    if request.session["blank_optional_keywords"]["keyword_3"] == False:
        keywords_sentences.append(request.POST.getlist('keyword2'))

    final_sentences_info = generate_final_sentences_info(sentences_info, keywords_sentences)

    request.session["final_sentences_info"] = final_sentences_info

    #print (final_sentences_info)
    theres_sentences = False

    for info in final_sentences_info:
        #print (info["sentences"])
        if (info["sentences"] != []):
            theres_sentences = True


    return render(request, 'textMining/edittext.html', {'final_sentences_info' : final_sentences_info, 'theres_sentences' : theres_sentences})

def generate_aiml(request):
    final_sentences_info = request.session["final_sentences_info"]

    print("vai gerar o aiml")

    print(request.session["final_sentences_info"])

    print("<<<<<<<<<")
    keywords = get_keywords(final_sentences_info)

    sentences_ids = get_final_sentences_ids(final_sentences_info)
    keyword_sentences = list()
    for i in range(len(sentences_ids)):
        keyword_sentences.append( request.POST[sentences_ids[i]] )

    typeOfAIML = request.POST["typeOfAIML"]

    relatedKeywords = request.POST["relatedKeywords"]

    user_file_name = request.POST["fileName"]

    final_info = {
        "keywords" : keywords,
        "sentences" : keyword_sentences,
        "extra" : relatedKeywords
    }

    
    AIMLGenerator = AIMLquestions(final_info, typeOfAIML)

    print("to no view mandando criar o aiml")
    print(final_info["extra"])
    aiml = AIMLGenerator.create_aiml()
    aimlTree = AIMLGenerator.save_aiml(aiml)

    if user_file_name != "":
        if user_file_name.endswith(".xml"):
            download_file_name = user_file_name
        else:
            download_file_name = user_file_name + ".xml"
    else:
        download_file_name = 'aiml-' + time.strftime("%d-%m-%Y-%H-%M-%S") + '.xml'

    download_file_path = get_file_path(download_file_name, "xml")
    aimlTree.write(download_file_path, encoding="utf-8", xml_declaration=True)

    with open(download_file_path, 'r', encoding='utf-8') as xml:
        aiml_str = xml.read()

    #needs to pretty print
    bs = BeautifulSoup(open(download_file_path, 'r', encoding='utf-8'), 'xml')
    aiml_str = bs.prettify(encoding='utf-8')

    aiml = aiml_str.decode('utf-8')
    text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
    pretty_aiml = text_re.sub('>\g<1></', aiml)

    with open(download_file_path, 'w', encoding='utf-8') as f:
        f.write(pretty_aiml)

    with open(download_file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/xml")
        if request.POST['aimlOption'] == 'save':
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(download_file_path)
        if request.POST['aimlOption'] == 'show':
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_file_path)

    #return render(request, 'textMining/generateaiml.html', {'aiml_str' : aiml_str.decode('utf-8'), 'download_file_path' : download_file_path})
    return response

def get_file_path(file_name, typeOfFile):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if typeOfFile == 'text':
        file_folder = "\\texts\\"
        return ( dir_path + file_folder + file_name )
    elif typeOfFile == 'xml':
        file_folder = "\\aimls\\"
        #return os.path.abspath(os.path.join(dir_path, os.pardir)) + '\\media\\' + file_name #localserver(windows)
        return os.path.abspath(os.path.join(dir_path, os.pardir)) + '/media/' + file_name #server(linux)
        #return '/home/metis/public_html/media/' + file_name #server
    elif typeOfFile == 'upload':
        file_name = file_name[len('/media/'):]
        #return os.path.abspath(os.path.join(dir_path, os.pardir)) + '\\media\\' + file_name #localserver(windows)
        return os.path.abspath(os.path.join(dir_path, os.pardir)) + '/media/' + file_name #server(linux)
        #return '/home/metis/public_html/media/' + file_name #server


def generate_sentences_info(sentences):
    keywords = list()
    for key in sentences.keys():
        keywords.append(key)

    sentences_info = list()

    '''

    sentences_info = [
        {
            "keyword": "",
            "keyword_id" : "",
            "sentences": [
                {
                    "sentence_id": "",
                    "sentence": ""
                },
                ...
            ],
            ...
        },
        ...
    ]

    '''
    sentence_id = 0
    for i in range(len(keywords)):
        aux_sentence_info = dict()

        aux_sentence_info["keyword"] = keywords[i]
        aux_sentence_info["keyword_id"] = "keyword" + str(i)
        aux_keyword_sentences = list()
        for j in range(len(sentences[keywords[i]])):
            aux_sentences = dict()
            aux_sentences["sentence_id"] = "sentence" + str( sentence_id )
            #aux_sentences["sentence"] = sentences[keywords[i]][j] + " lalala"

            aux_sentences["sentence"] = re.sub(keywords[i], "<b><font color=\"green\">" + keywords[i] + "</font></b>", sentences[keywords[i]][j])

            aux_keyword_sentences.append(aux_sentences)

            sentence_id += 1

        aux_sentence_info["sentences"] = aux_keyword_sentences

        sentences_info.append(aux_sentence_info)

    return sentences_info

def generate_final_sentences_info(sentences_info, keywords_sentences):
    final_sentences_info = list()

    '''
    only the sentences selected
    final_sentences_info = [
        {
            "keyword": "",
            "keyword_id" : "",
            "sentences": [
                {
                    "sentence_id": "",
                    "sentence": ""
                },
                ...
            ],
            ...
        },
        ...
    ]

    '''

    if len(keywords_sentences) == 1:

        final_sentences_info.append( relate_keyword_datas(0, sentences_info[0], keywords_sentences) )

    elif len(keywords_sentences) == 2:
        #keyword0 and keyword1

        final_sentences_info.append( relate_keyword_datas(0, sentences_info[0], keywords_sentences) )

        final_sentences_info.append( relate_keyword_datas(1, sentences_info[1], keywords_sentences) )

    else:
        #keyword0 and keyword1 and keyword2

        final_sentences_info.append( relate_keyword_datas(0, sentences_info[0], keywords_sentences) )

        final_sentences_info.append( relate_keyword_datas(1, sentences_info[1], keywords_sentences) )

        final_sentences_info.append( relate_keyword_datas(2, sentences_info[2], keywords_sentences) )

    return final_sentences_info

def relate_keyword_datas(index, keyword_data, keywords_sentences):
    new_sentences_info = dict()
    new_sentences_info["keyword"] = keyword_data["keyword"]
    new_sentences_info["keyword_id"] = keyword_data["keyword_id"]
    new_sentences_info["sentences"] = list()

    for i in range(len(keyword_data["sentences"])):
        if keyword_data["sentences"][i]["sentence_id"] in keywords_sentences[index]:
            new_sentences_info["sentences"].append(keyword_data["sentences"][i])

    return new_sentences_info

def get_final_sentences_ids(final_sentences_info):
    sentences_id = list()
    for i in range(len(final_sentences_info)):
        for j in range(len(final_sentences_info[i]["sentences"])):
            sentences_id.append(final_sentences_info[i]["sentences"][j]["sentence_id"])

    return sentences_id

def get_keywords(final_sentences_info):
    keywords = list()
    for i in range(len(final_sentences_info)):
        keywords.append(final_sentences_info[i]["keyword"])

    return keywords

def about(request):
    return render(request, 'textMining/sobre.html')
