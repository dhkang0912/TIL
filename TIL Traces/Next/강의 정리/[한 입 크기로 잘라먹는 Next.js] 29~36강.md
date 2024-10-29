# 목차
- [목차](#목차)
  - [30강 App router에서 페이지 라우팅 설정하기](#30강-app-router에서-페이지-라우팅-설정하기)
    - [query params](#query-params)
    - [url parameter](#url-parameter)
  - [31강 App router에서 layout 설정하기](#31강-app-router에서-layout-설정하기)
    - [특정한 경로만 동일한 레이아웃을 지정하기](#특정한-경로만-동일한-레이아웃을-지정하기)
  - [32강 리액트 서버 컴포넌트 이해하기](#32강-리액트-서버-컴포넌트-이해하기)
      - [React Server Component](#react-server-component)
      - [Client Component](#client-component)
      - [컴포넌트](#컴포넌트)
  - [33강 리액트 서버 컴포넌트 주의사항](#33강-리액트-서버-컴포넌트-주의사항)
  - [36강 네비게이팅](#36강-네비게이팅)
      - [Programmatic routing](#programmatic-routing)
## 30강 App router에서 페이지 라우팅 설정하기
![!\[alt text\](image.png)](<App router-페이지 라우팅 설정.png>)
- url 주소가 되고 싶은 폴더를 만들고 page.tsx라는 파일을 반드시 만들어줘야 함
- page router와 다르게 app router에서는 폴더가 필수고 하위에 반드시 page.tsx라는 이름으로 파일을 만들어줘야 함

### query params
- app router에서 query는 page.tsx의 props로 받게 되고 이 타입은 promise 타입임
- 서버 컴포넌트의 경우 함수형 컴포넌트에 async를 붙일 수 있음
```js
export default async function page({
  searchParams,
}: {
  searchParams: Promise<{ q: string }>;
}) {
  const {q}=await searchParams
  return <div>search 페이지 : {q}</div>;
}
```

### url parameter
- parameter 역시 props로 받게 되며, 구조분해 할당을 통해 가져올 수 있음
- 이 또한 promise 타입
```js
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  return <div>book/[id] 페이지 : {id}</div>;
}
```

- catch all segment : [...id]
  - 여러개의 parameter를 전달해도 다 받아올 수 있음
- optional all segment : [[...id]] 
  - params가 없더라도 에러가 나지 않고 페이지를 반환해줌

## 31강 App router에서 layout 설정하기
- 폴더 안에  ```layout.tsx```를 추가하면 해당 폴더의 모든 경로의 layout이 됨
- app 폴더 안 layout은 global layout으로 만약 삭제하거나 이름을 변경한 경우 자동으로 생성됨
```js
import { ReactNode } from "react";

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <div>
      <div>임시 서치바</div>
      {children}
    </div>
  );
}
```
- layout이 씌워지는 페이지는 children으로 받아서 어디에 렌더링될지를 정해줘야 함
- 폴더 안 폴더를 통해 경로가 존재하다면 중첩 레이아웃도 가능

### 특정한 경로만 동일한 레이아웃을 지정하기
- Route group
  - 폴더 명을 소괄호로 묶게 되면 경로 상에 아무런 영향을 주지 않음
    - 예 : (with-searchbar)
  - 파일들을 모아서 route group 안에 넣고 layout 파일을 넣게 되면 경로에는 영향을 주지 않지만 동일한 layout이 적용됨

## 32강 리액트 서버 컴포넌트 이해하기
#### React Server Component
- 리액트 18v부터 새롭게 추가된, 새로운 유형의 컴포넌트
- ***서버 측에서만 실행되는 컴포넌트 (브라우저에서 실행 X)***  
  - 서버에서만 실행되고 클라이언트에서 실행되지 않기 때문에 보안적인 문제가 발생하지 않음
  - 대신 브라우저에서만 실행 가능한 리액트 hooks를 사용하면 에러가 남

- 기존 페이지 라우터는 상호작용이 필요없는 컴포넌트도 JS Bundle에 포함되어 수화하게 되고 TTI까지 시간이 길어짐
- 서버 측에서 사전 렌더링될 때만 실행하고 JS Bundle한 후 수화할 때는 렌더링을 하지 않음


- 클라이언트 컴포넌트만 JS Bundle에 포함하고 서버에서만 실행되는 서버 컴포넌트는 제외
- 페이지의 대부분을 서버 컴포넌트로 구성하고 필요한 경우에만 클라이언트 컴포넌트로 구성하는 것을 권장함

#### Client Component
- ```"use client"```라는 지시자를 tsx 파일 안에 작성해주면 Client Component로 변경 가능
  - 기본은 서버 컴포넌트
- Client component의 경우 기본적으로 서버에서 한번 (사전 렌더링), 클라이언트에서 한번 실행됨 (hydration)
- UseEffect와 같은 브라우저에서 사용하는 리액트 훅 사용 가능
- 상호작용이 있으면 client component로 만들어주면 됨

#### 컴포넌트
- app 안에서도 파일의 이름이 page.tsx나 layout.tsx가 아니면 일반적인 컴포넌트로 인식함
- 컴포넌트도 페이지 파일과 같은 폴더 안에 넣어놓으면 됨 => co-Location이라는 특징

## 33강 리액트 서버 컴포넌트 주의사항
1. 서버 컴포넌트에는 브라우저에서 실행될 코드가 포함되면 안됨
   - 만약 라이브러리가 브라우저에서 실행될 경우 서버 컴포넌트이면 에러가 날 수 있음
2. 클라이언트 컴포넌트는 클라이언트에서만 실행되지 않음
   - 서버에서 사전렌더링을 위해 실행되고, 하이드레이션을 위해 브라우저에서도 실행됨
   - 서버와 클라이언트에서 한번씩 모두 실행됨

3. 클라이언트 컴포넌트에서 서버 컴포넌트를 import 할 수 없음
   - 클라이언트 컴포넌트 코드 : 서버와 브라우저에서 모두 실행됨
   - 서버 컴포넌트 코드 : 오직 서버에서만 실행됨
    => 서버 컴포넌트를 클라이언트 컴포넌트에서 열려고 하면 자동으로 리액트가 서버 컴포넌트를 클라이언트 컴포넌트로 변경됨
      - 이 경우 하위 컴포넌트로 렌더링하는게 아니라 상위에서 children으로 넘겨주는게 좋음
      - children으로 넘겨주면 client component로 자동으로 변경시키지 않음, 내용만 받아서 넘김
``` js
import ClientComponent from "./client-component";
import styles from "./page.module.css";
import ServerComponent from "./server-component";

export default function Home() {
  console.log("Home 컴포넌트 실행");

  const secretKey = "qwer123";

  return <div className={styles.page}>인덱스 페이지
    {/* server component */}
  <ClientComponent>
    <ServerComponent/>
  </ClientComponent>
  </div>;
}

```
```js
// Client component
"use client";

import { ReactNode } from "react";

export default function ClientComponent({ children }: { children: ReactNode }) {
  console.log("클라이언트 컴포넌트");

  return <div>{children}</div>;
}
```
4. 서버 컴포넌트에서 클라이언트 컴포넌트에게 직렬화 되지 않는 Props는 전달 불가
   - 직렬화 (serialization) : 객체, 배열, 클래스 등의 복잡한 구조의 데이터를 네트워크 상으로 전송하기 위해 아주 단순한 형태(문자열, byte)로 변환하는 것
   - 자바스크립트의 함수는 직렬화가 불가능 (다양한 환경에 의존해있음)
   - 직렬화가 되어있지 않은 함수의 경우 props로 전달 불가

   - 사전 렌더링 시 SC가 먼저 따로 실행된 이후 CC가 실행됨
     - SC가 먼저 실행되면 RSC payload라는 json과 비슷한 형태의 문자열 생성됨
     - RSC : React Server Component의 순수한 데이터(결과물), 직렬화한 결과
       - 서버 컴포넌트의 모든 데이터가 포함됨
       - 서버 컴포넌트의 렌더링 결과
       - 연결된 클라이언트 컴포넌트의 위치
       - 클라이언트 컴포넌트에게 전달하는 Props 값

    - 이후 CC를 실행하여 모두 실행하게 됨
      - 만약 함수 형태로 SC가 CC에게 함수 형태로 props를 넘겨주게 되면 직렬화(RSC payload)로 전달되지 못함 => 런타임 에러가 남

## 36강 네비게이팅
- 초기 접속 이후 페이지 이동은 CSR로 진행됨
- 이동할 수 있는 모든 파일을 먼저 불러와서(Pre-fetching) 렌더링함
- Pre-fetching 시 JS Bundle(서버 컴포넌트 정보는 제외)과 함께 RSC Payload(서버 컴포넌트 정보 전달을 위해)도 함께 전달함 => JS 실행(컴포넌트 교체) => 페이지 교체
- 만약 SC만 있는 경우 RSC Payload만 전달하고 CC인 경우 JS Bundle과 RSC Payload를 같이 불러옴

#### Programmatic routing
- navigation에서 import 해야와야 함
```js
import { useRouter } from "next/navigation";
```
- Dynamic Page : 브라우저의 요청을 받을 때마다 생성되는 페이지 (Like SSR)
  - url parameter, query string, dynamic routing을 사용하는 경우 Dynamic Page로 됨
  - 이에 따라 Pre-fetching이 달라짐
  - 향후 데이터 업데이트가 필요할 수도 있으니 JS Bundle을 제외한 RSC만 불러옴 
    - Static Page의 경우 RSC와 JS Bundle을 Pre-fetching함



