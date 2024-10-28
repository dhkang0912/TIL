import GlobalLayout from "@/components/global-layout";
import "@/styles/globals.css";
import { NextPage } from "next";
import type { AppProps } from "next/app";
import { ReactNode } from "react";

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
