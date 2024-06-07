<template>
  <div>
    <RouterLink :to="{name:'user-profile'}">UserProfile</RouterLink>
    <RouterLink :to="{name:'user-posts'}">UserPosts</RouterLink>
    <h1>UserView</h1>
    <!-- props 형태로 전달되어 아래와 같은 방식으로 전달받은 걸 사용 가능 -->
    <!-- 자바스크립트로도 사용 가능 -->
    <h2>{{ $route.params.userId }}번 User 페이지</h2>
    <h2>{{ userId }}번 User 페이지</h2>
    <button @click="goHome">goHome</button>
    <!-- 같은 페이지에서 같은 페이지로 이동함, 페이지간 이동은 없지만 값은 바꿔야 함, 특정 일부분만 바뀜 -->
    <button @click="routeUpdate">100번 유저 페이지로!</button>
    <hr>
    <RouterView/>
  </div>
</template>

<script setup>
import {ref} from 'vue'
// useRoute는 Route 안에 있는 객체를 접근하기 위함
import {useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate} from 'vue-router'

const route = useRoute()
// 자바스크립트에서 반응형 변수에 담아서 이걸 출력하는 걸 권장
const userId = ref(route.params.userId)

// 코드로서 링크 전환도 가능
const router = useRouter()
const goHome = function(){
  // router link에서 home을 누르는 것과 동일
  router.push({name:'home'})

  // 히스토리 스택에 푸시하는 코드가 아니라서 뒤로가기가 안됨, 현재 위치 변경
  // router.replace({name:'home'})
}

onBeforeRouteLeave((to, from)=>{
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    // 네비게이션 이동에 대한 취소
    return false
  }
  // return이 생략된 경우 to로 이동
  // return true
})

const routeUpdate = function(){
  router.push({name:'user', params:{userId:100}})
  // 반응형 변수가 재할당이 안됨, 바꿔줘야 함
}

// 현재 주소는 동일하지만 params의 내용이 바뀐 경우
// 반응형 변수가 재할당이 안됨(새로고침을 하지 않은 상태로 컴포넌트를 재사용하기 때문), 바꿔줘야 함
// 컴포넌트는 그대로지만 그 안의 내용만 조금 변경되는 경우 처리할 때
onBeforeRouteUpdate((to, from) => {
  // console.log(to)
  userId.value = to.params.userId
})

</script>

<style scoped>

</style>