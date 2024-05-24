<template>
    <div class="card-box">
        <div class="card" @click="goToDetail">
            <img :src="`${imgUrl}${movie.poster}`" alt="movie poster" v-if="movie.poster">
            <img :src="defaultImg" alt="movie poster" v-else >
            <p style="margin-bottom: 0px;">영화 제목 :<br> {{ movie.title }} </p>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import defaultImg from '@/assets/default_img.jpg'

const router = useRouter()
const route = useRoute()

const props = defineProps({
    movie: Object,
})

const movieCode = props.movie.code
const imgUrl = ref('https://image.tmdb.org/t/p/original/')

const goToDetail = function(){
    router.push({name:'MovieDetailView', params:{movie_id: movieCode}})
}


</script>
  
<style scoped>
.card-box {
    display: flex;
    justify-content: center;
    align-items: center;
    width: fit-content;
}

.card {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 200px;  /* 카드의 너비 고정 */
    height: 350px; /* 카드의 높이 고정 */
    margin: 10px;
    padding: 10px;
    border: 1px solid #f7f7f7;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    cursor: pointer;
}

.card img {
    max-width: 100%;
    max-height: 70%;
    margin-bottom: 10px;
    border-radius: 10px;
    object-fit: cover;
}

.card p {
    margin-top: 10px;
    text-align: center;
}
</style>