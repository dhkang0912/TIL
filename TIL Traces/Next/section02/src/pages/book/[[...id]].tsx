import { useRouter } from "next/router";

export default function Page() {
  const router = useRouter();
  console.log(router);
  // 동적 경로에 대응하는 법
  // 파일 생성 시 대괄호 안에 들어간 변수명으로 저장됨
  const { id } = router.query;
  // 만약 다양한 id를 받는 경우에는 배열로 저장됨
  // 예시 : ['255', '3984793', '39747394', '1212']
  console.log(id);

  return <h1>Book {id}</h1>;
}

// 만약 여러개의 dynamic routing 변수를 가지고 있다면,
//  이를 모두 대응할 수 있도록 파일명을 [...변수명]으로 작성하면 됨
//  => catch all segment(구간) 이라고 함

// 만약 더 범용적으로 사용하고 싶다면 [[...변수명]]과 같이 한번 더 []로 감싸주면 뒤에 다이나믹 라우팅 변수가 없는 url로 접속을 하더라도 오류가 나지 않음
//  => optional catch all segment 이라고 함
