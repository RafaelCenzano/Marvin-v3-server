# Imports
from bs4 import BeautifulSoup as bs
from requests import get

'''
Get your movie's raitings and what people think of the movie

Gets rottentomatoes score and imdb raiting
'''

class TomatoeScrape:

    # Create URL and request webpage
    def __init__(self, movie):
        self.movie = movie

        # Create URL
        self.url = ('https://www.rottentomatoes.com/m/' + self.movie)

        # Request Page
        r = get(self.url)
        page = r.text

        # Parse Page Data
        self.soup = bs(page, 'html.parser')

    def scrapeRottentomatoes(self):
        try:
            # Find data in parsed data
            rt = self.soup.findAll('span', attrs={'class':'meter-value superPageFontColor'})

            # Raise Exception if data doesn't exsist
            if rt == []: raise Exception

            # Find data in parsed data and get text
            raiting = rt[0].getText()
            people_score = self.soup.findAll('span', attrs={'class':'superPageFontColor', 'style':'vertical-align:top'})
            score = people_score[0].getText()
            want_or_like = self.soup.findAll('div', attrs={'class':'smaller bold hidden-xs superPageFontColor'})
            like_or_want = want_or_like[0].getText()

            # Change type if movie has hit the theaters yet
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
            # Return none when no data found
            movie_data = {'type':'none',
                          'score':'none','raiting':'none'}
            return movie_data

    def IMDb(self):
        try:
            # Find data in parsed data
            pg_up = self.soup.findAll('li', attrs={'class':'meta-row clearfix'})

            # Raise exception when no data found
            if pg_up == []: raise Exception

            # Get text of data
            up_pg = pg_up[0].getText()
            movie_data = {'raiting':up_pg.rstrip()}
            return movie_data

        except Exception as e:
            # Return none when no data found
            movie_data = {'raiting':'none'}
            return movie_data
