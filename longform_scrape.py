import requests
import pandas
import csv
import time
from bs4 import BeautifulSoup


def parse_article(requests_content, i):
    """parses a longform.org article for date/author/publication etc"""
    soup = BeautifulSoup(requests_content)
    #posted_at is outside the article div
    posted_at = soup.find("div", attrs={'class': 'posted_at'}).text
    #grab the article div and extract relevant data
    article = soup.find("div", attrs={'class': 'content'})
    title = article.find("h2").text
    author = article.find("span", attrs={'class': 'byline'}).text
    pub_date = article.find("span", attrs={'class': 'publication_date'}).text
    pub_name = article.find("span", attrs={'class': 'publication'}).text
    article_summary = article.find("div", attrs={'class': 'body'}).text
    parsed = pandas.DataFrame({
        'author': author,
        'posted_at': posted_at.replace('Posted on ', ''),
        'pub': pub_name,
        'pub_date': pub_date,
        'summary': article_summary.replace('\n', ''),
        'title': title,
    }, index=[i])
    return parsed

#df to hold the articles
df = pandas.DataFrame()

start = 1
limit = 8227
#testing only
#start = 8000
#limit = 8010

for i in range(start, limit):
    url = 'http://longform.org/posts/' + str(i)
    r = requests.get(url)

    if r.status_code == 200:
        try:
            parsed = parse_article(r.content, i)
            df = df.append(parsed)
        except:
            print 'failed: ' + url
            pass

    #don't hammer them
    time.sleep(0.1)

df.to_csv('longform_sources.csv', sep=',', quoating=csv.QUOTE_ALL, encoding='utf-8')