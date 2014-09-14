'''
Created on Sep 14, 2014

@author: jordan
'''
import urllib, urllib2
import json
from bs4 import BeautifulSoup

def search(searchTerm):
    query = urllib.urlencode ( { 'q' : searchTerm } )
    url = ('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query)
    response = urllib.urlopen(url).read()
    results = json.loads(response)
    data = results['responseData']['results']
    return data

def search4url(text):
    data = search(text)
    if(not data):
        return None
    for result in data:
        url = result['url']   # was URL in the original and that threw a name error exception
        if('stackoverflow' in url):
            return(url)
    return(None)

def url2code(url):
    response = urllib2.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html)
    mydivs = soup.findAll("div", { "class" : "accepted-answer" })
    div = mydivs[0]
    return div.code.string

def text2code(text):
#     search google for text
    url = search4url(text)
#     get code from first stack overflow result
    if( not url):
        return None
    code = url2code(url)
#     run code
    exec(code)

if __name__ == '__main__':
    text2code('python hello world')
