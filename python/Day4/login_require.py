# login_required   유저가 로그인 되었는지   @login_required
# is_admin         유저가 관리자 인지       @is_admin


# User Class :: username, is_admin

# Request    :: user instance ( user O => login O ; user X => login X )
# request = Request()
# request.user
# Response   :: body(string)


class User():

    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin

pando = User("Pando")
admin_user = User("admin", is_admin=True)

class Request():

    def __init__(self, url, user=None):
        self.url = url
        self.user = user

class Response():

    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return "Response :: {body}".format(body = self.body)


# mypage 페이지에 접속했는지 여부
# is_admin
# is_logined

def mypage(request):
    return Response("성공적으로 MyPage에 접속했습니다.")

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user:
            response = func(request, *args, **kwargs)
        else:
            response = Response("로그인이 필요합니다.")
        return response
    return wrapper

def is_admin(func):
    def wrapper(request, *args, **kwargs):
        if request.user and request.user.is_admin:
            response = func(request, *args,**kwargs)
        else:
            response = Response("관리자 권한이 필요합니다.")
        return response
    return wrapper

@is_admin
@login_required
def admin(request):
    return Response("성공적으로 Admin에 접속했습니다.")

request = Request("/admin/")
print(admin(request))
