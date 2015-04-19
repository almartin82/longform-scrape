import requests
import pandas
import csv
import time
from BeautifulSoup import BeautifulSoup


def parse_article(requests_content, i):
    """parse a longform.org article"""
    soup = BeautifulSoup(requests_content)
    article = soup.find("div", attrs={'class': 'content'})
    title = article.find("h2").text
    author = article.find("span", attrs={'class': 'byline'}).text
    pub_date = article.find("span", attrs={'class': 'publication_date'}).text
    pub_name = article.find("span", attrs={'class': 'publication'}).text
    summary = article.find("div", attrs={'class': 'body'}).text
    parsed = pandas.DataFrame({
        'title': title,
        'author': author,
        'pub_date': pub_date,
        'publication': pub_name,
        'summary': summary
    }, index = [i])
    return parsed

#df to hold the articles
df = pandas.DataFrame()

start = 1
limit = 8227
#testing only
# start = 8000
# limit = 8010

for i in range(start, limit):
    url = 'http://longform.org/posts/' + str(i)
    r = requests.get(url)

    if r.status_code == 200:
        try:
            parsed = parse_article(r.content, i)
        except:
            print 'failed: ' + url
            pass
        df = df.append(parsed)

    #don't hammer them
    time.sleep(0.5)

df.to_csv('longform_sources.csv', sep=',', quoating=csv.QUOTE_ALL, encoding='utf-8')