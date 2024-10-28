// useRouter는 두가지가 있음 (router, navigator에서 가져오는 방식)
// router에서 가져오는 경우 = page router, navigator에서 가져오는 방식 = app router
import React, { ReactNode, useEffect, useState } from "react";
import SearchableLayout from "@/components/searchable-layout";
import BookItem from "@/components/book-item";
import fetchBooks from "@/lib/fetch-books";
import { useRouter } from "next/router";
import { BookData } from "@/types";

// contex에는 현재 브라우저에서 받은 요청에 대한 모든 정보가 다 담겨있음
// export const getStaticProps = async (
//   context: GetStaticProps
// ) => {
//   // 빌드 타입에 쿼리 스트링을 알 수 없음

//   const q = context.query.q;
//   const books = await fetchBooks(q as string);
//   return {
//     props: { books },
//   };
// };

export default function Page() {
  const router = useRouter();
  const [books, setBooks] = useState<BookData[]>([]);
  const q = router.query.q;

  const fetchSearchResult = async () => {
    const data = await fetchBooks(q as string);
    setBooks(data);
  };

  useEffect(() => {
    if (q) {
      fetchSearchResult();
    }
  }, [q]);

  return (
    <div>
      {books.map((book) => (
        <BookItem key={book.id} {...book} />
      ))}
    </div>
  );
}

Page.getLayout = (page: ReactNode) => {
  return <SearchableLayout>{page}</SearchableLayout>;
};
