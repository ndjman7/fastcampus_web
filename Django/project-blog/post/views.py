from django.shortcuts import render, render_to_response
from .models import Post
# Create your views here.
# post_list라는 이름의 view
# Post인스턴스를 전부 가져와 posts라는 이름으로 'post_list.html'템플릿에 전달해준다.
def post_list(request):
    # ORM을 이용해 Post인스턴스를 전부 가져옵니다.
    posts = Post.objects.all()

    # 템플릿에 전달할 dictionary객체
    ret = {
            'title': '블로그 글 목록',
            # posts라는 key값에 posts(Queryset)을 지정
            'posts': posts
    }
    # 해당 템플릿('post_list_html')에 전달한 데이터로 render한 값을 response해줍니다.:
    return render_to_response('post_list.html',ret)
