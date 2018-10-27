#Imports
from bs4 import BeautifulSoup as bs # process html
from requests import get # to request page url code
from urllib.parse import urlparse # urlparse to parse url data


'''
File that was created to help my lazy self
open youtube without my voice

Webscraper that gets the first 2 non Advertisements
videos that show up when we it searches for your query
'''

class YoutubeScrape:
    def __init__(self, query):
        self.query = query
        self.videolist = [] # create empty list
        self.url = ('https://www.youtube.com/results?search_query=' + self.query)# combine url with search query from command
        r = get(self.url) # request page
        page = r.text # formatting
        soup = bs(page, 'html.parser') # parse html
        self.vids = soup.findAll(attrs={'class':'yt-uix-tile-link'}) # search for class yt-uix-tile-link in html from page

    def is_absolute(self, url):
        return bool(urlparse(url).netloc)

    def scrapeYoutube(self):
        for v in self.vids: #for loop for finding all videos that show up
            if self.is_absolute(v['href']) == True:
                pass
            else:
                tmp = 'https://www.youtube.com' + v['href'] # create url to add to list with links from html
                self.videolist.append(tmp) # add the newly created url to list
        link = self.videolist[0]
        link2 = self.videolist[1]
        video_link = {'code':200,'link':link,'link2':link2}
        return video_link
