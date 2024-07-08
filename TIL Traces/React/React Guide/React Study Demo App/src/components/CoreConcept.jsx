// 구조 분해 할당을 통해 매개변수 목록에서 사용되는 매개 변수를 지정할 수 있음
// 첫번째 매개 변수를 함수에 구조 분해 할당함, 들어오는 객체의 속성들을 이름별로 목표로 함
export default function CoreConcept({ title, image, description }) {
    return (
        <li>
            <img src={image} alt={title} />
            <h3>{title}</h3>
            <p>{description}</p>
        </li>
    )
}
