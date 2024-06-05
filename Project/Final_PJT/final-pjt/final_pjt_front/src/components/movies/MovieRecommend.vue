<template>
    <div class="main-box">
        <div class="pick-area">
            <MovieHashTag @tag-filter="tagFilterMovie" />
        </div>
        <div class="moviecards">
            <MovieItem v-for="movie in recommendedMovies" :movie="movie" :key="movie.code" class="movie-item" />
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import MovieItem from '@/components/movies/MovieItem.vue'
import MovieHashTag from './MovieHashTag.vue';
import { useMovieStore } from '@/stores/movie';
import { useAccountStore } from '@/stores/account';
import axios from 'axios';

const MovieStore = useMovieStore()
const AccountStore = useAccountStore()
const recommendedMovies = ref([])
const tags = ref([])

onMounted(() => {
    recommendedMovies.value = MovieStore.recommendedMovies
})

const tagFilterMovie = function (...args) {
    tags.value = args.map((obj) => {
        return obj.value
    })
}

watch(tags, (newValue, oldValue) => {
    if (tags.value) {
        console.log(tags.value)
        axios({
            method: 'POST',
            url: `${MovieStore.url}/movies/hashtag_to_movie/`,
            headers: {
                Authorization: `Token ${AccountStore.token}`
            },
            data: {
                tags: tags.value
            }
        }).then((res) => {
            console.log(res.data)
            recommendedMovies.value = res.data
            console.log(recommendedMovies.value)
        }).catch((err) => {
            console.log(err)
            recommendedMovies.value = MovieStore.recommendedMovies
            alert('해당 태그를 포함하는 영화가 없습니다!')
        })
    }
})

</script>

<style scoped>
.main-box {
    min-height: 1000px;
    width: 100%;
    margin: 20px
}

.pick-area {
    width: 100%;
    border: solid 1px #F7F7F7;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    /* 그림자 효과 추가 */
    overflow-x: auto;
    margin-bottom: 20px;
}

.moviecards {
    display: flex;
    flex-wrap: wrap;
    /* flex 아이템이 여러 줄에 걸쳐 표시되도록 설정 */
    justify-content: center;
    gap: 20px;
    /* 카드 사이의 간격 조정 */
}

.movie-item {
    flex: 1 1 calc(20% - 20px);
    /* 한 줄에 5개의 카드가 보이도록 설정 */
    margin-bottom: 20px;
    /* 각 카드 아래 여백 추가 */
}
</style>