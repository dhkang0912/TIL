<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->
    <nav>
      <RouterLink class="logo" style="font-size: 20px;" :to="{ name: 'HomeView' }">Movie Sh#rping</RouterLink>
      <div class="nav-links">
        <div class="login" v-show="AccountStore.isLogin">
          <RouterLink :to="{ name: 'MovieRecommend' }">Movies</RouterLink>
          <a href="#" @click="AccountStore.logOut">logout</a>
          <RouterLink :to="{ name: 'MyPageHome', params: { username: 1 } }">My Page</RouterLink>
        </div>
        
        <div class="notlogin" v-show="!AccountStore.isLogin">
          <RouterLink :to="{ name: 'MovieUpcoming' }">Movies</RouterLink>
          <RouterLink :to="{ name: 'LogInView' }">Log In</RouterLink>
          <RouterLink :to="{ name: 'SignUpView' }">Sign Up</RouterLink>
        </div>
      </div>
    </nav>
  </header>

  <RouterView class="container" />

  <footer>
    <span class="logo">Movie Sh#rping</span>
    <span class="footercontent">&copy;copy right reserved</span>
    <span class="footercontent"> ️Doohong Kang, GyuBeom Seo </span>
  </footer>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, RouterLink, RouterView } from 'vue-router'
import { useAccountStore } from './stores/account';
import { useMovieStore } from './stores/movie';

const AccountStore = useAccountStore()
const MovieStore = useMovieStore()


onMounted(()=>{
  MovieStore.getMovies()
  MovieStore.getGenres()
  MovieStore.getActors()
})
</script>

<style scoped>
header {
  position: fixed;
  /* 화면에 고정 */
  top: 0;
  /* 상단에 고정 */
  left: 0;
  /* 좌측에 고정 */
  width: 100%;
  /* 전체 너비 */
  height: 40px;
  background-color: #2A2A2A;
  color: white;
  text-align: center;
  padding: 10px 0;
  z-index: 1000;
  min-width: 500px;
  /* 다른 요소 위에 표시되도록 z-index 설정 */
}

nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  padding: 0 20px;
  font-size: 20px;
  margin-bottom: 20px;

}

nav a,
nav a:visited,
nav a:hover,
nav a:active,
nav RouterLink {
  color: white;
  text-decoration: none;
}

.nav-links {
  display: flex;
  justify-content: space-between;
}


footer {
  width: 100%;
  /* 전체 너비 */
  height: 40px;
  background-color: #2A2A2A;
  color: white;
  text-align: center;
  padding: 10px 0;
  z-index: 1000;
  /* 다른 요소 위에 표시되도록 z-index 설정 */
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.footercontent {
  font-size: 12px;
  
}

.container {
  margin-top: 35px;
  /* 헤더 높이만큼 마진 추가 */
  padding: 40px;
  font-family: '기본';
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 100%;
}
a{
  margin-right: 10px;
  font-size: 16px;
}

</style>
