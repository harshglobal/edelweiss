from bs4 import BeautifulSoup 
from django.shortcuts import render


import requests
import lxml
import urllib


def mynews(request,id):
    home_url = 'https://www.livemint.com/market'
    url = f'https://www.livemint.com/market/page-{id}'
    r = requests.get(url).text.encode('utf8').decode('ascii', 'ignore')
    soup = BeautifulSoup(r, 'lxml')

    data =[]
    for div,daman in zip(soup.findAll('div', {'class': 'listtostory clearfix'}),soup.findAll('div', {'class': 'headlineSec'})):
        link = urllib.parse.urljoin(url, div.h2.a['href'])
        text = div.h2.a.text
        img=div.div.a.img['src']
        try:
            time = daman.span.em.span.text
        except AttributeError as e:
            time = ""

        try:
            date = daman.span.span.text
        except AttributeError as e:
            date = ""

        ids={'id0':id-1,'id':id,'id1':id+1,'id2':id+2,'id3':id+3,'id4':id+4,'id5':id+5,'id_next':id+1}
        data.append([text,link,img,time,date])
    return render(request,'news.html',{'data':data,'ids':ids})
