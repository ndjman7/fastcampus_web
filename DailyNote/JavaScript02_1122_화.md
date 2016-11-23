웹 퍼블리셔는 HTML, CSS만 하는 사람!

브라우져 핵

브라우져 스니핑 기법

리터럴 값을 쓰는 것을 권장한다.
생성자 함수와 프로토타입

window.navigator.userAgent
-> 브라우져의 식별자

모더나이져

for문 -> 배열 값 순환
for ~ in문 -> 객체 속성 순환

for( let prop in obj ) {
	console.log( 'prop:', prop);
	console.log('value:', obj[prop]);
}

Closer (참조 가능한 데이터는 전부 사용가능 배열,함수,객체)
스코프 체이닝이 가능하므로 전역변수를 오염시키지 않고 변수를 재사용할 수 있다.
그 전에는 메모리 누수가 발생했었지만, 가비지 콜렉터가 가지고 있는 알고리즘을 2012년 이후에 바뀌고 나서는 손실이 최소화된다.  내부에 숨겨진 변수들은 참조되지 않으면 가비지 콜렉터에 의해 자동 소멸된다.

Closer를 이용하면 비공개 멤버를 만들어 줄 수 있다.
아래 예의 init_count와 function_name 같은 느낌.


```javascript
var countDownInit = function(init_count) {
  var function_name = 'countDown';
  // init_count 초기 설정 변수 값
  // 함수 영역 안쪽에 감춰진 함수
  var countDown = function() {
    return init_count--;
  };
  return countDown;
};
var countDown10 = countDownInit(10);
```

함수가 함수를 반환한다.

developer.mozil	la.org
