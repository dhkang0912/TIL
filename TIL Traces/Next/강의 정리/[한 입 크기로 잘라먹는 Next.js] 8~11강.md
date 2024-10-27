## 목차
- [목차](#목차)
  - [8강 Page Router](#8강-page-router)
  - [Next 프로젝트 생성하기](#next-프로젝트-생성하기)
  - [Page router](#page-router)
    - [\_app.tsx](#_apptsx)
    - [useRouter](#userouter)
    - [Dynamic Routing](#dynamic-routing)
    - [에러 페이지](#에러-페이지)
  - [10강 네비게이팅](#10강-네비게이팅)
    - [Link](#link)
    - [Programmatic navigation](#programmatic-navigation)
  - [11강 프리페칭](#11강-프리페칭)
    - [Pre-fetching](#pre-fetching)
    - [이미 초기 접속 요청이 완료되어서 페이지가 렌더링 됐는데 왜 pre-fetching이 필요할까?](#이미-초기-접속-요청이-완료되어서-페이지가-렌더링-됐는데-왜-pre-fetching이-필요할까)
    - [Programmatic navigation에서 pre-fetching하기](#programmatic-navigation에서-pre-fetching하기)

### 8강 Page Router
- 폴더 구조로 url 페이지 라우팅이 생김
- 동적 경로(Dynamic Routes)도 쉽게 만들 수 있음
  - 폴더 경로 하위에 [id].js와 같이 생성하면 id라는 동적 경로에 대응하는 페이지 라우팅이 생김

### Next 프로젝트 생성하기
``` js
npx create-next-app@latest [프로젝트 이름]
```
- NPX : Node Package Executor
  - NPM에 올라가 있는 최신 버전의 노드 패키지를 다운로드 없이 바로 실행시키는 명령어

### Page router
#### _app.tsx
- 리액트의 App.tsx와 대응되는 파일
- 페이지 컴포넌트와 그 내용들을 받아서 렌더링함
- App이 최상단으로 그 하위 컴포넌트로 페이지들이 들어가게 됨

#### useRouter
- query parameter를 불러올 수 있음
- 페이지 라우터 방식의 경우 useRouter를 router에서 불러와야 함
  - 앱 라우터 방식의 경우 navigator에서 불러옴

#### Dynamic Routing
- query Parameter에 동적인 변수가 들어가는 경우 파일명을 [변수명].tsx로 하면 됨
- 만약 다양한 query를 받는다면 [...변수명].tsx를 하면 됨
  - 이 경우 router의 query에 배열로 저장됨
  => catch all segment라고 함
  
- 이렇게 한 경우 query parameter가 없는 경우 에러가 뜸
  - 더 범용적으로 사용하고 에러가 안 뜨고 싶으면 [[...변수명]].tsx로 작성하면 됨
  => optional catch all segment 라고 함

#### 에러 페이지
- 404 에러 페이지에 대응하는 페이지의 경우 404.tsx로 만들어주면 됨


### 10강 네비게이팅
#### Link
- Link를 import하여 CSR 방식으로 페이지를 이동할 수 있음

#### Programmatic navigation
- 함수 실행 혹은 이벤트 발생 시 특정 조건이 만족할 때 페이지를 이동할 수 있음
- ```router.push("/이동할 페이지");``` 를 통해 이동시킬 수 있음
- replace(뒤로 가기 방지하며 페이지 이동)와 back(뒤로 가기) 기능도 존재

### 11강 프리페칭
#### Pre-fetching
- 사전에, 미리 불러온다는 뜻을 가짐
- 현재 사용자가 보고 있는 페이지에서 연결되어있는 링크를 미리 불러오는 기능
- 현재 페이지에서 이동할 수 있는 모든 페이지를 미리 렌더링해놓음
- 초기 접속 경험은 더 빠르고 이후 SSR로 연결되어 넘어가는 링크도 빠르게 느껴질 수 있게 해줌
  - 이미 연결된 페이지를 미리 JS Bundle로 가져오기 때문에 이동이 빠름
- pre-fetching은 npm run dev에서는 확인 불가능 build 후 npm run start 해볼 것

#### 이미 초기 접속 요청이 완료되어서 페이지가 렌더링 됐는데 왜 pre-fetching이 필요할까?
- next의 리액트 컴포넌트를 페이지 별로 split해서 가지고 있음
- 초기 렌더링 시 모든 페이지의 JS Bundle이 전달되는 게 아니라 pre-fetching을 통해 연결되어있는 페이지와 초기 접속한 페이지의 JS Bundle만 보내줌 
- 이를 위해서 pre-fetching이 필요함
![!\[alt text\](image.png)](<pre-fetching 동작 방식.png>)

#### Programmatic navigation에서 pre-fetching하기
- Link 태그로 네비게이팅하는 경우 자동으로 pre-fetching을 해옴
  - 만약 Link 태그로 네비게이팅 될 때 자동으로 pre-fetcing을 하고 싶지 않다면 false로 바꿔줌
  ```js 
    <Link href={"/search"} prefetch={false}>
    search
    </Link>
  ```
- 하지만 Programmatic navigation을 하는 경우 pre-fetcing을 기본으로 해오지 않음
- 이를 원한다면 마운트 될 때 pre-fetching 해오도록 직접 설정해줘야 함
```js
useEffect(() => {
    router.prefetch("/test");
  }, []);
```



