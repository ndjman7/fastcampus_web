from django.shortcuts import render, redirect
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from .forms import VideoForm
from .models import Video


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDZkR1Zn7YYQt5PA1PHIGQVYTXSKteUCW0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword, page_token, max_results=10):
    youtube = build(
      YOUTUBE_API_SERVICE_NAME,
      YOUTUBE_API_VERSION,
      developerKey=DEVELOPER_KEY
    )

  # Call the search.list method to retrieve results matching the specified
  # query term.
    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=max_results,
        pageToken=page_token,
    ).execute()

    return search_response


def search(request):
    context = {}
    keyword = request.GET.get('keyword')
    page_token = request.GET.get('page_token')
    if keyword:
        response = youtube_search(keyword, page_token)
        context['keyword'] = keyword
        context['response'] = response
        context['page_token'] = page_token
    return render(request, 'video/search.html', context)


def add_bookmark(request):
    """
    POST요청을 받음

    kind
    videoId
    title
    description
    publishedAt
    thumbnails

    요소들을 사용해서​
        Video 인스턴스 생성 후
        받았던 페이지로 돌아가기
        request.path값을 POST안에 받아서 돌아와야 됨
    """
    if request.method == 'POST':
        video = Video(
            kind=request.POST['kind'],
            videoId=request.POST['videoId'],
            title=request.POST['title'],
            description=request.POST['description'],
            publishedAt=request.POST['publishedAt'],
            thumbnails=request.POST['thumbnails'],
        )
        video.save()
        # redirect 가 url 만 보내주 면 되는건지 url이름을읽고그함수에게일을넘기는건지알아봐야겠다.
        # 만약함수에 게일을넘기는역할을하는거라면내생각에는render가 어울릴 거같기도?
        return redirect('search')

def bookmark_list(request):
    videos = Video.objects.all()
    return render(request, 'video/bookmark_list.html', {'videos': videos})
