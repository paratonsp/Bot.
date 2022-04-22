import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from dhooks import Webhook, Embed
import re

def getHtml(url):
    ua = UserAgent()
    header = {'user-agent':ua.random}
    response = requests.get(url,timeout=3000)
    response.raise_for_status()
    return response.content


with open('C:/Users/parat/Desktop/link-sub-kontraktor.txt','r') as fd:
    for i, line in enumerate(fd.readlines()):

        url = line.strip()
           
        html = getHtml(url)
        soup = BeautifulSoup(html, 'html.parser',)
        text = soup.find_all(attrs='list-unstyled')
        p = soup.find_all(name='p', text=True)

        output = ''

        emails = re.findall('\S+@\S+', str(p))
        for each in emails:
            p = each.replace('<p>', '')
            pp = p.replace('</p>', '')
            ppp = pp.replace('[', '')
            pppp = ppp.replace(']', '')
            ppppp = pppp.replace(',', '')
            with open("C:/Users/parat/Desktop/email-sub-kontraktor.txt", "a") as text_file:
                text_file.write(ppppp + "\n")

        print("Progress...")

print('FINISH!!!')