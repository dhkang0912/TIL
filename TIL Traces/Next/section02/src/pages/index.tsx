import { ReactNode } from "react";
import style from "./index.module.css";
import SearchableLayout from "@/components/searchable-layout";
export default function Home() {
  return (
    <>
      <h1 className={style.h1}>인덱스</h1>
    </>
  );
}

// JS에서 함수는 모두 사실 상 객체이기 때문에 메서드를 추가할 수 있음
// Home이라는 함수에 layout을 가져오는 메서드를 추가함
Home.getLayout = (page: ReactNode) => {
  return <SearchableLayout>{page}</SearchableLayout>;
};
