<template>
    <div>
        <div class="link-area">
            <span>
                <RouterLink :to="{name:'MovieRecommend'}">추천 영화</RouterLink>
                <p class="link-context">Movie Sh#rping만의 선호도 기반 추천 영화</p>
            </span> 
            <span>|</span>

            <span>
                <RouterLink :to="{name:'MovieUpcoming'}">상영 예정 영화</RouterLink>
                <p class="link-context">곧 개봉할 상영 예정 영화, 보고 싶은 영화를 찜해보세요.</p>
            </span>
        </div>

        <RouterView/>

    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';


</script>

<style scoped>
.link-area{
    background-color: #F2F2F2;
    width: 100%;
    height: 70px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    min-width: 500px;
}

a{
    text-decoration: none;
    color: black;
    margin-bottom: 0;
    font-size: 20px;
}

.link-context {
    font-size: 15px;
    margin: 0 0;
}

span {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.router-link-active {
  color: #1D97C1; /* 활성화된 링크의 글씨 색상 변경 */
}

.router-link-active + .link-context {
  color: #53C7F0; /* 활성화된 링크 및 아래 텍스트의 색상 변경 */
}
</style>