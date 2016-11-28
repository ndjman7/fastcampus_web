## DFS Tutorial 4: Authentication & Permissions

게시물을 만들 때에는 작성자가 필요하다.

`models.py`
```python3
owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlighted = models.TextField()
```

`serializers.py`
```python3
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
```

`views.py`
```python3
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

`urls.py`
```python3
url(r'^users/$', views.UserList.as_view()),
url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
```

#### 게시글과 Users를 연결
`SnippetList`
```python3
def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
```
기존의 createview가 HTTP method POST로 들어오면, 생성되는데, onwer와 같은 경우는 기존의 데이터가 아닌 특이한 request.user이기 때문에 직접 명시해줘야한다.

## Updating our serializer
`serializers.py`
```python3
owner = serializers.ReadOnlyField(source='owner.username')
```

**ReadOnlyField**란?
출력때는 표현되지만 작성/수정 중에는 추가할 수 없다.

`views.py`
```python3
from rest_framework import permissions

permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
```

#### Object level permissions
`permission.py`
```python3
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
```

`views.py`
```python3
from snippets.permissions import IsOwnerOrReadOnly

permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
```