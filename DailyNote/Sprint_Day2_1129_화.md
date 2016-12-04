pk=kwargs.get("pk")
url로 넘어온 값은 {} dic 형태로 와서 다음과 같이 얻을 수 있다.

```python3
all = mov.useractivity_set.all().exclude(score=None)
```
다음과 같이 score = None을 제외한 값을 얻어올 수 있다.

### Github의 Organization 
Git repository의 그룹같은 느낌이다. 여기서 백엔드, 프론트엔드, 안드로이드의 저장소를 한 번에 다 관리한다. Owner와 Member가 있는데, Owner는 pull request를 merge할 수 있는 권한이 있는 것 같다.

 - upstream이라는 원격저장소로, fork를 내 repository에 뜬다.
 - local은 upstream에서 pull을 받아온다.
 - local에서 새로운 브랜치를 수정한 뒤에는 fork를 뜬 내 github 저장소의 repository에 origin으로 push를 날려서 정보를 업데이트한다.
 - upstream으로 pull request를 관리한다.

### 중간자 모델의 역할
m2m field 없이 중간자 모델에서
forienkey(A), forienkey(B)만으로 작성이 되었는데,
이 때 중간자 모델이 필요한 이유는 A,B가 서로 직접 찾을 수 있도록 해준다는 점이다.
