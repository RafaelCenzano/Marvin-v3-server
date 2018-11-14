# Imports
from bs4 import BeautifulSoup as bs
from requests import get

'''
File to get definition data without glitchy definition api

gets word definition and type of word exp:'Noun'
'''

# Class for webscraping definitions
class DefinitionFind:

    # Create URL and request webpage
    def __init__(self, query):
        self.query = query

        # Create URL
        url = ('https://www.dictionary.com/browse/' + self.query + '?s=t')

        # Request Page
        r = get(url)
        page = r.text

        # Parse Page Data
        self.soup = bs(page, 'html.parser')

    # Get definition data from requested page
    def scrapeDefinition(self):
        try:
            # Find data in parsed data
            define_find_type = self.soup.findAll('span', attrs={'class':'luna-pos'})
            define_find = self.soup.findAll('span', attrs={'class':'css-9sn2pa e10vl5dg6'})

            # Raise Exception if data doesn't exsist
            if define_find == []: raise Exception
            if define_find_type == []: raise Exception

            # Get text for definition data
            definition_type = define_find_type[0].getText()
            definition = define_find[0].getText()

            # Correct text
            definition_type_corrected = self.removeComma(definition_type)

            # Create dictionary for JSON API
            dictionary_data = {'type':definition_type_corrected,'definition':definition}

            # Return Data
            return dictionary_data

        except Exception as e:
            # Return none when data can't be found
            dictionary_data = {'type':'none','definition':'none'}
            return dictionary_data

    def removeComma(self, definition_type):
        # Split apart word into letters in list
        definition_type_letters = list(definition_type)

        # Remove comma in list
        if ',' in definition_type_letters:
            definition_type_letters.remove(',')
            joined_definition_type = ("").join(definition_type_letters) # joining anything that was split from after any unnecessary words

            # Return correct definition type
            return joined_definition_type
        return definition_type
