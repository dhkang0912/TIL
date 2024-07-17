import "./Header.css"
import { memo } from "react";

const Header = () => {
  return (
    <div className="Header">
      <h3>오늘은 📅</h3>
      <h1>{new Date().toDateString()}</h1>
    </div>
  );
};

// 최적화하고 싶은 컴포넌트를 넣어주면 됨, 부모요소가 리렌더링될 때는 리렌더링 되지 않고 Header의 props가 바뀔 때만 리렌더링
// const memoizedHeader =  memo(Header)

export default memo(Header);
