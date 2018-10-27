#Imports
from bs4 import BeautifulSoup as bs # process html
from requests import get # to request page url code

'''
File to get definition data without glitchy definition api

gets word definition and type of word exp:'Noun'
'''

class DefinitionFind:
    def __init__(self, query):
        self.query = query
        url = ('https://www.dictionary.com/browse/' + self.query + '?s=t')# combine url with search query from command
        r = get(url) # request page
        page = r.text # formatting
        self.soup = bs(page, 'html.parser') # parse html

    def scrapeDefinition(self):
        try:
            define_find_type = self.soup.findAll('span', attrs={'class':'luna-pos'})
            define_find = self.soup.findAll('span', attrs={'class':'css-9sn2pa e10vl5dg6'})
            if define_find == []: raise Exception
            if define_find_type == []: raise Exception
            definition_type = define_find_type[0].getText()
            definition = define_find[0].getText()
            definition_type_corrected = self.removeComma(definition_type)
            dictionary_data = {'type':definition_type_corrected,'definition':definition}
            return dictionary_data
        except Exception as e:
            dictionary_data = 400
            return dictionary_data

    def removeComma(self, definition_type):
        definition_type_letters = list(definition_type)
        if ',' in definition_type_letters:
            definition_type_letters.remove(',')
            joined_definition_type = ("").join(definition_type_letters) # joining anything that was split from after any unnecessary words
            return joined_definition_type
        else:
            return definition_type
