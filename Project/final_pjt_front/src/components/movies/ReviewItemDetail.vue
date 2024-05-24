<template>
    <div>
        <h3 style="margin-bottom: 0;">
            <button class="deleteBtn" @click="deleteReview(review.id)" v-if="review.user.username === AccountStore.user.username" style="margin-right: 10px;">X</button>
            <span style="text-decoration: underline; ">{{ review.user.nickname }}</span>
            <span style="font-size: 0.8rem; color:#828282 ;">
                <span style="margin-left: 20px">작성일 : {{ formatDate(new Date(review.created_at)) }}</span> | 
                <span>수정일 : {{ formatDate(new Date(review.updated_at)) }}</span>
            </span>
        </h3>
        <div>
            <span v-for="tag in review.hashtag_set" style="color: #828282;">&ThickSpace;#{{ tag.tag }}&ThickSpace;</span>
        </div>
        
        <div class="review-content">
            <form @submit.prevent="updateReview(review.id)">
                <p style="margin-top: 0; width: 100%;" v-if="!isUpdating">{{ reviewText }}</p>
                <input type="text" name="text" id="updateText" style="width: 80%; margin-right: 20px;" v-model.trim="updateText" v-else>
                <span style="margin-top: 0;" v-if="review.user.username === AccountStore.user.username">
                    <input type="submit" v-if="isUpdating" value="submit" class="button"/>
                </span>
            </form>
            <span style="text-align: right;">
                <button @click="isUpdating = !isUpdating" v-if="isWriter && !isUpdating" class="button"  style="margin-right: 10px;">Edit</button>
                
            </span>
        </div>
        <hr>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/account';
import { useMovieStore } from '@/stores/movie';
import { ref } from 'vue';
import axios from 'axios';

const props = defineProps({
    review: Object,
    movie: Object,
})

const MovieStore = useMovieStore()
const AccountStore = useAccountStore()

const reviewText = ref(props.review.text)
const isWriter = AccountStore.user.pk === props.review.user.id
const isUpdating = ref(false)
const updateText = ref(reviewText.value)

const createdAt = ref(props.created_at)
const updatedAt = ref(props.updated_at)

const updateReview = function (reviewId) {
    isUpdating.value = true

    axios({
        method: 'PUT',
        url: `${MovieStore.url}/movies/${props.movie.code}/review/${reviewId}/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        },
        data: {
            text: updateText.value,
        },
    }).then((res) => {
        console.log('업데이트 완료')
        reviewText.value = updateText.value
        isUpdating.value = false
        location.reload(true)
    }).catch((err) => {
        console.log(err)
    })
}

const deleteReview = function (reviewId) {
    axios({
        method: 'delete',
        url: `${MovieStore.url}/movies/${props.movie.code}/review/${reviewId}/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        }
    }).then((res) => {
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
        }).then((res) => {
            location.reload(true)
        })
    }).catch((err) => {
        console.log(err)
    })
}

const formatDate = function (date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');

  return `${year}-${month}-${day} ${hours}:${minutes}`;
}
</script>

<style scoped>
.review-content {
    display: flex;
    /* align-items: center; */
    margin: 10px 0;
    height: 20px;
    box-sizing: border-box;
}

.review-content > form {
    min-width: 97%;
    text-align: left;
}

/* button {
    border-radius: 10px;
    background-color: #828282;
    color: aliceblue;
    margin-top: 0px;
    cursor: pointer;
} */

.button {
    border-radius: 10px;
    background-color: #828282;
    color: aliceblue;
    margin-top: 0px;
    cursor: pointer;
}

.deleteBtn {
    background-color: transparent;
    border: 1px solid  #828282 ;
    border-radius: 5px;
    color: #828282;
}
</style>