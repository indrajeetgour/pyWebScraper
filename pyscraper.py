"""
Crawler the sample web site data for this example
"""

import requests
import bs4

site_url = 'https://www.developercodehack.com/'


def get_site_response():
    res = requests.get(site_url)
    return res


def extract_site_response(res):
    # start parsing the site response
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # print(soup.prettify())
    # only_dev = soup.find('div', class_='blog-posts hfeed container index-post-wrap')
    # print(only_dev.article.prettify())

    # for only_dev in soup.find_all('div', class_='blog-posts hfeed container index-post-wrap'):
    div_section = soup.find('div', class_='sidebar widget-ready section').div
    for only_dev in div_section.find_all('article'):
        print("Post URL: " + only_dev.find('div', class_='entry-header').h2.a['href'])
        print("Post Heading: " + only_dev.find('div', class_='entry-header').h2.a.text+'\n\n')

        # print("Post URL: " + only_dev.article.find('div', class_='widget-content').h2.a['href'])
        # print("Post Heading: " + only_dev.article.find('div', class_='entry-header').h2.a.text)
        # print("Short description: " + only_dev.article.find('div', class_='entry-header').p.text)

    # for article in soup.find_all('div', class_='blog-posts hfeed container index-post-wrap'):
    #     # print(article.article.prettify())
    #     for oneArticle in article.article.find_all('div', class_='entry-header'):
    #         print(oneArticle.h2.a.text)


if __name__ == '__main__':
    # python request for site
    response = get_site_response()

    # extract the required information
    extract_site_response(response)

"""
print(soup.select('.widget-content'))

print("----------------")
for i in soup.select('.widget-content'):
    print(i.text)
"""
