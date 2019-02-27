import requests
from bs4 import BeautifulSoup


def get_chapter_titles():
    lines = [line.rstrip('\n') for line in open('DataCampClasses.txt')]

    html_docs = []

    for line in lines:
        r = requests.get('https://www.datacamp.com/courses/' + line)
        html_docs.append(r.text)

    titles_dict = {}

    for course in html_docs:
        soup = BeautifulSoup(course, features='html.parser')
        hero_title = soup.find_all('h1', attrs={'class': 'header-hero__title'})
        chapter_title = soup.find_all('h4', attrs={'class': 'chapter__title'})
        for item in chapter_title:
            titles_dict.setdefault(hero_title[0].text, []).append(item.text.strip())

    for key, value in titles_dict.items():
        print('\n' + key)
        for item in value:
            print(item)


get_chapter_titles()
