<template>
  <div class="login-main">
    <h1>로그인 </h1>

    <div class="login-area">
      <div class="origin-login">
        <h2>로그인</h2>
        <form @submit.prevent="logIn">
          <div style="padding-right: calc(20% + 30px); text-align: right;">
            <label for="username">ID : </label>
            <input type="text" name="username" id="username" v-model.trim="username" style="margin-bottom: 20px; height: 20px; width: 200px;">
          </div>
          <div style="padding-right: calc(20% + 30px); text-align: right;">
            <label for="password">PW : </label>
            <input type="password" name="password" id="password" v-model.trim="password" style="height: 20px; width: 200px;">
          </div>
          <input type="submit" value="Log In" style=" margin-top: 20px; border-radius: 10px; background-color: #828282; color: aliceblue; height: 25px;">
        </form>
      </div>
  
  
      <div class="social-login">
        <h2>소셜 로그인</h2>
        <button><img :src="googleLoginImg" alt=""></button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import googleLoginImg from '@/assets/google_login.png'
import { useAccountStore } from '@/stores/account';

const AccountStore = useAccountStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  AccountStore.logIn(payload)
}
</script>

<style scoped>
.login-area{
  display: flex;
  justify-content: center;
  width: 100%;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  height: 650px;
  align-items: center;
  display: relative;
}

.origin-login{
  width: 600px;  
  border-right: 1px solid #5F5F5F;
}

.social-login{
  width: 600px;
  text-align: center;
}


.login-main{
  display: flex;
  justify-content: center;
  align-items: center;
}

img{
  height: 60px;
  width: 250px;
}

button{
  background-color: transparent;
  border: none;
  cursor: pointer;
}
</style>