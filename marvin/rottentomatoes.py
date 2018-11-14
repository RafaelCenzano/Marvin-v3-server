# Imports
from bs4 import BeautifulSoup as bs
from requests import get

'''
Get your movie's raitings and what people think of the movie

Gets rottentomatoes score and imdb raiting
'''

class TomatoeScrape:
    def __init__(self, movie):
        self.movie = movie
        self.url = ('https://www.rottentomatoes.com/m/' + self.movie)
        r = get(self.url)
        page = r.text
        self.soup = bs(page, 'html.parser')

    def scrapeRottentomatoes(self):
        try:
            rt = self.soup.findAll('span', attrs={'class':'meter-value superPageFontColor'})
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
