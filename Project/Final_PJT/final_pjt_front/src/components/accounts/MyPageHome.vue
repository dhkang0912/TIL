<template>
    <div class="like-card">
        <h3 style="margin-bottom: 0;">💗Prefences💗</h3>
        <div class="like-card" style="margin-bottom: 20px;">
            <form @submit.prevent="editPreference">
                <div class="prefence-card">
                    <div class="hashtag">
                        <p>선호하는 <b>장르</b>와 <b>배우</b>를 선택해보세요.</p>
                        <label for="genre">장르 :</label>&ThickSpace;
                        <input id="genre" ref="inputGenre">
                        <br>
                        <br>
                        <label for="actor">배우 :</label>&ThickSpace;
                        <input id="actor" ref="inputActor">
                        <br>
                        <br>
                        <input class="button" type="submit" value="수정하기" style="margin-bottom: 20px;">
                    </div>
                </div>
            </form>
        </div>
        <div class="like-card" style="margin-bottom: 20px;">
            <p v-if="AccountStore.user.likeActor && AccountStore.user.likeGenre">'{{ AccountStore.user.nickname }}'님이 저장한 선호
                장르 및 배우</p>
            <p>장르 : {{ AccountStore.user.likeGenre }} </p>
            <p>배우: {{ AccountStore.user.likeActor }}</p>
        </div>
    </div>


    <div class="like-card">
        <h3>💗Liked Movies💗</h3>
        <div class="card-area">
            <div v-if="likedMovies.length === 0" style="margin-bottom: 20px;">
                찜한 영화가 없습니다.
            </div>
            <div class="card" style="cursor: pointer;" v-for="movie in likedMovies" @click="goToDetail(movie.code)">
                <img :src="`${MovieStore.imgUrl}${movie.poster}`" alt="">
                <p>영화 제목 : {{ movie.title }}</p>
            </div>
        </div>
    </div>


    <div class="like-card">
        <h3>💗My Reviews💗</h3>
        <div class="review-card">
            <div v-if="personalReviews.length === 0" style="margin-bottom: 20px;">
                작성한 리뷰가 없습니다.
            </div>
            <div class="review-content" v-for="review in personalReviews">
                <p style="margin-top: 0; text-align: left; width: 80%; cursor: pointer; color:#454545 ;"
                    @click="goToDetail(review.movie.code)">{{ review.movie.title }} - {{ review.text }}</p>
                <button style="cursor: pointer;" @click="deleteReview(review.movie.code, review.id)">Delete</button>
            </div>
            <!-- </div> -->
        </div>
    </div>
</template>
  
<script setup>
import { onMounted, ref } from 'vue';
import Tagify from '@yaireo/tagify';
import { useMovieStore } from '@/stores/movie';
import axios from 'axios';
import { useAccountStore } from '@/stores/account';
import { useRouter } from 'vue-router';

const AccountStore = useAccountStore()
const MovieStore = useMovieStore()
const router = useRouter()

const inputGenre = ref('')
const inputActor = ref('')

console.log(MovieStore.movies)

// 태그가 추가되면 이벤트 발생

// 화이트 리스트 : 해당 문자만 태그로 추가 가능
const genreWhiteList = MovieStore.genres.map((obj) => {
    return obj.name
})
const actorWhiteList = MovieStore.actors.map((obj) => {
    return obj.name
})

const personalReviews = ref([])
const likedMovies = ref([])

const goToDetail = function (movieCode) {
    router.push({ name: 'MovieDetailView', params: { movie_id: movieCode } })
}

const deleteReview = function (movieCode, reviewId) {
    console.log(movieCode, reviewId)
    console.log(typeof movieCode, typeof reviewId)
    if (confirm('정말 삭제하시겠습니까?')) {
        axios({
            method: 'delete',
            url: `${MovieStore.url}/movies/${movieCode}/review/${reviewId}/`,
            headers: {
                Authorization: `Token ${AccountStore.token}`
            }
        })
            .then((res) => {
                console.log(res)
                getPersonalReviews()
            })
            .catch((err) => {
                console.log(err)
            })
    }
}

const getPersonalReviews = function () {
    axios({
        method: 'get',
        url: `${MovieStore.url}/movies/reviews/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        }
    })
        .then((res) => {
            console.log(res.data)
            personalReviews.value = res.data
            console.log(personalReviews.value)
        })
        .catch((err) => {
            console.log(err)
        })
}

const getLikedMovies = function () {
    axios({
        method: 'get',
        // /accounts/profile/testuser1/
        url: `${AccountStore.url}/accounts/profile/${AccountStore.user.username}/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        }
    })
        .then((res) => {
            console.log(res.data)
            likedMovies.value = res.data.like_movie
            console.log(`좋아요한 영화`, likedMovies.value)
            console.log(AccountStore.user.username)
        })
        .catch((err) => {
            console.log(err)
            console.log(`${AccountStore.user.username}`)
        })
}

onMounted(() => {
    // initialize Tagify
    new Tagify(inputGenre.value, {
        enforceWhitelist: true, // 화이트리스트에서 허용된 태그만 사용
        whitelist: genreWhiteList, // 화이트 리스트 배열. 화이트 리스트를 등록하면 자동으로 드롭다운 메뉴가 생긴다
        // userInput: false, // 입력 제한
        mode: 'select',
        dropdown: {
            maxItems: 50,
            highlightFirst: true,
        }
    })
    new Tagify(inputActor.value, {
        enforceWhitelist: true, // 화이트리스트에서 허용된 태그만 사용
        whitelist: actorWhiteList, // 화이트 리스트 배열. 화이트 리스트를 등록하면 자동으로 드롭다운 메뉴가 생긴다
        // userInput: false, // 입력 제한
        mode: 'select',
        dropdown: {
            maxItems: 50,
            highlightFirst: true,
        }
    })

    if (AccountStore.isLogin) {

        getPersonalReviews()

        getLikedMovies()
    }


})

const editPreference = function () {
    console.dir(inputActor.value.value)
    console.dir(inputGenre.value.value)
    axios({
        method: 'PUT',
        url: `${AccountStore.url}/accounts/prefer/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        },
        data: {
            like_actor: inputActor.value.value,
            like_genre: inputGenre.value.value,
        }
    }).then((res) => {
        console.log(res)
        MovieStore.getRecommendedMovies()
        AccountStore.user.likeActor = inputActor.value.value.split('"')[3]
        AccountStore.user.likeGenre = inputGenre.value.value.split('"')[3]
    }).catch((err) => {
        console.log(err)
    })
}
</script>

<style scoped>
.like-card {
    width: 100%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-top: 40px;
    padding: 0 20px;
    height: fit-content;
    box-sizing: border-box;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* 중앙 정렬 */
}


.card-area {
    width: 100%;
    display: grid;
    padding-left: 0;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    justify-content: center; /* 중앙 정렬 */
    min-height: fit-content;
    overflow-y: auto;
    overflow-x: hidden; /* 수평 스크롤 비활성화 */
}

.prefence-card {
    width: 100%;
    display: grid;
    padding-left: 0;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    justify-content: center;
    /* 중앙 정렬 */
    height: fit-content;
    overflow-y: auto;
    overflow-x: hidden;
    /* 수평 스크롤 비활성화 */
}



.card {
    width: 100%;
    height: 350px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-left: 0;
    border: solid 1px #F7F7F7;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card img {
    max-width: 100%;
    max-height: 70%;
}

.card p {
    margin-top: 10px;
}

img {
    border-radius: 20px;
    height: 250px;
    width: 200px;
    margin-bottom: 15px;
}

.pickhashtag {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.hashtag {
    color: #828282;
    height: fit-content;
}

.hashtag>div>span {
    display: inline-block;
    margin: 20px;
}

.review-content {
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 100%;
}

.review-card {
    display: flex;
    flex-direction: column;
    width: 100%;
    min-height: fit-content;
}

.button {
    border-radius: 10px;
    background-color: #828282;
    color: aliceblue;
    margin-bottom: 10px;
}

.review-content>p {
    margin-bottom: 10px;
}

.tagify {
    width: 100%;
    max-width: 700px;
}
</style>