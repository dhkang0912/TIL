<template>
    <div style="min-height: 900px;">
        <div style="height: 100%;">
            <div class="card">
                <div class="img-container">
                    <img :src="`${imgUrl}${movie.poster}`" alt="movie poster" v-if="movie.poster">
                    <img :src="defaultImg" alt="movie poster" v-else>
                </div>
                <div class="text-container">
                    <div class="intro">
                        <span class="heart-icon" @click="like" v-if="showLikeBtn">💗</span>
                        <span @click="like" class="heart-icon" v-else>🤍</span>
                        <h2 style="color: #1D97C1; margin-bottom: 0; box-sizing: inline-block;">{{ movie.title }} ({{
                            movie.title_origin }}) </h2>
                    </div>
                    <p style="margin: 0; color: #53C7F0;">----------------------------------------------</p>
                    <div class="text">
                        <p>장르 : {{ genres.slice(0, 5).join(', ') }}</p>
                        <p>개봉일 : {{ movie.release_date }}</p>
                        <p>배우 : {{ actors.slice(0, 5).join(', ') }} ......<span style="font-size: 0.6rem;">(더 궁금하면 저 아래 링크
                                클릭해서 확인!)</span></p>
                        <p v-if="movie.overview">설명 : {{ movie.overview }} </p>
                        <p v-else> 자세한 설명은 아래 링크를 참조하세요 </p>
                        <a
                            :href="`https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=${movie.title}%20영화`">더
                            자세한 영화 소개 보러 가기</a>
                    </div>
                </div>
            </div>

            <Review :movie="movie" />
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import Review from '@/components/movies/Review.vue';
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { useAccountStore } from '@/stores/account';
import defaultImg from '@/assets/default_img.jpg'
import axios from 'axios';

import JSConfetti from 'js-confetti';


const route = useRoute()
const imgUrl = ref('https://image.tmdb.org/t/p/original/')
const AccountStore = useAccountStore()
const MovieStore = useMovieStore()

const jsConfetti = new JSConfetti();

const isLogin = AccountStore.isLogin
const movieId = ref(route.params.movie_id)


const getLikedMovies = function () {
    axios({
        method: 'get',
        url: `${AccountStore.url}/accounts/profile/${AccountStore.user.username}/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        }
    }).then((res) => {
        likedMovies.value = res.data.like_movie
        isLikedUpdate()
    }).catch((err) => {
        console.log(err)
    })
}

const likedMovies = ref(null)
getLikedMovies()


const movie = ref(MovieStore.movies.find((obj) => {
    return obj.code === Number(movieId.value)
}))

const isLiked = ref(false)
const isLikedUpdate = function () {
    const cnt = likedMovies.value.filter((liked_movie) => {
        return liked_movie.code === movie.value.code
    }).length
    if (cnt) {
        isLiked.value = true
    } else {
        isLiked.value = false
    }
}

const showLikeBtn = ref(isLiked.value)

const genres = ref(movie.value.genre_set.map((obj) => {
    return obj.name
}))
const actors = ref(movie.value.actor_set.map((obj) => {
    return obj.name
}))

watch([isLogin, isLiked], (newValue, oldValue) => {
    showLikeBtn.value = isLogin && isLiked.value;
});

const like = function () {
    if (!showLikeBtn.value) {
        jsConfetti.addConfetti({
            emojis: ['💗', '✨', '💓'], // 컨페티로 사용할 이모티콘 배열
            emojiSize: 40,
            confettiNumber: 100, // 컨페티의 수
            confettiColors: ['#ff0a54', '#ff477e', '#ff7096'], // 컨페티의 색상 배열
        });
    }

    axios({
        method: 'post',
        url: `${MovieStore.url}/movies/${movie.value.code}/like/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        }
    }).then((res) => {
        // console.log(res.data.like_movie)
        getLikedMovies()
        const liked = likedMovies.value.find((liked_movie) => {
            return (liked_movie.code === movie.value.code)
        }) ? true : false
        isLiked.value = liked
    }).catch((error) => {
        console.log(error)
    })
}
</script>

<style scoped>
.card {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 10px;
    align-items: center;
    width: 100%;
    height: 500px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    overflow: auto;
}

.img-container {
    grid-column: span 2;
    display: flex;
    justify-content: center;
}

.img-container img {
    border-radius: 20px;
    width: 300px;
    max-height: 400px;
}

.text-container {
    grid-column: span 4;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.text-container p {
    margin-top: 10px;
}

a {
    text-decoration: none;
    color: #53C7F0;
}

.heart-icon {
    font-size: 30px;
    display: flex;
}

.intro {
    display: flex;
}

.text {
    margin: 20px;
    box-sizing: inline-block;
}

@media (max-width: 1085px) {
    .card {
        grid-template-columns: 1fr;
        grid-template-rows: auto auto;
        height: auto;
    }

    .img-container {
        grid-column: span 1;
        justify-content: center;
    }

    .text-container {
        grid-column: span 1;
        align-items: center;
    }

    .img-container img {
        width: 100%;
        max-width: 300px;
        height: auto;
    }
}

.scroll::-webkit-scrollbar {
    display: none;
}</style>