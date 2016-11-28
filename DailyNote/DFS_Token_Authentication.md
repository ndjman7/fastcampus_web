## Django rest Tokenauthentication

Django에서 인증 구현 방법으로 Token이 있다.
Token 클래스에서 user의 정보를 넣어주면 토큰을 반환하는데, 이를 통해서
Request Header에 넣으면 로그인 인증을 해준다.
Token이 노출되면 api를 무단으로 호출될 가능성이 있지만, 비밀번호 유출을 막음으로써 보안이 강화되었다고 볼 수 있다.

framework로 token을 본 결과, logout시에는 Token을 delete() 시켜준다.
