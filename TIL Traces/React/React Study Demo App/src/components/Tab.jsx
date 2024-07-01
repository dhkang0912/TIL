export default function Tabs({ children, buttons, ButtonsContainer='menu' }) {
    // buttonsContainer는 소문자로 시작하여 내장 속성을 검색함, 하지만 이런 빌트인 요소는 없음, 이를 커스텀 컴포넌트로 사용하기 위해서는 대문자로 시작하는 변수를 선언하여 할당해줘야 함
    // const ButtonsContainer = buttonsContainer
    return <>
        <ButtonsContainer>
            {buttons}
        </ButtonsContainer>
        {children}
    </>
}