<template>
    <div>
        <!-- <h3 style="margin-bottom: 0;">{{ review.user.nickname }}</h3>
        <div class="review-content" >
            <p style="margin-top: 0; width: 400px; color:#454545 ;">{{ review.text }}</p>
            <input type="text" name="text" id="updateText" style="width: 90%;" v-model.trim="updateText">
            <span style="margin-top: 0;" v-if="review.user.username === AccountStore.user.username">
                <button style="border-radius: ;" @click="updateReview(review.id)">Update</button>
                <button style="border-radius: ;" @click="deleteReview(review.id)">Delete</button>
            </span>
        </div> -->
        <ReviewItemDetail v-for="review in movieReviews" :key="review.pk" :review="review" :movie="movie" />
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/account';
import { useMovieStore } from '@/stores/movie';
import ReviewItemDetail from '@/components/movies/ReviewItemDetail.vue';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const MovieStore = useMovieStore()
const AccountStore = useAccountStore()
// console.log(AccountStore.user.username)
const movieReviews = ref([])
const isUpdating = ref(false)
const updateText = ref('')


const props = defineProps({
    movie:Object
})

const updateReview = function (reviewId) {
    axios({
        method: 'PUT',
        url:`${MovieStore.url}/movies/${props.movie.code}/review/${reviewId}/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        },
        data: {

        }
    })
}

const deleteReview = function(reviewId){
    axios({
        method:'delete',
        url:`${MovieStore.url}/movies/${props.movie.code}/review/${reviewId}/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        }
    }).then((res)=>{
        // console.log(res.data)
        axios({
        method: 'get',
        url: `${MovieStore.url}/movies/${props.movie.code}/get_review/`,
        }).then((res) => {
            // console.log(`받아옴` ,res.data)
            movieReviews.value = res.data
            // console.log(`받아온 데이터`,movieReviews.value)
        }).catch((err) => {
            console.log(err)
        })
    }).catch((err)=>{
        console.log(err)
    })
}


onMounted(()=>{
    axios({
        method: 'get',
        url: `${MovieStore.url}/movies/${props.movie.code}/get_review/`,
    }).then((res) => {
        // console.log(`받아옴`, res.data)
        movieReviews.value = res.data
        // console.log(`받아온 데이터`, movieReviews.value)
    }).catch((err) => {
        if (err.response.statusText === 'Not Found') {
            console.log('리뷰 데이터가 없습니다.')
        }
    })
})


// console.log(`props`, props.review)

</script>
  
<style scoped>
.review-content {
    display: flex;
    justify-content: space-between;
    /* align-items: center; */
    margin-bottom: 10px;
    height: 20px;
}

button {
    border-radius: 10px;
    background-color: #828282;
    color: aliceblue;
    margin-top: 0px;
    cursor: pointer;
}
</style>