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

# Class for all youtube based scraping
class YoutubeScrape:
    def __init__(self, query): # pass in search query

        # create self variables to hold class constants
        self.query = query
        self.videolist = [] # create empty list
        self.url = ('https://www.youtube.com/results?search_query=' + self.query)# combine url with search query from command

        # request data section
        r = get(self.url) # request page
        page = r.text # formatting

        # start soup functions
        soup = bs(page, 'html.parser') # parse html
        self.vids = soup.findAll(attrs={'class':'yt-uix-tile-link'}) # search for class yt-uix-tile-link in html from page

    def is_absolute(self, url):
        # determine if data is already a url
        return bool(urlparse(url).netloc)

    def scrapeYoutube(self):
        # go through all found links with
        for v in self.vids: #for loop for finding all videos that show up

            # if link that its checking is already a true link then it is an ad
            if self.is_absolute(v['href']) == True:
                pass # pass to not add advertisement link

            # when not true link so its a real video
            else:
                tmp = 'https://www.youtube.com' + v['href'] # create url to add to list with links from html
                self.videolist.append(tmp) # add the newly created url to list

        # create dictionary to return to send found data in json format
        video_link = {'link':self.videolist[0],'link2':self.videolist[1]}
        return video_link # return dictionary
