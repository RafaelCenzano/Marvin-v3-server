#Imports
from bs4 import BeautifulSoup as bs
from requests import get
from urllib.parse import urlparse


'''
File that was created to help my lazy self
open youtube with my voice

Webscraper that gets the first 2 non advertisement
videos that show up when we it searches for your query
'''

# Class for all youtube based scraping
class YoutubeScrape:
    def __init__(self, query):

        # create self variables to hold class constants
        self.query = query
        self.videolist = []
        self.url = ('https://www.youtube.com/results?search_query=' + self.query)

        # request data section
        r = get(self.url)
        page = r.text

        # start soup functions
        soup = bs(page, 'html.parser')
        self.vids = soup.findAll(attrs={'class':'yt-uix-tile-link'})

    def is_absolute(self, url):
        # determine if input url is true url
        return bool(urlparse(url).netloc)

    def scrapeYoutube(self):
        # go through all found links with
        for v in self.vids:

            # if link that its checking is already a true link then it is an ad
            if self.is_absolute(v['href']) == True:
                pass # pass to not add advertisement link

            # when not true link so its a real video
            else:
                tmp = 'https://www.youtube.com' + v['href']
                self.videolist.append(tmp)

        # create dictionary to return to send found data in json format
        video_link = {'link':self.videolist[0],'link2':self.videolist[1]}
        return video_link # return dictionary
