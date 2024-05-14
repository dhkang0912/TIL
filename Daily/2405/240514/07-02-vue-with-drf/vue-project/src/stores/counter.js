import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()

  const isLogin = computed(()=>{
    if (token.value === null) {
      return false
    }
    else {
      return true
    }
  })

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers:{
        Authorization:`Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 사용자 입력 데이터를 받아, axios로 django에 요청을 보냄
  const signUp = function(payload){
    // 구조분해 할당
    const {username, password1, password2} = payload

    axios({
      method:'post',
      url:`${API_URL}/accounts/signup/`,
      data:{
        username,
        password1,
        password2,
      }
    })
      .then((res)=>{
        console.log('회원가입 성공')
        const password = password2
        LogIn({username, password})
      })
      .catch((error)=>{console.log(error)})

  }

  const LogIn = function(payload){
    // 구조분해 할당
    const {username, password} = payload

    axios({
      method:'post',
      url:`${API_URL}/accounts/login/`,
      data:{
        username,
        password,
      }
    })
      .then((res)=>{
        // 로그인 성공 후 토큰 저장
        console.log('로그인 성공')
        console.log(res.data.key)

        token.value = res.data.key
        router.push({name:'ArticleView'})
        
      })
      .catch((error)=>{console.log(error)})

  }

  return { articles, API_URL, getArticles, signUp, LogIn, token, isLogin }
}, { persist: true })
