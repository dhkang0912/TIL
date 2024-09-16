var 이름 = "kim";
// 터미널 켜서 tsc -w 입력해두면 자동변환됨
// ?인 경우 해당 속성이 들어올 수도 있고, 아닐 수도 있는 경우
// 아래와 같이 하는 경우 name 속성은 문자만 가능
var 이름 = { name: "kim" };
// union 타입으로 문자와 숫자가 들어올 수 있는 경우
var 이름 = 123;
var 이름 = 123;
// 무조건 number를 인자로 받고, number를 리턴함
function 함수(x) {
    return x * 2;
}
var john = [123, true];
var john = { name: "kim", age: "123" };
// class 타입 지정 가능
var User = /** @class */ (function () {
    function User(name) {
        this.name = name;
    }
    return User;
}());
