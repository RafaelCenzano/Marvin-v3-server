#Imports
from bs4 import BeautifulSoup as bs # process html
from requests import get # to request page url code

'''
Get your movie's raitings and what people think of the movie

Gets rottentomatoes score and imdb raiting
'''

class TomatoeScrape:
    def __init__(self, movie):
        self.movie = movie
        self.url = ('https://www.rottentomatoes.com/m/' + self.movie)# combine url with search query from command
        r = get(self.url) # request page
        page = r.text # formatting
        self.soup = bs(page, 'html.parser') # parse html

    def scrapeRottentomatoes(self):
        try:
            rt = self.soup.findAll('span', attrs={'class':'meter-value superPageFontColor'}) # search for class meter-value superPageFontColor in html from page
            if rt == []: raise Exception
            raiting = rt[0].getText()
            people_score = self.soup.findAll('span', attrs={'class':'superPageFontColor', 'style':'vertical-align:top'})
            score = people_score[0].getText()
            want_or_like = self.soup.findAll('div', attrs={'class':'smaller bold hidden-xs superPageFontColor'})
            like_or_want = want_or_like[0].getText()
            if like_or_want == 'liked it':
                movie_data = {'type':'liked',
                              'score':score,'raiting':raiting}
                return movie_data
            elif like_or_want == 'want to see':
                movie_data = {'type':'want',
                              'score':score,'raiting':raiting}
                return movie_data
            else:
                raise Exception
        except Exception as e:
            movie_data = {'type':'none',
                          'score':'none','raiting':'none'}
            return movie_data

    def IMDb(self):
        try:
            pg_up = self.soup.findAll('li', attrs={'class':'meta-row clearfix'})
            if pg_up == []: raise Exception
            up_pg = pg_up[0].getText()
            movie_data = {'raiting':up_pg.rstrip()}
            return movie_data
        except Exception as e:
            movie_data = {'raiting':'none'}
            return movie_data

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
            dictionary_data = {'type':'none','definition':'none'}
            return dictionary_data

    def removeComma(self, definition_type):
        definition_type_letters = list(definition_type)
        if ',' in definition_type_letters:
            definition_type_letters.remove(',')
            joined_definition_type = ("").join(definition_type_letters) # joining anything that was split from after any unnecessary words
            return joined_definition_type
        else:
            return definition_type
