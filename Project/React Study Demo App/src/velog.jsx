<ul>
    {/* JSX는 코드 배열과 같이 렌더링 가능한 데이터 배열을 처리할 수 있음 */}
    {/* {[<p>Hello</p>,<p>World</p>]} */}
    {/* 동적으로 CoreConcept을 출력해야 나중에 데이터 수가 줄어들거나 늘어나도 깨지지 않음 */}

    {/* JSX 안에서 객체를 읽도록 해서 동적으로 이미지나 데이터를 처리할 수 있도록 함 */}
    {CORE_CONCEPTS.map((conceptItem) => (
        <CoreConcept key={conceptItem.title} {...conceptItem} />
    ))}

</ul>