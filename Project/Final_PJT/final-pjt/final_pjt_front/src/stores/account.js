import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useMovieStore } from './movie'

export const useAccountStore = defineStore('account', () => {
  const MovieStore = useMovieStore()
  const router = useRouter()
  const url = `http://127.0.0.1:8000`
  const isLogin = ref(false)
  const token = ref(null)
  const user = ref({
    pk: null,
    username: null,
    nickname: null,
    likeActor: null,
    likeGenre: null,
  })

  const signUp = function (payload) {
    const nickname = payload.nickname
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    axios({
      method: 'POST',
      url: `${url}/accounts/registration/`,
      data: {
        nickname, username, password1, password2
      }
    })
    .then((res)=>{
      console.log('회원가입 성공')
      logIn({ username, password: password1 })
    })
    .catch((error)=>{
      alert(error.response.request.response)
    })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'POST',
      url: `${url}/dj_rest_auth/login/`,
      data: {
        username,
        password,
      }
    }).then((res) => {
      console.log('로그인 성공')
      token.value = res.data.key
      isLogin.value = true
      user.value.username = username
      MovieStore.getRecommendedMovies()

      axios({
        method: 'GET',
        url: `${url}/accounts/profile/${username}/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
        }).then((res) => {
          user.value.pk = Number(res.data.id)
          user.value.nickname = res.data.nickname
          user.value.likeGenre = res.data.like_genre?.name
          user.value.likeActor = res.data.like_actor?.name

          router.push({ name: 'MyPageHome', params: { username: username } }).then(res => alert(`로그인 성공!! "${user.value.nickname}"님, 반갑습니다.`))
        })
    }).catch((err) => {
      console.log('로그인 실패')
      console.log(err)
      alert('로그인 실패!')
    })
  }

  const logOut = function () {
    axios({
      method: 'POST',
      url: `${url}/dj_rest_auth/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    }).then((res) => {
      console.log('로그아웃 완료')
      token.value = null
      localStorage.removeItem('token'); // 로컬 스토리지에서 토큰 제거
      isLogin.value = false
      alert('로그아웃 완료!')
      router.push({ name: 'HomeView' }).then(() => {
        isLogin.value = false
        user.value = {
          pk: null,
          username: null,
          nickname: null,
          likeActor: null,
          likeGenre: null,
        }
      })
    }).catch((err) => {
      console.log(err)
    })
  }
  
  return { isLogin, token, url, user, signUp, logIn, logOut }
}, { persist: true })
