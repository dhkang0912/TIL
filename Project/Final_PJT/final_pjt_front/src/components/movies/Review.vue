<template>
    <div class="review-card" v-if="isShowReviewForm">
        <div class="review-title">
            <h2 style="color: #1D97C1;">{{ movie.title }}</h2>
        </div>
        
        <div class="review-write isLogin" >
            <p style="color: #53C7F0;">해시태그를 Sh#rping하여 걸어보세요.</p>
            <form class="review-form" @submit="reviewForm" >
                <input id="hashtag" ref="inputHashtag">
                <div class="review-submit">
                <input type="text" v-model="inputReview" placeholder="리뷰를 작성해주세요" id="review-text">
                <input type="submit" value="submit"
                    style=" border-radius: 10px; background-color: #828282; color: aliceblue;">
                </div>
            </form>
        </div>

        <hr style="margin-top: 30px; color: #828282; font-weight: 300;">

        <div class="review-box">
            <ReviewItem :movie="movie"/>
        </div>
    </div>
    <div v-else class="review-card" style="text-align: center; font-weight: 300; color: #1D97C1;">
        <p>상영 예정 영화입니다.</p>
        <p>시청 후 리뷰를 남겨주세요.</p>
    </div>
</template>

<script setup>
import { ref, onMounted, watchEffect, watch } from 'vue';
import ReviewItem from './ReviewItem.vue';
import { useAccountStore } from '@/stores/account';
import { useMovieStore } from '@/stores/movie';
import axios from 'axios';
import Tagify from '@yaireo/tagify';

const props = defineProps({
    movie: Object,
})

const AccountStore = useAccountStore()
const MovieStore = useMovieStore()
const isLogin = AccountStore.isLogin

const inputHashtag = ref(null);
const inputReview = ref(null)

const url = AccountStore.url

// hashtagContent를 reactive 변수로 만듦
// const hashtagContent = ref([]);


onMounted(() => {
    const options = {
        whitelist: ["감동영화", "재밌는영화", "스릴넘치는", "명작영화", "눈물샘자극", "힐링영화", "긴장감", "인생영화", "감성영화", "여운남는",
            "웃긴영화", "가족영화", "로맨틱", "공포영화", "액션영화", "서스펜스", "드라마영화", "감동적인", "재미있는", "기분좋은",
            "대박영화", "눈물나는", "웃음터짐", "설레는", "소름돋는", "감성자극", "흥미진진", "웃음폭발", "진한여운", "긴장감있는",
            "따뜻한영화", "무서운영화", "잔잔한감동", "흥미로운", "멋진영화", "기대되는", "생각하게하는", "환상적인", "몰입감", "강추영화",
            "가슴뭉클", "재밌음", "소름", "잊지못할", "영화추천", "신나는", "코미디영화", "슬픈영화", "놀라운", "충격적인",
            "공감되는", "매력적인", "흥미유발", "흥미롭다", "이야기꾼", "독특한영화", "재밌다", "짜릿한", "여운", "호러영화",
            "눈물버튼", "서사적", "대서사시", "서정적인", "예술영화", "영화의밤", "감탄사", "새로운시도", "인상적인", "극적전개",
            "상상초월", "비극적", "따뜻한", "우정영화", "음악영화", "감동받다", "기억에남는", "새로운발견", "반전있는", "유쾌한",
            "애니메이션영화", "고전영화", "명작추천", "강력추천", "웃긴", "진지한", "심오한", "독립영화", "멜로영화", "감명깊은",
            "철학적", "의미있는", "휴먼드라마", "스펙터클", "반전영화", "눈물샘", "웃음가득", "화제작", "카리스마", "삶의교훈"],
        dropdown: {
            classname: "color-blue",
            enabled: 0,
            maxItems: 50,
            closeOnSelect: false,
            highlightFirst: true,
        },
        enforceWhitelist: true,
    };
    let tagifyhashtag = new Tagify(inputHashtag.value, options);
    // 태그가 추가될 때 이벤트 처리

});

const reviewForm = () => {
    
    const hashtagValue = inputHashtag.value.value; // Tagify input의 값을 문자열로 가져옴
    const hashtagArray = JSON.parse(hashtagValue); // 문자열을 JSON 배열로 변환
    const tags = hashtagArray.map(item => item.value); // 배열 형식 변환
    const reviewTextValue = inputReview.value; // 리뷰 텍스트 입력 필드의 값을 가져옴

    console.log('Hashtags:', tags);
    console.log('Review Text:', reviewTextValue);
    console.log('movie id',props.movie.code)

    axios({
        method:'POST',
        url:`${url}/movies/${Number(props.movie.code)}/review/`,
        data: {
            tags : tags,
            review : reviewTextValue,
        },
        headers: {
            Authorization: `Token ${AccountStore.token}`
        }
    }).then((res) => {
        console.log(res)
        alert('리뷰가 작성 작성되었습니다.')
    }).catch((err) => {
        console.log('error')
        console.log(err)
        alert(`리뷰 작성이 실패했습니다. 다시 리뷰를 작성해주세요.`)
    })
};

// console.log('upcoming movie', MovieStore.upcomingMovies)
const isUpcoming = MovieStore.upcomingMovies.find(upcomingmovie => upcomingmovie.code === props.movie.code) !== undefined;

// console.log(`isupcoming`, isUpcoming);

const isShowReviewForm = isLogin === true && isUpcoming === false



</script>
<style scoped>
.review-card {
    width: 100%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-top: 40px;
    padding: 10px 20px;
    height: fit-content;
    box-sizing: border-box;
}

.review-form {
    display: block; /* 기본 왼쪽 정렬 */
    margin-top: 10px;
    width: 100%;
}

#review-text {
    box-sizing: border-box;
    width: 100%; /* 100% 너비 */
    height: 35px;
    padding: 10px;
    font-size: 16px;
}

input[type="submit"] {
    width: 100px;
    height: 35px;
    font-size: 16px;
    padding: 10px;
}

.review-submit {
    display: flex;
    justify-content: flex-start; /* 왼쪽 정렬 */
    align-items: center;
}

#hashtag {
    width: 80%;
    height: 45px;
    font-size: 16px;
    padding: 10px;
}

.customLook {
    min-width: 5000px;
    background-color: red;
}
</style>