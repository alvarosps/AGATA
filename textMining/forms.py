from django import forms


class FormKeywords(forms.Form):
    keyword_1 = forms.CharField(label = "Palavra-chave 1: *", max_length = 100)
    keyword_2 = forms.CharField(label = "Palavra-chave 2:", max_length = 100, required=False)
    keyword_3 = forms.CharField(label = "Palavra-chave 3:", max_length = 100, required=False)
    #book = forms.FileField(label= "Livro-Texto (formato .txt) *")
