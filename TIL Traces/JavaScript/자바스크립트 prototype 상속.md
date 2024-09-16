## 절차지향 프로그램 방식

- 개발자가 프로그래밍할 내용의 논리를 세운 순서대로 구성하는 방식
    
    ⇒ 일련의 절차대로 구성하는 방식
    
- 절차 지향 프로그래밍은 프로그래밍할 데이터를 처리할 함수를 중심으로 코드를 작성하고 그 함수에 데이터를 처리하는 방식

```jsx
let carName = "포르쉐";
let carModel = "911 타르가";
let carColor = "white";

const startCar = name => {
    console.log(`${name} 출발`);
}

const helloCar = (name, model, color) => {
    const hello = `제 차의 이름은 ${name}이고 모델명은 ${model}입니다. 색상은 ${color}입니다.`;
    console.log(hello);
}

const drvingCar = name => {
    console.log(`${name} 운전!`);
}

// 예제 사용
startCar(carName); // 출력: "포르쉐 출발"
helloCar(carName, carModel, carColor); // 출력: "제 차의 이름은 포르쉐이고 모델명은 911 타르가입니다." 색상은 white입니다.
drvingCar(carName); // 출력: "포르쉐 운전!"
```

## 객체 지향 프로그래밍 방식

- 절차 지향 프로그래밍은 코드를 모듈화하기 어렵고 한번 작성한 코드를 재사용하기 어려움, 기능을 변경하거나 수정할 때 유지보수가 어려움 ⇒ 객체 지향 프로그래밍으로 넘어감
- **객체 지향 프로그래밍**이란 사람이 인식하거나 파악하기 쉬운 현실 세계의 사물이나 개념 (혹은 집합)을 프로그램 내에서 적용한 것

<aside>
💡

자동차는 현실 세계의 사물입니다. 

자동차는 엔진, 바퀴, 좌석 등과 같은 여러 개의 구성 요소를 가지고 있습니다. 
또한, 자동차는 주행, 정지, 회전 등과 같은 여러 가지 기능을 가지고 있습니다. 

객체 지향 프로그래밍에서는 자동차를 객체로 표현합니다. 자동차 객체는 엔진, 바퀴, 좌석 등과 같은 속성을 가지고 있습니다. 

또한, 자동차 객체는 주행, 정지, 회전 등과 같은 메서드(객체에 포함되어 있는 함수)를 가지고 있습니다.

</aside>

```jsx
// Car 객체 생성자 함수
function Car(name, model, color) {
    this.name = name;
    this.model = model;
    this.color = color;
}

// Car 객체의 메서드를 프로토타입으로 정의
Car.prototype.start = function() {
    console.log(`${this.name} 출발`);
};

Car.prototype.hello = function() {
    const hello = `제 차의 이름은 ${this.name}이고 모델명은 ${this.model}입니다. 색상은 ${this.color}입니다.`;
    console.log(hello);
};

Car.prototype.drive = function() {
    console.log(`${this.name} 운전!`);
};

// 예제 사용
let myCar = new Car("포르쉐", "911 타르가", "white");

myCar.start(); // 출력: "포르쉐 출발"
myCar.hello(); // 출력: "제 차의 이름은 포르쉐이고 모델명은 911 타르가입니다. 색상은 white입니다."
myCar.drive(); // 출력: "포르쉐 운전!"
```

- 절차 지향 프로그래밍 방식에서는 개별 함수를 사용했지만 객체 지향 프로그래밍에서는 `myCar.xxxx()`로 되어 있어 "myCar의 start", "myCar의 hello", "myCar의 drive"처럼 'myCar"라는 `객체와 그 객체에 속한 함수`로 쉽게 인식할 수 있음
- 절차 지향 프로그래밍 방식은 객체 생성자 함수와 그 객체의 메서드로 작성됨

<aside>
💡

**객체란** 현실 세계의 사물이나 개념을 프로그램에서 객관적으로 표현하기 위한 그릇으로, 데이터와 그 데이터를 처리하는 함수들을 하나로 묶은 것입니다. 

예를 들어, 자동차 객체는 자동차의 속성(색상, 모델 등)과 동작(가속, 정지 등)을 가지고 있습니다. 이렇게 객체는 데이터와 해당 데이터를 다루는 함수들을 함께 가지고 있어 쉽게 관리하고 사용할 수 있습니다. 

즉, 데이터와 그 데이터를 처리하는 메서드를 포함하는 프로그래밍 요소입니다.

</aside>

## 자바스크립트 프로토타입 상속

```jsx
// 부모 객체 선언
function Animal() {
    this.name = "Animal"; // 부모 객체(Animal)가 가지고 있는 속성입니다.
}

// 부모 객체(Animal)에 프로토타입이라는 방식으로 메서드 추가
Animal.prototype.say = function() {
    console.log("I am an animal.");
};

// 자식 객체 선언
function Dog() {
    this.name = "Dog";
}

// 프로토타입이라는 방식으로 부모 객체(Animal)가 가지고 있는 속성을 자식 객체(Dog)에게 상속됩니다.
Dog.prototype = new Animal();

// 자식(Dog) 객체에서 부모 객체(Animal)의 속성과 메서드를 사용합니다.
const myDog = new Dog();
console.log(myDog.name); // 출력: "Dog"
myDog.say(); // 출력: "I am an animal."
```

1. 먼저 `Animal`이라는 부모 객체를 선언합니다. 이 객체에는 `name`이라는 속성이 정의되어 있습니다. (생성자 함수 사용)
2. `Animal.prototype`을 이용하여 부모 객체에 메서드 `say()`를 추가합니다. 이 메서드는 "I am an animal."이라는 메시지를 출력합니다.
3. 그 다음으로 `Dog`라는 자식 객체를 선언합니다. 이 객체는 부모 객체인 `Animal`을 상속받아야 합니다.
4. `Dog.prototype`을 부모 객체 `Animal`의 인스턴스로 설정하여, 부모 객체의 속성과 메서드를 자식 객체에 상속합니다.
5. `myDog`라는 객체를 생성하고, 이 객체는 `Dog`의 인스턴스입니다.
6. `myDog.name`을 출력하면 "Dog"가 나오는데, 이는 자식 객체인 `Dog`에서 `name` 속성을 상속받은 것입니다.
7. 마지막으로 `myDog.say()`를 호출하면 "I am an animal."이라는 메시지가 출력됩니다. 이는 부모 객체인 `Animal`의 메서드인 `say()`를 상속받아 사용한 것입니다.

## 프로토타입 방식이란 무엇인가?

<aside>
💡

프로토타입(Prototype)이란 무슨 뜻일까요? 사전적 의미로는 "원래의 형태 또는 원본"이라는 뜻입니다. 자바스크립트에서 "프로토타입은 객체를 만들 때 사용하는 템플릿 또는 원본"이라는 의미로 사용됩니다. 간단하게 말하면 객체의 원본이라고 생각할 수 있습니다.

</aside>

### **`prototype` 속성**

- `prototype` 속성은 자바스크립트에서 객체들 간에 속성과 메서드를 공유하기 위해 객체의 속성과 메서드를 저장하는 속성입니다.

### **`prototype` 속성의 사용 방법**

- 자바스크립트에서 객체는 `prototype`속성을 가지고 있습니다. 이 `prototype` 속성은 해당 객체의 프로토타입 객체를 가리킵니다. 프로토타입 객체에 정의된 속성과 메서드는 해당 객체를 상속받은 다른 객체들이 공유할 수 있습니다.

```jsx
function Animal(name) {
    this.name = name;
}

// Animal 생성자 함수로부터 생성된 모든 객체들이 상속받는 프로토타입 객체
Animal.prototype.speak = function() {
    console.log(`안녕하세요, ${this.name}입니다.`);
};

const dog = new Animal("멍멍이");
dog.speak(); // 출력: "안녕하세요, 멍멍이입니다."
```

## **객체 리터럴과 `Object.create()`**

- `Object.create()` 속성을 사용하여 새로운 객체를 생성하고, 이를 기존 객체의 프로토타입으로 설정함으로써 상속을 구현할 수 있습니다.

```jsx
const parent = {
    sayHello:function() {
        console.log("안녕하세요!");
    }
};

const child = Object.create(parent);
child.sayHello(); // 출력: "안녕하세요!"
```

- 위의 예제에서 `child` 객체는 `parent` 객체를 프로토타입으로 상속받았으며, `sayHello()` 메서드를 호출할 수 있습니다.

## **클래스와 `extends`**

- 클래스를 사용하여 객체를 정의하고, `extends`를 통해 다른 클래스를 상속받을 수 있습니다.

```jsx
class Animal {
    constructor(name) {
        this.name = name;
    }
    
    speak() {
        console.log(`${this.name}이 소리를 냅니다.`);
    }
}

class Dog extends Animal { // extends키워드로 Animal 클래스를 상속받음
    constructor(name, breed) {
    // 자식 클래스에서 부모 클래스의 생성자나 메서드를 호출
        super(name);
        this.breed = breed;
    }

    bark() {
        console.log(`${this.name}이 짖습니다.`);
    }
}

const myDog = new Dog("멍멍이", "리트리버");
myDog.speak(); // 출력: "멍멍이이 소리를 냅니다."
myDog.bark(); // 출력: "멍멍이이 짖습니다."
```

- 위의 예제에서 `Dog` 클래스는 `Animal` 클래스를 상속받아 사용하고 있습니다.