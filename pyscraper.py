import requests
import bs4

res = requests.get('https://www.developercodehack.com/')

# print(type(res))

# print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup.prettify())
# print(type(soup))
for article in soup.find_all('div', class_='blog-posts hfeed container index-post-wrap'):
    # print(article.article.prettify())
    for oneArticle in article.article.find_all('div', class_='entry-header'):
        print(oneArticle.h2.a.text)

"""
print(soup.select('.widget-content'))

print("----------------")
for i in soup.select('.widget-content'):
    print(i.text)
"""
