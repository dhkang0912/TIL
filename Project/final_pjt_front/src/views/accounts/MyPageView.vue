<template>
  <div>
      <h1>{{ AccountStore.user.nickname }}</h1>
      <div class="myPageRouterlink">
        <span><RouterLink :to="{name:'MyPageHome'}">My Page</RouterLink></span>
        <span><RouterLink :to="{name: 'MyPageUserEdit'}">Info Edit</RouterLink></span>
      </div>

      <RouterView/>
  </div>

</template>

<script setup>
import { useAccountStore } from '@/stores/account';
import { RouterLink, RouterView } from 'vue-router';

const AccountStore = useAccountStore()
</script>

<style scoped>
.router-link-active {
  color: #1D97C1; /* 활성화된 링크의 글씨 색상 변경 */
}

.router-link-active + .link-context {
  color: #53C7F0; /* 활성화된 링크 및 아래 텍스트의 색상 변경 */
}

a {
  text-decoration: none;
  color: black;
  margin-bottom: 0;
  font-size: 20px;
  margin-right: 40px;
}

.myPageRouterlink{
  display: flex;
  justify-content: space-around;
  width: 100%;
}


</style>