<template>
  <div class="login-main">
    <h1>회원가입 </h1>

    <div class="login-area">
      <div class="origin-login">
        <h2>회원가입</h2>
        <form @submit.prevent="signUp">
          <div style="padding-right: calc(20% + 30px); text-align: right;">
            <label for="username">ID : </label>
            <input type="text" name="username" id="username" v-model.trim="username" style="margin-bottom: 20px; height: 20px; width: 200px;" pattern="[A-Za-z0-9]{5,}" title="5자 이상의 영문자와 숫자만 입력하세요." required>
          </div>
          <div style="padding-right: calc(20% + 30px); text-align: right;">
            <label for="pw">PW : </label>
            <input type="password" name="password1" v-model.trim="password1" id="pw" style="margin-bottom: 20px; height: 20px; width: 200px;" pattern=".{8,}" title="8자 이상 입력하세요." required>
          </div>
          <div style="padding-right: calc(20% + 30px); text-align: right;">
            <label for="pw2">PW Confirm: </label>
            <input type="password" name="password2" id="pw2" v-model.trim="password2"  style=" margin-bottom: 20px;  height: 20px; width: 200px;" pattern=".{8,}" title="8자 이상 입력하세요." required>
          </div>
          <div style="padding-right: calc(20% + 30px); text-align: right;">
            <label for="nickname">Nickname : </label>
            <input type="text" name="nickname" id="nickname" v-model.trim="nickname" style= "height: 20px; width: 200px;" required>
          </div>
          <input type="submit" value="Sign Up" style=" margin-top: 20px; border-radius: 10px; background-color: #828282; color: aliceblue; height: 25px;">
        </form>
      </div>
  
  
      <div class="social-login">
        <h2>소셜 회원가입</h2>
        <button><img :src="googleLoginImg" alt=""></button>
      </div>
    </div>
  </div>
</template>

<script setup>
import googleLoginImg from '@/assets/google_login.png'
import { ref, watch } from 'vue';
import { useAccountStore } from '@/stores/account';
const AccountStore = useAccountStore()

// const csrfToken = ref(null)
const nickname = ref(null)
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  if (password1.value !== password2.value) {
    alert('비밀번호가 일치하지 않습니다')
  } else {
    const payload = {
      nickname : nickname.value,
      username : username.value,
      password1 : password1.value,
      password2 :password2.value
    }
  
    AccountStore.signUp(payload)
    }
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