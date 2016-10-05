## Writing your first Django app, part1

두 가지로 구성
1. 사람들이 투표를 할 수 있는 사이트
2. 관리자 사이트에서 투표를 추가,변경 그리고 삭제
Django는 이미 설치 되었다고 가정
```shell
$ python -m django --version
```
<br>
#### 프로젝트 생성
__cd__를 이용해서 해당 폴더로 들어간 다음에, 명령어 입력
```script
$ django-admin startrpoject mysite
```
주의할 점
> 가능한 Python과 Django 요소와 관련된 이름은 제외한다.
> django (Django자체로 충돌 가능)
> test (Python package와 충돌 가능)
<br>
> PHP의 옛날 프레임워크를 사용해서 서버의 root폴더가 /var/www에 있을 것이다.
> 보안상의 문제로 Django에서는 추천하는 방법이 아니다.
> root 디렉토리 밖에다가 코드를 사용해라. ex) /home/mycode
<br>
startproject시 생성되는 건 다음과 같다.
```
mysite/
	manage.py
	mysite/
		__init__.py
		settings.py
		urls.py
		wsgi.py
```

1. 바깥쪽의 **mysite/** root 폴더는 프로젝트의 컨테이너 역할이다. Django랑은 상관 없으므로 원하는 이름으로 바꿔도 된다.
2. **manage.py**: 커맨드라인으로 Django와 다양한 방법으로 이용할 수 있다.
3. 안쪽의 **mysite/**는 프로젝트의 Python package다. 필요한 건 뭐든 import해서 사용할 수 있다. ex) **mysite.urls**
4. **mysite/\__init__.py**: 파이썬 모듈임을 선언해주는 파일이다.
5. **mysite/settings.py**: 프로젝트의 세팅 설정이다.
6. **mysite/urls.py**: Django의 URL 선언; 
7. **mysite/wsgi.py**: WSGI-compatible 웹 서버를 사용하게 해주는 것.
<br>
##The development server
```
$ python manage.py runserver
```
http://127.0.0.1:8000/ 이 웹 브라우저에서 나타나며 "Welcome to Django"를 출력할 것이다.

>**Changing the port**
>port를 바꿀 시
>```
>$ python manage.py runserver 8080
>```
>IP를 바꿀 시
>```
>$ python manage.py runserver 0.0.0.0:8000
>```
<br>
>runserver는 자동으로 reload된다.
## Creating the Polls app
apps은 Python path 어디든 존재할 수 있다. 이 튜토리얼은 manage.py 옆에 만들겠다.
```
$ python manage.py startapp polls
```

```
polls/
	\__init__.py
	admin.py
	apps.py
	migrations/
		\__init__.py
	models.py
	tests.py
	views.py
```
#Write your first view
poll/views.py
```python
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
```

view를 사용하기 위해서 URL을 매칭시켜야한다. 이는 URLconf가 필요하다.
__urls.py__ 를 생성한다.

```
polls/
	\__init__.py
	admin.py
	apps.py
	migrations/
		\__init__.py
	models.py
	tests.py
	urls.py
	views.py
```
<br>
polls/urls.py
```python
from django.conf.urls import url
form . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
```

mysite/url.py
```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', admin.site.urls),
]
```
<br>

## Writing your first Django app, part2
Migrations는 매우 강력하다. models를 변경할때,
> 모델을 변경 (models.py를 수정)
**python manange.py makemigrations**를 실행시켜서, 이러한 변화들을 통해 migrations를 생성한다.
**python manage.py migrate**를 실행시켜서, DB에 적용시킨다.

## Writing your first Django app, part3
## Writing your first Django app, part4