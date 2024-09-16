let 이름: string[] = "kim";
// 터미널 켜서 tsc -w 입력해두면 자동변환됨

// ?인 경우 해당 속성이 들어올 수도 있고, 아닐 수도 있는 경우
// 아래와 같이 하는 경우 name 속성은 문자만 가능
let 이름: { name?: string } = { name: "kim" };

// union 타입으로 문자와 숫자가 들어올 수 있는 경우
let 이름: string | number = 123;

// 타입을 변수로 만들고 싶은 경우 아래처럼 사용 가능
// 타입 변수는 구분을 위해 주로 대문자로 지정
type Name = string | number;
let 이름: Name = 123;

// 무조건 number를 인자로 받고, number를 리턴함
function 함수(x: number): number {
  return x * 2;
}

// array에 쓸 수 있는 tuple 타입
type Member = [number, boolean];
let john: Member = [123, true];

// object에 타입 지정해야할 속성이 너무 많은 경우
// Member 안에 들어오는 모든 key와 값은 string
type Member = {
  [key: string]: string;
};

let john: Member = { name: "kim", age: "123" };

// class 타입 지정 가능
class User {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}
