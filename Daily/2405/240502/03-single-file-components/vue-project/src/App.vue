<template>
  <div>
    <h1>App.vue</h1>
    <!-- 닫는 태그가 따로 없음, 하나로 합침 -->
    <MyComponent/>
  </div>
</template>


<script setup>
// 상대 경로로 불러옴
// import MyComponent from './components/MyComponent.vue';
// @는 src/와 동일
import MyComponent from '@/components/MyComponent.vue'
</script>


<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
