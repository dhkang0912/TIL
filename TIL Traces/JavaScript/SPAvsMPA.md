# SPA vs MPA
- [SPA vs MPA](#spa-vs-mpa)

## SPA
### SPA (Single Page Application)
- 하나의 페이지로 구성되어있는 애플리케이션
- 사용자 경험 향상이라는 핵심 가치를 가지고 있음
- 애플리케이션의 속도 향상
- 사용하는 사이트 : Facebook, Google, Medium
- 사용 프레임워크 : Angular, React, Vue

### 작동방식
- 웹 애플리케이션에 필요한 모든 정적 리소스를 최소 접근 시 단 한번만 다운로드
- 이후 새로운 페이지 요청 시 페이지 갱신에 필요한 데이터만 전달받아 페이지 갱신
- 기존 페이지의 내부를 수정해서 보여주는 방식
- 기본적으로 SPA는 CSR(Client Server Rendering
)

### 장점
- 정적 리소스를 처음 렌더링될 때 모두 다운받기 때문에 페이지 갱신 시 화면이 깜빡 거리지 않음
  => 사용자 경험 향상
- 갱신에 필요한 데이터만 받기 때문에 속도와 응답 시간이 빠름
- 컴포넌트 기반의 코드를 작성하기 때문에 재사용성이 높음
- 프레임워크를 사용하여 기존 코드를 재사용하여 모바일 앱을 만들 수 있음
- 모바일 앱 개발을 염두에 둔다면 동일한 API를 사용하여 설계 가능

### 단점
- 모든 리소스를 최초 접근 시에 다운하기 때문에 초기 구현 속도가 느림
- JavaScript로 구축되기 때문에 검색엔진최적화(SEO)가 어려움
- 보안이 약함
  - JavaScript는 코드 컴파일을 수행하지 않으므로 악의적인 사용자가 엑세스할 수 있음
- 브라우저 히스토리를 제공하지 않아서 뒤로가기를 할 수 없음, 직전 페이지만 가지고 있음

---
[목차로 돌아가기](#)

---

## MPA
### MPA (Multi Page Application)
- MPA는 SPA와 반대되는 개념
- 사용하는 사이트 : Amazon, eBay, e-commerce sites

### 작동방식
- MPA는 각 페이지별로 HTML 문서가 따로 존재하며 페이지를 이동할 때마다 새로운 html 페이지를 받아와서 새로 렌더링하는 전통적인 웹페이지 구성 방식

### 장점
- SEO 최적화
  - 여러 페이지를 생성할 수 있기 때문에 더 많은 수의 키워드를 타겟팅할 수 있음
  - Google에서 얻을 수 있는 유기적 트래픽의 양이 자동으로 향상됨
- 페이지의 제한이 없기 때문에 많은 양의 데이터를 수용 가능
- 이미 검증된 안정한 프레임워크들이 많음

### 단점
- 페이지 이동 시 새로운 파일을 받아야 하기 때문에 로딩 시간 증가
- 여러 페이지의 규모가 너무 커지면 유지 관리 및 업데이트가 어려울 수 있음

## 선택하는 기준
- SPA 
  - SEO가 중요하지 않은 SaaS 플랫폼이나 social networks에 적합
  - 데이터 볼륨이 적은 플랫폼
- MPA
  - 데이터 볼륨이 큰 웹사이트
  - 온라인 유통 사이트에 적합


## 참고 자료
- [Which one you actually need-“Single Page Application or Multi Page Application”](https://shifat-jaman.medium.com/which-one-you-actually-need-single-page-application-or-multi-page-application-c0976d45ed93)

- [SPA vs MPA와 SSR vs CSR 장단점 뜻정리
](https://hanamon.kr/spa-mpa-ssr-csr-%EC%9E%A5%EB%8B%A8%EC%A0%90-%EB%9C%BB%EC%A0%95%EB%A6%AC/)
- [CSR/SSR, SPA/MPA 완전 정복](https://demain18-blog.tistory.com/73)