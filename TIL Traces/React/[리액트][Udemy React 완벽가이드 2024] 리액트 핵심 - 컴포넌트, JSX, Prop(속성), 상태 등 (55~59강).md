## [리액트][Udemy React 완벽가이드 2024] - 리액트 핵심 : 컴포넌트, JSX, Prop(속성), 상태 등 (55~59강)

### 조건적 콘텐츠 렌더링
- 조건적 콘텐츠를 렌더링하는 방법은 여러개
1. 삼항연산자 사용
2. 논리 And 연산자 사용 (&&)
3. jsx 변수 적용
<br>


1. 삼항연산자 사용
```
const [selectedTopic, setSelectedTopic] = useState(null)

function handleSelect(selectedButton) {
    // console.log(selectedButton)
    // 
    setSelectedTopic(selectedButton)
    // console 찍으면 리액트가 작동하는 방식 때문에 과거 정보가 나옴
    console.log(selectedTopic)
}

{/* 삼항연산자를 사용하여 selectedTopic이 초기값인 null로 undefined 상태라면 글을 보여주고 그렇지 않다면 선택한 것의 글자들을 보여주게 함 */ }
{
    !selectedTopic ? (
        <p>Please select a topic.</p>
    ) : (
    <div id="tab-content">
        {/* EXAMPLES 객체의 속성이 변수명이 되어야 하기 때문에 []를 사용, 자바스크립트 문법 */}
        <h3>{EXAMPLES[selectedTopic].title}</h3>
        <p>{EXAMPLES[selectedTopic].description}</p>
        <pre>
            <code>
                {EXAMPLES[selectedTopic].code}
            </code>
        </pre>
    </div>
)
}
```
<br>

2. &&, 논리 AND 연산자
```
{/* && 연산자를 활용해서도 작성 가능, 논리 AND 연산자로 조건이 사실이라면 AND 바로 뒤에 나온 것을 출력함 */ }
{ !selectedTopic && <p>Please select a topic.</p> }
{ selectedTopic && <div id="tab-content">
        <h3>{EXAMPLES[selectedTopic].title}</h3>
        <p>{EXAMPLES[selectedTopic].description}</p>
        <pre>
            <code>
                {EXAMPLES[selectedTopic].code}
            </code>
        </pre>
    </div>
}
```

<br>
3. jsx 변수 활용

```
// jsx return 전
let tabContent = <p>Please select a topic.</p>
if (selectedTopic) {
    tabContent = (
        <div id="tab-content">
            <h3>{EXAMPLES[selectedTopic].title}</h3>
            <p>{EXAMPLES[selectedTopic].description}</p>
            <pre>
                <code>
                    {EXAMPLES[selectedTopic].code}
                </code>
            </pre>
        </div>
    )
}

// jsx return 후
{ tabContent }
```

<br>

### CSS 스타일링 및 동적 스타일링
- JSX에서 class를 설정하고 싶을 때는 className이라는 속성을 사용함
- 특정한 버튼이 활성화됐을 때만 특정 스타일을 입히고 싶다면 삼항연산자를 통해 현재 상태를 표시하는 플래그를 만들고 이를 매개변수로 넘겨서 특정 스타일 클래스 이름을 나타나게 할 수 있다
  - 아래 코드를 보면 isSelected가 true인 경우 active라는 클래스 네임을 활성화시키고 있음, 만약 false인 경우 undefined로 null이게 됨
```
export default function TabButton({ children, onSelect, isSelected }) {

    // 이벤트를 추가할 때도 prop을 넣어줌
    // on~은 prop을 추가하는 것으로 함수로 작성해야함
    // 함수 값을 넣고 싶기 때문에 소괄호를 넣으면 안되고 함수 이름만 작성해야함 
    // jsx에서 class를 넣을 때는 className 속성을 통해 넣음
    // 삼항연산자를 통해 해당 요소가 선택됐을 때만 활성화할 수 있음
    return <li><button className={isSelected ? 'active' : undefined} onClick={onSelect}>
            {children}
        </button></li>
}

<TabButton isSelected={selectedTopic === 'components'}
onSelect={() => handleSelect("components")}>
Components
</TabButton>

<TabButton isSelected={selectedTopic === 'jsx'}
onSelect={() => handleSelect("jsx")}>
JSX
</TabButton>

<TabButton isSelected={selectedTopic === 'props'}
onSelect={() => handleSelect("props")}>
Props
</TabButton>

<TabButton isSelected={selectedTopic === 'state'}
onSelect={() => handleSelect("state")}>
State
</TabButton>

```

### List 데이터 동적 출력
- JSX는 리스트 안에 있는 문자열, html 구문을 출력할 수 있음
  - 렌더링 가능한 데이터 배열을 처리할 수 있음
- 동적으로 순회하면서 JSX를 통해 데이터를 출력하면 데이터의 수가 줄거나 늘었을 때도 앱이 깨지지 않고 정상적으로 작동할 수 있음
- JSX 안에 코드를 작성하고 배열을 map을 통해 순회하면서 각 컴포넌트들의 props를 전달할 수 있도록 전개구문을 사용하여 펼침
- 순회된 각 컴포넌트들의 prop은 key를 가져야 한다는 룰이 있기 때문에 고유성을 가진 내용을 key로 설정해줌

```
<ul>
    {/* JSX는 코드 배열과 같이 렌더링 가능한 데이터 배열을 처리할 수 있음 */}
    {/* {[<p>Hello</p>,<p>World</p>]} */}
    {/* 동적으로 CoreConcept을 출력해야 나중에 데이터 수가 줄어들거나 늘어나도 깨지지 않음 */}

    {/* JSX 안에서 객체를 읽도록 해서 동적으로 이미지나 데이터를 처리할 수 있도록 함 */}
    {CORE_CONCEPTS.map((conceptItem) => (
        <CoreConcept key={conceptItem.title} {...conceptItem} />
    ))}

</ul>
```


