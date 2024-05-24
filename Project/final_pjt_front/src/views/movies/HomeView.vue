<template>
  <div>
    <!-- <div class="area" v-show="AccountStore.isLogin">
      <h2 style="margin-bottom: 0; text-align: left;">추천 영화 <button @click="goToReccomend">더보기</button></h2>
      <p style="margin-top: 0; text-align: left; color: #828282;">Movie Sh#rping만의 선호도 기반 추천 영화</p>
      <div class="card-area swiper">
        <div class="swiper-wrapper" v-for="recommendedMovie in MovieStore.recommendedMovies"
          @click="goToDetail(recommendedMovie)">
          <div class="card">
            <img :src="`${imgUrl}${recommendedMovie.poster}`" alt="">
            <p>영화 제목 : {{ recommendedMovie.title }}</p>
          </div>
        </div>
      </div>
    </div> -->

    <div class="area" v-show="AccountStore.isLogin">
      <div class="area">
        <h2 style="margin-bottom: 0;">추천 영화 <button @click="goToReccomend">더보기</button></h2>
        <p style="margin-top: 0; color: #828282;">Movie Sh#rping만의 선호도 기반 추천 영화</p>
        <swiper class="card-area swiper" :modules="[Navigation, Pagination, Autoplay]" :slidesPerView="4"
          :spaceBetween="20" :loop="true" :autoplay="{ delay: 3000, disableOnInteraction: false }"
          :navigation="{ nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' }"
          :pagination="{ el: '.swiper-pagination', clickable: true }">
          <swiper-slide style="max-width: fit-content; margin-right: 10px;" class="card"
            v-for="recommendedMovie in MovieStore.recommendedMovies" :key="recommendedMovie.id"
            @click="goToDetail(recommendedMovie)">

            <div style="margin: 20px; max-width: fit-content;">
              <img :src="`${imgUrl}${recommendedMovie.poster}`" alt="">
              <p>영화 제목 : {{ recommendedMovie.title }}</p>
            </div>
          </swiper-slide>
          <div class="swiper-button-next"></div>
          <div class="swiper-button-prev"></div>
        </swiper>
      </div>
    </div>


    <div class="area not-login" v-show="!AccountStore.isLogin">
      <h2 style="margin-bottom: 0;">추천 영화</h2>
      <p style="margin-top: 0; color: #828282;">Movie Sh#rping만의 선호도 기반 추천 영화</p>
      <div class="card-area not-login-p">
        <p>로그인 후 사용하실 수 있습니다.</p>
      </div>
    </div>

    <!-- <div class="area">
      <h2 style="margin-bottom: 0;">상영 예정 영화 <button @click="goToUpcoming">더보기</button></h2>
      <p style="margin-top: 0; color: #828282;">곧 개봉할 상영 예정 영화, 보고 싶은 영화를 찜해보세요.</p>
      <div class="card-area">

        <div class="card" v-for="upcomingMovie in MovieStore.upcomingMovies" @click="goToDetail(upcomingMovie)">
          <img :src="`${imgUrl}${upcomingMovie.poster}`" alt="movie poster" v-if="upcomingMovie.poster">
          <img :src="defaultImg" alt="movie poster" v-else>
          <p>영화 제목 : {{ upcomingMovie.title }}</p>
        </div>
      </div>
    </div> -->


    <div class="area">
      <h2 style="margin-bottom: 0;">상영 예정 영화 <button @click="goToUpcoming">더보기</button></h2>
      <p style="margin-top: 0; color: #828282;">곧 개봉할 상영 예정 영화, 보고 싶은 영화를 찜해보세요.</p>
      <swiper class="card-area swiper" :options="swiperOptions" :modules="[Navigation, Pagination, Autoplay]"
        :slidesPerView="4" :spaceBetween="20" :loop="true" :autoplay="{ delay: 3000, disableOnInteraction: false }"
        :navigation="{ nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' }"
        :pagination="{ el: '.swiper-pagination', clickable: true }">

        <swiper-slide style="max-width: fit-content; margin-right: 10px;" class="card"
          v-for="upcomingMovie in MovieStore.upcomingMovies" @click="goToDetail(upcomingMovie)">
          <div style="max-width: fit-content; margin: 20px;">
            <img :src="`${imgUrl}${upcomingMovie.poster}`" alt="movie poster" v-if="upcomingMovie.poster">
            <img :src="defaultImg" alt="movie poster" v-else>
            <p>영화 제목 : {{ upcomingMovie.title }}</p>
          </div>
        </swiper-slide>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
      </swiper>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { useMovieStore } from '@/stores/movie'
import defaultImg from '@/assets/default_img.jpg'
// import { Swiper, SwiperSlide } from 'swiper/vue';
// import 'swiper/css';
// import 'swiper/css/navigation';
// import 'swiper/css/pagination';
// import 'swiper/css/autoplay';
// import { Navigation, Pagination, Autoplay } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Navigation, Pagination, Autoplay } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/autoplay';


const mySwiper = ref(null);


const swiperOptions = {
  modules: [Navigation, Pagination, Autoplay],
  slidesPerView: 4,
  spaceBetween: 20,
  loop: true,
  autoplay: {
    delay: 3,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
};




const AccountStore = useAccountStore()
const MovieStore = useMovieStore()
// console.log(AccountStore.isLogin)

const router = useRouter()

const imgUrl = ref('https://image.tmdb.org/t/p/original/')

const goToReccomend = function () {
  router.push({ name: 'MovieRecommend' })
}
const goToUpcoming = function () {
  router.push({ name: 'MovieUpcoming' })
}

const goToDetail = function (movie) {
  router.push({ name: 'MovieDetailView', params: { movie_id: movie.code } })
}


// const onSwiper = (swiper) => {
//   console.log(swiper);
// };
// const onSlideChange = () => {
//   console.log('slide change');
// };

// const goToPrev = () => {
//   // Swiper 객체가 초기화될 때까지 대기하고 슬라이드 이동
//   Vue.nextTick(() => {
//     if (mySwiper.value && mySwiper.value.$swiper) {
//       mySwiper.value.$swiper.slidePrev();
//     }
//   });
// }

// const goToNext = () => {
//   // Swiper 객체가 초기화될 때까지 대기하고 슬라이드 이동
//   Vue.nextTick(() => {
//     if (mySwiper.value && mySwiper.value.$swiper) {
//       mySwiper.value.$swiper.slideNext();
//     }
//   });
// }


// onMounted(() => {
//   // Swiper 인스턴스에 접근하여 버튼 이벤트 처리
//   mySwiper.value.$swiper.on('slideChange', () => {
//     console.log('slide changed');
//   });
// });
// const modules = [Navigation, Pagination];

</script>

<style scoped>
.area {
  height: 30rem;
  width: 100%;
  /* border: 1px solid; */
  margin-bottom: 20px;
  overflow: hidden;
}

.align {
  width: 100%;
  box-sizing: border-box;
  height: 30rem;
  text-align: center;
}

.card-area {
  width: 100%;
  display: flex;
  align-items: center;
  padding-left: 0;
  display: grid;
  /* 그리드 레이아웃 설정 */
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  /* 열의 너비를 설정합니다. 반응형으로 조정됩니다. */
  gap: 20px;
  /* 그리드 아이템 사이의 간격을 설정합니다. */
  /* border: 1px solid; */
  height: 360px;
  /* 부모 요소인 .card-area의 높이에 맞게 설정 */
  overflow: hidden;
}

.card {
  width: 100%;
  /* 카드의 너비를 100%로 설정합니다. 그리드의 열 너비에 따라 자동 조정됩니다. */
  height: 350px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-left: 0;
  border: solid 1px #F7F7F7;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  /* 그림자 효과 추가 */
  cursor: pointer;
}

.card img {
  max-width: 100%;
  /* 이미지의 최대 너비 설정 */
  max-height: 70%;
  /* 이미지의 최대 높이 설정 */
}

.card p {
  margin-top: 10px;
  /* 텍스트와 이미지 사이의 간격 조절 */
}

img {
  border-radius: 20px;
  height: 250px;
  width: 200px;
  margin-bottom: 15px;
}

.card img {
  max-width: 100%;
  /* 이미지의 최대 가로 너비를 부모 요소에 맞추어 설정 */
  max-height: 100%;
  /* 이미지의 최대 세로 높이를 부모 요소에 맞추어 설정 */
  object-fit: cover;
  /* 이미지를 찌그러지지 않고 부모 요소에 맞게 조정합니다. */
}

button {
  text-decoration: none;
  position: relative;
  border: none;
  font-size: 10px;
  font-family: inherit;
  cursor: pointer;
  color: #fff;
  width: 9em;
  height: 3em;
  line-height: 2em;
  text-align: center;
  background: linear-gradient(90deg, #03a9f4, #f441a5, #ffeb3b, #03a9f4);
  background-size: 300%;
  border-radius: 30px;
  z-index: 1;
  height: 15px;
  width: 40px;
  padding: 0;
}

button:hover {
  animation: ani 8s linear infinite;
  border: none;
}

@keyframes ani {
  0% {
    background-position: 0%;
  }

  100% {
    background-position: 100%;
  }
}

button:before {
  content: "";
  position: absolute;
  top: -5px;
  left: -5px;
  right: -5px;
  bottom: -5px;
  z-index: -1;
  background: linear-gradient(90deg, #03a9f4, #f441a5, #ffeb3b, #03a9f4);
  background-size: 400%;
  border-radius: 35px;
  transition: 1s;
}

button:hover::before {
  filter: blur(20px);
}

button:active {
  background: linear-gradient(32deg, #03a9f4, #f441a5, #ffeb3b, #03a9f4);
}

.not-login-p {
  display: flex;
  justify-content: center;
  /* 수평 가운데 정렬 */
  align-items: center;
  /* 수직 가운데 정렬 */
  height: 76%;
  /* 부모 요소인 .card-area의 높이에 맞게 설정 */
  width: 100%;
  /* 부모 요소인 .card-area의 너비에 맞게 설정 */
  overflow: auto;
  /* 내용이 넘칠 경우 스크롤 나타나도록 설정 */
  padding: 20px;
  /* 내용과 경계 사이의 간격을 조정합니다. */
  box-sizing: border-box;
  /* 패딩과 경계를 포함하여 요소의 전체 너비를 설정합니다. */
  border: solid 1px #F7F7F7;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  /* 그림자 효과 추가 */
  padding-bottom: 10px;
}

.swiper-button-prev,
.swiper-button-next {
  color: whitesmoke;
  font-size: 10px;
  width: 40px;
  height: 40px;
  border-radius: 20%;
  background-color: rgba(13, 13, 13, 0.78);
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
}


.swiper-button-prev {
  left: 5px;
}

.swiper-button-next {
  right: 5px;
}
</style>