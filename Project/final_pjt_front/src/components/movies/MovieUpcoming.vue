<template>
    <div class="main-box">
        <div class="moviecards" v-if="MovieStore.upcomingMovies" >
            <MovieItem 
            v-for="movie in MovieStore.upcomingMovies"
            :movie="movie"
            :key="MovieStore.code"

            class="movie-item"
            />
        </div>

    </div>
</template>

<script setup>
import MovieItem from '@/components/movies/MovieItem.vue'
import { useMovieStore } from '@/stores/movie';
const MovieStore = useMovieStore()
console.log(MovieStore.upcomingMovies)

</script>

<style scoped>
.main-box {
    min-height: 1000px;
    width: 100%;
    margin: 20px;
}

.moviecards {
    display: flex;
    flex-wrap: wrap; /* flex 아이템이 여러 줄에 걸쳐 표시되도록 설정 */
    justify-content: center;
    gap: 20px;  /* 카드 사이의 간격 조정 */
}

.movie-item {
    flex: 1 1 calc(20% - 20px);  /* 한 줄에 5개의 카드가 보이도록 설정 */
    margin-bottom: 20px; /* 각 카드 아래 여백 추가 */
}
</style>