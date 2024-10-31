"use client";

import { useRouter } from "next/navigation";
import { startTransition, useEffect } from "react";

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  const router = useRouter();

  useEffect(() => {
    console.error(error.message);
  }, [error]);

  return (
    <div>
      <h3>오류가 발생했습니다.</h3>
      {/* reset은 서버 컴포넌트를 다시 실행하지는 않음, 클라이언트 컴포넌트 내부 오류만 복구 가능 */}
      {/* <button onClick={() => reset()}>다시 시도</button> */}
      {/* <button onClick={() => window.location.reload()}>다시 시도</button> */}
      <button
        onClick={() => {
          // 현재 페이지에 필요한 서버 컴포넌트들을 다시 실행해주는 기능을 함
          // 서버 컴포넌트 재렌더링
          // startTransition는 안의 컴포넌트를 일괄적으로 수정해줌
          startTransition(() => {
            router.refresh;
            // 에러 상태를 초기화, 컴포넌트들을 다시 렌더링
            reset();
          });
        }}
      >
        다시 시도
      </button>
    </div>
  );
}
