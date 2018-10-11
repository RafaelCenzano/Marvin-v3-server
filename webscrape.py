#Imports
from bs4 import BeautifulSoup as bs # process html
from requests import get # to request page url code
from urllib.parse import urlparse # urlparse to parse url data


########################
# File for webscraping #
########################


class YoutubeScrape:
    def __init__(self, speak_type, command, split_num):
        if checkConnection() == True:
            self.search_query = splitJoin(command, split_num) # function to split and rejoin command
            self.speak_type = speak_type
            self.videolist = [] # create empty list
            self.url = ('https://www.youtube.com/results?search_query=' + self.search_query)# combine url with search query from command
            r = get(self.url) # request page
            page = r.text # formatting
            soup = bs(page, 'html.parser') # parse html
            self.vids = soup.findAll(attrs={'class':'yt-uix-tile-link'}) # search for class yt-uix-tile-link in html from page
            self.go_no_go = 'go'
        else:
            self.go_no_go = 'no'

    def is_absolute(self, url):
        return bool(urlparse(url).netloc)

    def scrapeYoutube(self):
        if self.go_no_go == 'go':
            speak('Opening first video for ' + self.search_query + ' on YouTube', self.speak_type) # saying what it will open
            for v in self.vids: #for loop for finding all videos that show up
                if self.is_absolute(v['href']) == True:
                    pass
                else:
                    tmp = 'https://www.youtube.com' + v['href'] # create url to add to list with links from html
                    self.videolist.append(tmp) # add the newly created url to list
            webopen(self.videolist[0], new = 2) # open the url
            print('Done!') # finish message
        else:
            speak('No internet connection couldn\'t access')

class TomatoeScrape:
    def __init__(self, movie):
        spliting = self.search_query.split(" ")[0:]
        search_query_with_under_scores = ("_").join(spliting)
        self.url = ('https://www.rottentomatoes.com/m/' + search_query_with_under_scores)# combine url with search query from command
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
                movie_data = ('movie'=self.search_query,'type'='liked',
                              'score'=score,'raiting'=raiting)
                return movie_data
            elif like_or_want == 'want to see':
                movie_data = ('movie'=self.search_query,'type'='want',
                              'score'=score,'raiting'=raiting)
                return movie_data
            else:
                raise Exception
        except Exception as e:
            movie_data = ('movie'='none','type'='none',
                          'score'='none','raiting'='none')
            return movie_data

    def IMDb(self):
        if go_no_go == 'go':
            try:
                pg_up = self.soup.findAll('li', attrs={'class':'meta-row clearfix'})
                if pg_up == []: raise Exception
                up_pg = pg_up[0].getText()
                speak('\n' + self.search_query + ' got a IMDb' + up_pg, self.speak_type)
            except Exception as e:
                speak('\nI ran into a problem\nThe name of the movie was probably input incorrectly', self.speak_type)
        else:
            speak('No internet connection couldn\'t access')

class DefinitionFind:
    def __init__(self, speak_type, command, split_num):
        if checkConnection() == True:
            self.search_query = splitJoin(command, split_num) # function to split and rejoin command
            self.speak_type = speak_type
            url = ('https://www.dictionary.com/browse/' + self.search_query + '?s=t')# combine url with search query from command
            r = get(url) # request page
            page = r.text # formatting
            self.soup = bs(page, 'html.parser') # parse html
            self.go_no_go = 'go'
        else:
            self.go_no_go = 'no'

    def scrapeDefinition(self):
        if go_no_go == 'go':
            try:
                define_find_type = self.soup.findAll('span', attrs={'class':'luna-pos'})
                define_find = self.soup.findAll('span', attrs={'class':'css-9sn2pa e10vl5dg6'})
                if define_find == []: raise Exception
                if define_find_type == []: raise Exception
                definition_type = define_find_type[0].getText()
                definition = define_find[0].getText()
                definition_type_corrected = self.removeComma(definition_type)
                speak(self.search_query + ' is a ' + definition_type_corrected + '\nThe definition is: ' + definition, self.speak_type)
            except Exception as e:
                speak('\nI ran into a problem\nThe name of the word was probably input incorrectly', self.speak_type)
                print(e)
        else:
            speak('No internet connection couldn\'t access')

    def removeComma(self, definition_type):
        definition_type_letters = list(definition_type)
        if ',' in definition_type_letters:
            definition_type_letters.remove(',')
            joined_definition_type = ("").join(definition_type_letters) # joining anything that was split from after any unnecessary words
            return joined_definition_type
        else:
            return definition_type


def getVersion():
    if checkConnection() == True:
        url = ('https://github.com/SavageCoder77/MARVIN_2.0/blob/master/marvin/json/marvin_version.txt')
        r = get(url) # request page
        page = r.text
        soup = bs(page, 'html.parser') # parse html
        vids = soup.findAll('td', attrs={'id':'LC1', 'class':'blob-code blob-code-inner js-file-line'}) # search for class meter-value superPageFontColor in html from page
        version_marvin = vids[0].getText()
        print('Marvin Version ' + str(version_marvin))
        return version_marvin
    else:
            speak('No internet connection couldn\'t access')
