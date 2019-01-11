import re
import requests
from bs4 import BeautifulSoup

# lines = [line.rstrip('\n') for line in open('DataCampClasses.txt')]
#
# html_docs = []
#
# for line in lines:
#     r = requests.get('https://www.datacamp.com/courses/' + line)
#     html_docs.append(r.text)
#
# link_list = []
#
# for course in html_docs:
#     soup = BeautifulSoup(course, features='html.parser')
#     exercise_link = soup.find('a', attrs={'class': 'chapter__exercise-link'})['href']
#     exercise_link = str.replace(exercise_link, '?ex=1', '?ex=2')
#     link_list.append(exercise_link)
#
# exercise_html = []
# link_pattern = re.compile(r'https://s3.amazonaws.com/assets.datacamp.com/.{10,75}slides.pdf')
# pdf_links = []
#
# for link in link_list:
#     request = requests.get(link)
#     exercise_html.append(request.text)
#
#     pdf_link = re.findall(link_pattern, request.text)
#     for item in pdf_link:
#         if item not in pdf_links:
#             pdf_links.append(item)
#
# with open('PDF Links.txt', 'w') as f:
#     for item in pdf_links:
#         f.write("%s\n" % item)
#
# print(pdf_links)

# lines = [line.rstrip('\n') for line in open('PDF Links.txt')]
#
# pdf_pattern = re.compile(r'course.*\b')
# new_pdf_name = []
#
# for download_link in lines:
#     r = requests.get(download_link, stream=True)
#
#     pdf_name = re.findall(pdf_pattern, download_link)
#     pdf_name[0] = str.replace(pdf_name[0], '/', '_')
#
#     with open('D:\\Users\\ana1\\PycharmProjects\\ParseDataCamp\\' + pdf_name[0], "wb") as f:
#         f.write(r.content)
