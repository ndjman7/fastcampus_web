import requests
from django.shortcuts import render
import xml.etree.ElementTree as et
import io
from bs4 import BeautifulSoup


def search(request):
    return render(request, 'movie/movie_search.html', {})


def detail(request):
    client_id = '4'
    client_secret = 'n'
    query = request.GET['movie']
    url = 'https://openapi.naver.com/v1/search/movie.xml?query={}'.format(query)

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    ans = requests.get(url, headers=headers)

    data = et.parse(io.StringIO(ans.text))

    data_root = data.getroot()
    context = {}

    context['movies'] = [
        {
            'title': movie.find('title').text,
            'directors': str(movie.find('director').text).split('|'),
            'actors': str(movie.find('actor').text).split('|'),
            'image': movie.find('image').text,
            'pubdate': movie.find('pubDate').text,
            'link': movie.find('link').text,
        }
        for movie in movies[0].findall('item')
    ]
    for movie in context['movies']:
        movie['title'] = movie['title'].replace('<b>', "")
        movie['title'] = movie['title'].replace('</b>', "")

    return render(request, 'movie/movie_detail.html', context)

