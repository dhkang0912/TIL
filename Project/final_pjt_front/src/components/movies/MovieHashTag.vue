<template>
    <div class="pickhashtag">
        <div class="logo">
            <p>Pick Your Sh#rping</p>
        </div>

        <div class="hashtag">
            <input class="hashtagTagify" ref="inputTag" placeholder="해시태그를 선택하세요" @input="tagFilter">
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import Tagify from '@yaireo/tagify';

const inputTag = ref(null)

// 태그가 추가되면 이벤트 발생

// 화이트 리스트 : 해당 문자만 태그로 추가 가능
const whitelist = ["감동영화", "재밌는영화", "스릴넘치는", "명작영화", "눈물샘자극", "힐링영화", "긴장감", "인생영화", "감성영화", "여운남는",
                "웃긴영화", "가족영화", "로맨틱", "공포영화", "액션영화", "서스펜스", "드라마영화", "감동적인", "재미있는", "기분좋은",
                "대박영화", "눈물나는", "웃음터짐", "설레는", "소름돋는", "감성자극", "흥미진진", "웃음폭발", "진한여운", "긴장감있는",
                "따뜻한영화", "무서운영화", "잔잔한감동", "흥미로운", "멋진영화", "기대되는", "생각하게하는", "환상적인", "몰입감", "강추영화",
                "가슴뭉클", "재밌음", "소름", "잊지못할", "영화추천", "신나는", "코미디영화", "슬픈영화", "놀라운", "충격적인",
                "공감되는", "매력적인", "흥미유발", "흥미롭다", "이야기꾼", "독특한영화", "재밌다", "짜릿한", "여운", "호러영화",
                "눈물버튼", "서사적", "대서사시", "서정적인", "예술영화", "영화의밤", "감탄사", "새로운시도", "인상적인", "극적전개",
                "상상초월", "비극적", "따뜻한", "우정영화", "음악영화", "감동받다", "기억에남는", "새로운발견", "반전있는", "유쾌한",
                "애니메이션영화", "고전영화", "명작추천", "강력추천", "웃긴", "진지한", "심오한", "독립영화", "멜로영화", "감명깊은",
                "철학적", "의미있는", "휴먼드라마", "스펙터클", "반전영화", "눈물샘", "웃음가득", "화제작", "카리스마", "삶의교훈"];

const emit = defineEmits(['tagFilter'])

onMounted(()=>{
    // initialize Tagify
    const tagify = new Tagify(inputTag.value, {
        enforceWhitelist: true, // 화이트리스트에서 허용된 태그만 사용
        whitelist: whitelist, // 화이트 리스트 배열. 화이트 리스트를 등록하면 자동으로 드롭다운 메뉴가 생긴다
        // userInput: false // 입력 제한
        dropdown: {
            classname: "color-blue",
            enabled: 0,
            maxItems: 50,
            closeOnSelect: false,
            highlightFirst: true,
            enforceWhitelist: true,
        },
    })

    
    tagify.on('add', function () {
        // console.log(tagify.value); // 입력된 태그 정보 객체
        emit('tagFilter', ...tagify.value)
    })
})

// // initialize Tagify
// const tagify = new Tagify(inputTag.value, {
//     enforceWhitelist: true, // 화이트리스트에서 허용된 태그만 사용
//     whitelist: whitelist, // 화이트 리스트 배열. 화이트 리스트를 등록하면 자동으로 드롭다운 메뉴가 생긴다
//     userInput: false // 입력 제한
// })



// tagify.on('add', function () {
//     console.log(tagify.value); // 입력된 태그 정보 객체
// })
</script>

<style scoped>
.logo {
    color: white;
    text-shadow: 2px 2px 4px #1D97C1;
    font-size: 20px;
    background-color: rgba(83, 199, 240, 0.5);
    box-shadow: 0 4px 8px #BCE3FF;
    border-radius: 10px;
    overflow: hidden;
    box-sizing: border-box;
    width: 400px;
    display: flex;
    justify-content: center;
    margin: 10px 10px 20px 10px;
    /* 둥근 모서리를 적용하기 위해 추가 */
}

.pickhashtag {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 250px;
}

.hashtag {
    color: #828282;
}

.hashtag>div>span {
    display: inline-block;
    margin: 20px;
}

.tagify{    
  width: 100%;
  max-width: 700px;
}
</style>