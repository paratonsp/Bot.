import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def getHtml(url):
    ua = UserAgent()
    header = {'user-agent':ua.random}
    response = requests.get(url,timeout=3000)
    response.raise_for_status()
    return response.content

count = 0

for page in range(1, 265):

    count+= 1
    page_url = "http://sispro.co.id/id/2-sub-kontraktor?page=" + str(page)
    html = getHtml(page_url)
    soup = BeautifulSoup(html, 'html.parser',)
    for a in soup.find_all(attrs='read-more', href=True):
        with open("C:/Users/parat/Desktop/link-sub-kontraktor.txt", "a") as text_file:
            text_file.write("http://sispro.co.id" + a['href'] + "\n")

    print("Progress: " + str(count) + " Pages")

print('FINISH!!!')
