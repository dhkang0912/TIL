## 목차
- [목차](#목차)
  - [12강 API Routes](#12강-api-routes)
  - [13강 스타일링](#13강-스타일링)
  - [14강 글로벌 레이아웃 설정하기](#14강-글로벌-레이아웃-설정하기)
    - [1) App.tsx](#1-apptsx)
    - [2) global-layout.tsx](#2-global-layouttsx)
  - [15강 페이지별 레이아웃 설정하기](#15강-페이지별-레이아웃-설정하기)
    - [1) 특정 원하는 레이아웃을 입히고 싶은 영역에 getLayout이라는 함수를 작성해주기](#1-특정-원하는-레이아웃을-입히고-싶은-영역에-getlayout이라는-함수를-작성해주기)
    - [2) App.tsx](#2-apptsx)

### 12강 API Routes
- Next.js에서 API를 구축할 수 있게 하는 기능
- src/pages/api 내부에서 ts 파일을 만들게 되면 동작하게 됨
- /api/hello로 접속한 경우 json 데이터를 확인할 수 있음
- 자주 사용되지 않는 기능으로 더 자세한 사항은 next 공식 문서를 통해 확인 가능
```js
// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";

type Data = {
  name: string;
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>,
) {
  res.status(200).json({ name: "John Doe" });
}
```

### 13강 스타일링
- 별로의 파일에서 css를 import해서 불러오는 경우 App 컴포넌트가 아닌 경우 모두 제한되어 에러가 남
  - 다른 컴포넌트에서 import하는 경우 css 충돌이 발생할 수 있기 때문 
- 모든 컴포넌트에서 css의 이름이 중복되는 것을 방지하기 위해 next에서는 css module을 제공함
- ```파일명.module.css``` 라고 css 파일명을 설정하면 됨
  - 이렇게 하면 next에서 각 css 명을 unique하게 변경해줌
  - import 방법은 동일
    - ```import style from './index.module.css'```


### 14강 글로벌 레이아웃 설정하기
- ```src/styles/global.css``` 경로에서 글로벌 css를 설정할 수 있음
- app에 있는 요소들에 GlobalLayout 컴포넌트를 만들어 입혀주면 컴포넌트화 할 수 있어서 좋음

#### 1) App.tsx
```js
import GlobalLayout from "@/components/global-layout";
import "@/styles/globals.css";
import type { AppProps } from "next/app";

// App.tsx로 페이지 컴포넌트와 그 내용들을 받아서 렌더링함
// App이 최상단으로 그 하위 컴포넌트로 페이지들이 들어가게 됨
export default function App({ Component, pageProps }: AppProps) {
  return (
    <GlobalLayout>
       <Component {...pageProps} />
    </GlobalLayout>
  );
}
```
- global-layout을 컴포넌트화한 후 페이지의 내용들을 children으로 받으면 됨

#### 2) global-layout.tsx
```js
import { ReactNode } from "react";
import style from "./global-layout.module.css";
import Link from "next/link";

export default function GlobalLayout({ children }: { children: ReactNode }) {
  return (
    <div className={style.container}>
      <header className={style.header}>
        <Link href={"/"}>📚 ONE BITE BOOKS </Link>
      </header>
      <main className={style.main}>{children}</main>
      <footer className={style.footer}>제작 @sarah </footer>
    </div>
  );
}
```

### 15강 페이지별 레이아웃 설정하기
#### 1) 특정 원하는 레이아웃을 입히고 싶은 영역에 getLayout이라는 함수를 작성해주기
```js
// JS에서 함수는 모두 사실 상 객체이기 때문에 메서드를 추가할 수 있음
// Home이라는 함수에 layout을 가져오는 메서드를 추가함
Home.getLayout = (page: ReactNode) => {
  return <SearchableLayout>{page}</SearchableLayout>;
};
```
  - 위와 같이 하면 해당 페이지를 렌더링할 때 ```Home.getLayout``` 까지 함께 인식

#### 2) App.tsx
```js
// NextPage 타입에 추가
type NextPageWithLayout = NextPage & {
  getLayout?: (page: ReactNode) => ReactNode;
};

// App.tsx로 페이지 컴포넌트와 그 내용들을 받아서 렌더링함
// App이 최상단으로 그 하위 컴포넌트로 페이지들이 들어가게 됨
export default function App({
  Component,
  pageProps,
}: AppProps & {
  Component: NextPageWithLayout;
}) {
  // Component.getLayout가 있다면 Component.getLayout를 반환하고
  // 없다면 undefined로 page를 그대로 반환하게 하는 함수
  const getLayout = Component.getLayout ?? ((page: ReactNode) => page);
  return <GlobalLayout>{getLayout(<Component {...pageProps} />)}</GlobalLayout>;
}
```
- getLayout 함수를 통해서 개별 레이아웃을 입히는 함수를 불러오고 이를 페이지가 렌더링될 수 있도록 넣어줌
- 타입 문제를 해결하기 위해 NextPage 타입에 getLayout의 타입을 추가해줌


