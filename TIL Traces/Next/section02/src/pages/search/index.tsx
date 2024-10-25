// useRouter는 두가지가 있음 (router, navigator에서 가져오는 방식)
// router에서 가져오는 경우 = page router, navigator에서 가져오는 방식 = app router
import { useRouter } from "next/router";
import React from "react";

export default function Page() {
  // query string을 오는 법
  const router = useRouter();
  console.log(router);
  const { q } = router.query;

  return <h1>Search {q}</h1>;
}
