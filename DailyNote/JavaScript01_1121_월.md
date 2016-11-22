## JavaScript 1일차
사용성 (UI & UX) 접근성

link는 병렬식
@import 직렬식

hoist와 closure를 만들기. (이 수업에서 알고 가져가야할 것)

설계가 필요하다.

title은 중요하다 페이지마다 의미를 담고있어야한다.

`<meta http-equiv="X-UA-Compatible" content="ie=edge">`
비표준 코드

프론트엔드 환경에서 자바스크립트 혼자 구동할 수 없다.

자바스크립에서의 null은 값이 비어있다는 의미이다.
head에서 script를 불러오는 것은 안좋은 짓이다.
Dom content loaded가 불리는 시점은 body 끝 쪽이다.

표현식과 선언식에서만 함수가 대입 가능하다.

(fucntion(){};()) - 권장하는 방식.

'use strict';
// 엄격한 자바스크립트 (모드 변경)

소스코드를 모듈화해서 전역변수에 (window를 오염) 선언시키지 않아서 깔끔하게 이용한다.

의존성 방식도 없고 모듈로드 방식도 없다.

#### JavaScript Core 정리
자바 스크립티 데이터 유형
원시 데이터 유형
1. Number
2. String
3. Boolean
참조 데이터 유형
4. Function (Object)
5. Array (Object)
6. Object (Plain Object)

리터럴 (보다 많이 사용 권장)
단!! 네이티브(내장, 빌트인) 객체 생성자 함수를 사용할 때만

데이터 타입 체크
1. typeof
```javascript
console.log('typeof num:', typeof num);             // 'number'
console.log('typeof str:', typeof str);             // 'string'
console.log('typeof boo:', typeof boo);             // 'boolean'
console.log('typeof fnc:', typeof fnc);             // 'function'
console.log('typeof arr:', typeof arr);             // 'array' [X]
console.log('typeof obj:', typeof obj);             // 'object'
console.log('typeof null:', typeof null);           // 'object' [X]
console.log('typeof undefined:', typeof undefined); // 'undefined'
```

2. instanceof
원시 데이터 유형의 경우 기대대로 체크되지 않음
참조 데이터 유형만 올바리그 체크함
```javascript
console.log('arr instanceof Array:', arr instanceof Array);   // true
console.log('arr instanceof Object:', arr instanceof Object); // false
```

3.constructor
자바스크립트객체.constructor === 생성자
객체의 유형에 한해서 만큼은 기대하는대로 올바르게 체크 됨.
객체가 아닌 유형 (undefined, null)에서는 오류가 발생함.

```javascript
console.log('num.constructor:', num.constructor);
console.log('str.constructor:', str.constructor);
console.log('boo.constructor:', boo.constructor);
console.log('fnc.constructor:', fnc.constructor);
console.log('arr.constructor:', arr.constructor);
console.log('obj.constructor:', obj.constructor);
```

4.custom function `isType()`
```javascript
function type(data) {
  // 어떤 데이터 유형인지 감지
  return Object.prototype.toString.call(data).slice(8,-1).toLowerCase();
}

function isType(data, compare) {
  return type(data) === compare;
}

function isNumber(data) {
  return type(data) === 'number';
}
function isString(data) {
  return type(data) === 'string';
}
function isBoolean(data) {
  return type(data) === 'boolean';
}
function isFunction(data) {
  return type(data) === 'function';
}
function isArray(data) {
  return type(data) === 'array';
}
function isObject(data) {
  return type(data) === 'object';
}
```

use strict로 엄격하게 자바스크립트 문법을 체크해준다.

>자바스크립트에서 **호이스트**란?
>
>var, function 키워드로 정의된 것들이 scope의 상단으로 끌어올려지는 현상을 말한다.
>주의할 점은 function 선언문과 달리 var 키워드의 경우는 변수 이름만 끌어 올리고, 값이 대입(할당)되는 시점은 실제 코드가 작성된 곳에서 진행된다.


**함수 표현식**
var clickPrintSquare = function (){
console.log('this:', this);
};
**함수 선언식**
function clickPrintSquare(){
console.log('this:', this);
};

프론트엔드 환경에슨 IIFE 패턴(즉시 실행함수)을 사용