## 목차
- [목차](#목차)
  - [17강 사전 렌더링과 데이터 페칭](#17강-사전-렌더링과-데이터-페칭)
    - [리액트 VS 넥스트](#리액트-vs-넥스트)
    - [Next의 3가지 사전 렌더링 방식](#next의-3가지-사전-렌더링-방식)
  - [18강 서버 사이드 렌더링 (SSR)](#18강-서버-사이드-렌더링-ssr)
    - [getServerSideProps의 타입 추론하기](#getserversideprops의-타입-추론하기)
    - [비동기 함수 병렬 실행법](#비동기-함수-병렬-실행법)
    - [GetServerSidePropsContext](#getserversidepropscontext)
    - [GetServerSideProps와 GetServerSidePropsContext](#getserversideprops와-getserversidepropscontext)
  - [20강 SSG 소개](#20강-ssg-소개)
    - [SSR](#ssr)
    - [SSG (Static Site Generation) - 정적 사이트 생성](#ssg-static-site-generation---정적-사이트-생성)
    - [SSG의 단점](#ssg의-단점)
  - [21강 SSG - 정적 경로에 적용하기](#21강-ssg---정적-경로에-적용하기)
  - [22강 SSG - 동적 경로에 적용하기](#22강-ssg---동적-경로에-적용하기)
  - [23강 SSG 실습 - Fallback 옵션 설정하기](#23강-ssg-실습---fallback-옵션-설정하기)
  - [Fallback 옵션 - false](#fallback-옵션---false)
    - [Fallback 옵션 - blocking](#fallback-옵션---blocking)
    - [Fallback 옵션 - true](#fallback-옵션---true)
  - [24강 ISR(Incremental Static Regeneration) : 증분 정적 재 생성](#24강-isrincremental-static-regeneration--증분-정적-재-생성)
  - [25강 주문형 재검증 (On-Demand-ISR)](#25강-주문형-재검증-on-demand-isr)
  - [26강 SEO 설정하기](#26강-seo-설정하기)
  - [27강 배포하기](#27강-배포하기)
  - [28강 페이지 라우터 정리](#28강-페이지-라우터-정리)
    - [Page router의 장점](#page-router의-장점)
    - [Page router의 단점](#page-router의-단점)

### 17강 사전 렌더링과 데이터 페칭
#### 리액트 VS 넥스트
- React App의 데이터 페칭
  - 컴포넌트 마운트 이후에 발생함
  - 데이터 요청 시점이 느려지게 되는 단점 발생
  ![!\[alt text\](image.png)](<리액트에서 데이터 페칭.png>)
- Next App의 데이터 페칭
  - 사전 렌더링 중 발생 (당연히 컴포넌트 마운트 이후에도 발생 가능)
  - 데이터 요청 시점이 매우 빨라지는 장점이 있음
  - 만약 사전 렌더링이 너무 오래 걸릴 것으로 예상되면 빌드 타임에 미리 사전 렌더링을 맞춰둘 수도 있고 요청이 들어왔을 때 렌더링하도록 할 수도 있음
  ![!\[alt text\](image.png)](<넥스트에서 데이터 페칭.png>)

#### Next의 3가지 사전 렌더링 방식
1. 서버사이드 렌더링 (SSR)
   - 가장 기본적인 사전 렌더링 방식
   - 요청이 들어올 때마다 사전 렌더링을 진행
2. 정적 사이트 생성 (SSG)
   - 방금 살펴본 사전 렌더링 방식
   - 빌드 타임에 미리 페이지를 사전 렌더링 해 둠
3. 증분 정적 재생성 (ISR)
   - 향후 다룰 사전 렌더링 방식

### 18강 서버 사이드 렌더링 (SSR)
- 브라우저에 요청이 들어올 때마다 사전 렌더링하는 방식
- ```export const getServerSideProps = () => {};```
  - 컴포넌트보다 먼저 실행되어서, 컴포넌트에 필요한 데이터를 불러오는 함수
  - 서버 측에서 실행되기 때문에 한번만 동작되고 브라우저에서 동작되는 동작은 작동하지 않음
  - 해당 컴포넌트는 서버에서 한번 동작되고 js Bundle을 통해 hydration이 동작될 때 한번 동작되어 총 2번 동작되게 됨
    - 만약 브라우저에서만 동작되는 함수를 사용하고 싶은 경우 useEffect를 사용하여 마운트될 때 실행되는 코드를 추가하면 됨
```js
export const getServerSideProps = () => {
  const data = "hello";

  return {
    props: {
      data,
    },
  };
};
```
- 무조건 return 객체 안에 props 객체가 있고 그 안에 컴포넌트에서 사용될 정보를 넣어줘야 함

#### getServerSideProps의 타입 추론하기
- ```InferGetServerSidePropsType<typeof getServerSideProps>)``` 을 통해 자동으로 getServerSideProps의 props 타입 추론 가능
- 이를 통해 타입 오류 해결 가능

#### 비동기 함수 병렬 실행법
- 인수로 전달한 배열 안에 들어있는 모든 비동기 함수들을 동시에 실행시킴
```js
const [allBooks, recoBooks] = await Promise.all([
    fetchBooks(),
    fetchRandomBooks(),
  ]);
```

#### GetServerSidePropsContext
- context에는 현재 브라우저에서 받은 요청에 대한 모든 정보가 다 담겨있음
```js
export const getServerSideProps = async (
  context: GetServerSidePropsContext
) => {
  const q = context.query.q
  const books = await fetchBooks(q as string)
  return {
    props: {books},
  };
};

export default function Page({books}:InferGetServerSidePropsType<typeof getServerSideProps>) {
  return (
    <div>
      {books.map((book) => (
        <BookItem key={book.id} {...book} />
      ))}
    </div>
  );
}
```

#### GetServerSideProps와 GetServerSidePropsContext
- 브라우저에서 받은 요청에 대한 정보가 필요없이 api 호출을 통해서 나온 데이터들을 전달하기만 할 때는 ***GetServerSideProps*** 사용
- 브라우저에서 받은 정보들을 사용하여 api를 호출하거나 렌더링되는 정보가 다른 경우 ***GetServerSidePropsContext*** 사용


### 20강 SSG 소개
#### SSR
![!\[alt text\](image.png)](<SSR 동작.png>)
- 장점 : 접속 요청 후 정보를 가져오기 때문에 항상 최신 정보를 가지고 있을 수 있음
- 단점 : 대신 서버 상태가 안 좋거나 주고 받아야 하는 데이터 용량이 크다면 사용자가 브라우저 로딩을 기다려야 하는 시간이 길어짐

#### SSG (Static Site Generation) - 정적 사이트 생성
- SSR의 단점을 해결하는 사전 렌더링 방식
- 빌드 타임에 페이지를 미리 사전 렌더링 해 둠
- 접속 요청이 발생하면 렌더링된 HTML을 서버가 브라우저에 전달하고 화면에 렌더링이 됨
- 빌드타임에 사전 렌더링이 필요하더라도 서버 가동되기 전인 빌드타임에 작동되기 때문에 사용자의 FCP가 매우 빠르게 진행됨
![!\[alt text\](image.png)](<SSG 동작 방식.png>)

#### SSG의 단점
- 매번 똑같은 페이지만 응답함, 최신 데이터 반영은 어려움


### 21강 SSG - 정적 경로에 적용하기
- 페이지로 만들었지만 설정을 안 한 것들은 SSG와 동일하게 동작함
  - 빌드를 했을 때 하얀 빈 동그라미 기호와 함께 'Static'으로 나옴

```js
export const getStaticProps = async () => {
  console.log("인덱스 페이지");

  // 인수로 전달한 배열 안에 들어있는 모든 비동기 함수들을 동시에 실행시킴
  const [allBooks, recoBooks] = await Promise.all([
    fetchBooks(),
    fetchRandomBooks(),
  ]);
  return {
    props: {
      allBooks,
      recoBooks,
    },
  };
};

export default function Home({
  allBooks,
  recoBooks,
}: InferGetStaticPropsType<typeof getStaticProps>) {
  return ()
```
- 브라우저에서 정보를 받아서 api를 부르는게 아니라면 getStaticProps로 함수명과 타입명만 수정해주면 됨

```js
const fetchSearchResult = async()=>{
    const data = await fetchBooks(q as string)
    setBooks(data)
  }

  useEffect(()=>{
    if(q){
      fetchSearchResult()
    }
  },[])
```
- 만약 브라우저에서 정보를 받아서 api를 불러야 하는 경우 (query params를 이용하는 경우, context를 사용하는 경우)에는 기본적인 SSG 렌더링이 되게 하고, 리액트에서 했던 것처럼 렌더링된 이후 CSR 상태에서 api를 호출하면 됨

### 22강 SSG - 동적 경로에 적용하기
- 동적 경로를 갖게 되는 경우 id에 따라 여러개의 경로를 가질 수 있음
- 백에서 동적 경로를 받아오는 것이지 브라우저와 상호작용해서 알게 되는 것이 아니라 ```GetStaticPropsContext```을 통해서 설정 가능
- 빌드 타임에 사전렌더링하기 위해서는 선수 과정으로 존재할 수 있는 경로들을 설정하는 과정이 필요함
  - 이를 설정해주면 가능한 모든 페이지들을 미리 렌더링해놓게 됨
- 이후에는 이미 렌더링된 페이지들을 빠르게 전달해줌
  => 설정을 하는 방법이 ```getStaticPaths```

- url parameter 값은 반드시 문자열이어야 함
- fallback 옵션을 함께 설정해줘야 함 (대체 값)
  - false : 존재 하지 않는 사전 설정값은 존재하지 않는 페이지로 인식
  - true : 즉시 생성 + 페이지만 미리 반환
  - blocking : 즉시 생성 (like SSR)

```js
export const getStaticPaths = () => {
  return {
    paths: [
      { params: { id: "1" } },
      { params: { id: "2" } },
      { params: { id: "3" } },
    ],
    fallback: false,
  };
};

export const getStaticProps = async (context: GetStaticPropsContext) => {
  const id = context.params!.id;
  const book = await fetchOneBook(Number(id));
  return {
    props: { book },
  };
};

```

### 23강 SSG 실습 - Fallback 옵션 설정하기
- fallback 옵션을 함께 설정해줘야 함 (대체 값)
  - false : 존재 하지 않는 사전 설정값은 존재하지 않는 페이지로 인식
  - true : 즉시 생성 + 페이지만 미리 반환
  - blocking : 즉시 생성 (like SSR)

### Fallback 옵션 - false
-  설정하지 않은 방식인 경우 404 Notfound를 띄워줌

#### Fallback 옵션 - blocking
- 이미 사전에 설정하지 않은 path더라도 SSG로 생성하여 새로운 path를 만들어줌
  - 한번 생성된 페이지는 next 서버에 존재하기 때문에 페이지를 새로 생성하지 않고 빠른 속도로 렌더링됨
  - SSG + SSR
  - ![!\[alt text\](image.png)](<fallback-blocking 옵션.png>)
- 대신 백엔드 서버에 받아와야 하는 내용이 많다면 새로 생성하여 정보를 보여주기 전까지 로딩이 걸림

#### Fallback 옵션 - true
- ![!\[alt text\](image.png)](<fallback-true 옵션.png>)
- blocking 옵션의 단점인 로딩을 해결하기 위해 우선 props가 없는 페이지를 반환함
- 이후 props만 먼저 계산하여 데이터만 다시 보내줌
- 즉, UI를 먼저 렌더링하고 데이터를 나중에 다시 보내주는 것

### 24강 ISR(Incremental Static Regeneration) : 증분 정적 재 생성
![!\[alt text\](image.png)](<ISR 동작방식.png>)
- SSG 방식으로 생성된 정적 페이지를 일정 시간을 주기로 다시 생성하는 기술
- 사전에 생성된 페이지만 반환되어 속도는 빠르지만 최신 데이터를 적용하기 어려움 => 이를 해소하기 위해 ISR을 사용
- ISR을 사용하면 유효기간을 지정하여 그 이후부터는 다시 페이지를 정적으로 생성하면서 새로 업데이트 된 페이지를 가져올 수 있음
  - 만약 유효기간이 60초라면 60초 이후에 첫 요청 시 이전과 동일한 페이지를 반환하고 그 이후 서버에 새로 생성하도록하여 업데이트된 방식을 반영하여 반환하게 됨
- 매우 빠른 속도로 응답이 가능한 SSG 방식의 장점 + 최신 데이터 반영 가능한 SSR 방식의 장점
```js
export const getStaticProps = async () => {
  console.log("인덱스 페이지");

  // 인수로 전달한 배열 안에 들어있는 모든 비동기 함수들을 동시에 실행시킴
  const [allBooks, recoBooks] = await Promise.all([
    fetchBooks(),
    fetchRandomBooks(),
  ]);
  return {
    props: {
      allBooks,
      recoBooks,
    },
    // 이렇게 재검증하는 유효기간을 정해주면 그 기간이 지나면 다시 SSG 방식으로 페이지를 반환한다
    // 어떻게 보면 리액트 쿼리랑 비슷한 방식이라고 느껴진다.
    revalidate:3,
  };
};
```

### 25강 주문형 재검증 (On-Demand-ISR)
- 요청을 받을 때마다 페이지를 다시 생성하는 ISR
- 페이지의 업데이트를 직접 트리거링  해줄 수 있음
- 아래와 같이 특정 api를 호출했을 때 (api/revalidate) 특정한 페이지가 재생성되게 하여 업데이트된 페이지를 반환하게 할 수 있음
  - 개인적으로 진짜 리액트 쿼리 revalidate 하는 방식과 동일하다고 느낌
```js
import { NextApiRequest, NextApiResponse } from "next";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    await res.revalidate("/ ");
    return res.json({ revalidate: true });
  } catch (err) {
    res.status(500).send("Revalidation Failed");
  }
}
```

### 26강 SEO 설정하기
- ```import Head from "next/head";``` 이걸 추가하고 return되는 UI 제일 상단에 <HEAD></HEAD>를 활용하여 meta 데이터 작성
- 로딩 중이더라도 기본적인 메타 태그들이 보일 수 있도록 설정
```js
export default function Page({
  book,
}: InferGetStaticPropsType<typeof getStaticProps>) {
  const router = useRouter();
  if (router.isFallback) {
    return (
      // 로딩 중이더라도 기본적인 메타 태그들이 보일 수 있게 설정
      <>
        <Head>
          <title>한입 북스</title>
          <meta property="og:image" content="/thumbnail.png" />
          <meta property="og:title" content="한입북스" />
          <meta
            property="og:description"
            content="한입북스에 등록된 도서들을 만나보세요 "
          />
        </Head>
        <div>"로딩 중입니다"</div>
      </>
    );
  }
  if (!book) return "문제가 발생했습니다 다시 시도하세요";
  ```

### 27강 배포하기
- ```npm install -g vercel```
- ```vercel login```
- ```vercely```
- ```vercel --prod```

### 28강 페이지 라우터 정리
#### Page router의 장점
- 파일 시스템 기반의 간편한 페이지 라우팅 제공
- 다양한 방식의 사전 렌더링 제공
  1. 서버 사이드 렌더링 (SSR)
   - 요청이 들어올 때마다 사전 렌더링을 진행함
  2. 정적 사이트 생성 (SSG)
   - 빌드 타임에 미리 사전 렌더링을 해놓음
  3. 증분 정적 재생성 (ISR)
   - SSG 페이지를 일정 시간마다 재생성

#### Page router의 단점
- 페이지별 레이아웃 설정이 번거로움
- 데이터 페칭이 페이지 컴포넌트에 집중됨 
  - (데이터 페칭을 페이지에서 받아와서 하단의 자식 컴포넌트들에 props로 모두 넘겨줘야 함)
- 불필요한 컴포넌트들도 JS Bundle에 포함됨
  - 상호작용이 필요하지 않고 단순히 UI 렌더링만 해도 되는 컴포넌트도 사전 렌더링을 위해 실행하면서 JS를 실행하고 수화 과정에서 한번 더 실행하게 됨