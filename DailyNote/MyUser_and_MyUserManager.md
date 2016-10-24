MyUser와 MyUserManager를 만들면서 드는 생각

User를 커스터마이징하든 기본 유저를 쓰든 Django에서는 한 가지 User 객체만을 사용한다.
개인이 만든 User를 사용할 경우 AUTH_USER_MODEL = 'member.MyUser'를 'settings.py'에 넣어준다.

##MyUser
MyUser는 AbstractBaseUser와 PermissionsMixin을 상속 받는다.
자기 입맛에 맞는 필드들을 넣어 주고,
USERNAME_FIELD는 ID를 지칭하는 부분이다.
REQUIRED_FIELDS는 필수 입력사항들을 넣어준다.

objects에는 MyUser가 커스터마이징된 Manager를 사용할 수 있게 한다.

MyUser 클래스는 get_full_name이라는 함수와 get_short_name함수를 오버라이딩 해주지 않으면 경고?가 나온다.

##MyUserManager
일단 create_user와 create_superuser 같은 경우는 내가 MyUser 필드들을 함부로 건드렸으므로 그에 해당하는 함수들을 오버라이딩 해주어야한다.