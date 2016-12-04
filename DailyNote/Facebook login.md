##Facebook API (로그인)
로그인 플로 직접 빌드
#### 로그인 상태 확인
SDK를 사용하는 앱에서는 사용자가 기본 제공 기능을 사용하여 이미 로그인했는지 확인할 수 있다. 기타 모든 앱에서는 사용자가 로그인한 시기를 저장하는 고유 방식을 만들어야 하며, 해당 지표가 없는 경우 사용자가 로그아웃했다는 가정하에 진행합니다. 사용자가 로그아웃하고 나면 사용자가 로그인 버튼을 클릭할 때처럼 해당 시기에 앱에서 사용자를 로그인 대화 상자로 리디렉션 해야합니다.

#### 사용자 로그인 유도
사용자가 앱에 로그인하지 않았거나 Facebook에 로그인하지 않은 경우 로그인 대화 상자를 사용하여 둘 다를 수행하도록 메시지를 표시할 수 있습니다. Facebook에 로그인하지 않은 경우 로그인하도록 메시지를 표시한다음 앱에 로그인을 진행합니다. 이는 자동으로 감지되므로 이 동작을 활성화하기 위해 어떠한 추가 작업도 수행할 필요 없습니다.

**로그인 대화 상자 호출 및 리디렉션 URL 설정**
앱에서 로그인 대화 상자를 표시할 엔드포인트로 리디렉션을 시작해야 합니다.

```python3
https://www.facebook.com/v2.8/dialog/oauth?
	client_id={app_id}
	&redirect_uri={redirect_uri}
```
	
이 엔드포인트의 필수 매개변수는 다음과 같습니다.
- client_id: 앱의 대시보드에 있는 앱 ID입니다.
- redirect_uri: 사용자가 다시 로그인하도록 리디렉션할 URL입니다. 이 URL은 로그인 대화 상자에서 응답을 캡처합니다.
#### REST (backend에서 처리해줘야할 사항)
클라이언트에서 처리된 AccessToken이 오면 Backend에서는 Debug_url을 이용해서 해당 토큰이 올바른 토큰인지 파악한 후에 비로소 로그인이 가능하도록 구현해준다.

#### Issue
메인 이미지와 커버 이미지 문제.
해당 이미지를 칼럼으로 만들지 아니면 요청이 들어왔을 시에 직접 Graph API를 통해 다녀올지, 그것도 아니면 클라이언트에서 받을지 생각해봐야한다.
일단은 서버에서 access_token으로 접근해서 가져오는 방안으로 생각한다.

#### field 추가
is_facebook_user = models.BooleanField(default=False)
facebook_id = models.CharField(max_length=200, blank=True)
img_profile_url = models.URLField(blank=True)
cover_img_url = models.URLField(bank=True)

#### backends.py
```python3
django_app/member/backends.py
from djnago.contrib.auth import get_user_model
User = get_user_model()

class FacebookBackend:
	def authenticate(self, user_info, token=None):
		try:
			user = User.objects.get(facebook_id=user_info.get('id'))
			return user
		except User.DoesNotExist:
			user = User.objects.create_facebook_user(user_info)
			return user
			
		def get_user(self, user_id):
			try:
				return User.objects.get(pk=user_id)
			except User.DoesNotExist:
				return None
```

```python3
def create_facebook_user(self, user_info):
	user = self.model(
		email=user_info['email']
		last_name=user_info.get('lasat_name',''),
		first_name=user_info.get('first_name'.''),
		is_facebook_user=True
		facebook_id=user_info['id'],
		img_profile_url=user_info['picture']['data']['url'],
	)
	user.save()
	return user
```

django_app/member/apis/facebook.py
```python3
from django.conf import settings
import requests
import json

__all__ = [
	'get_access_token',
	'get_user_id_from_token',
	'debug_token',
	'get_user_info'

APP_ID = settings.FACEBOOK_APP_ID
SECRET_CODE = settings.FACEBOOK_SECRET_CODE

APP_ACCESS_TOKEN = '{app_id}|{secret_code}'.format(
	app_id=APP_ID,
	secret_code=SECRET_CODE
)

def get_access_token(code, redirect_url):
	
```


facebook.py
```python3
import requests
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from member.apis import facebook
```