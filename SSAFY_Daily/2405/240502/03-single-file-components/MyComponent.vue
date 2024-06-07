<template>
  <div>
    <p class='greeting'> {{ msg }} </p>
  </div>
</template>

<!-- setup 함수 안 -->
<script setup>
// ref 사용 시 기존에는 구조 분해 할당으로 했지만 이제 import 하게 됨
// 이미 setup 함수 안이라서 return이 따로 필요하지 않음

// from 이후 vue는 문자열로 작성해야함
import {ref} from 'vue'

const msg = ref('Hello')


</script>

<!-- css 파일 안과 동일 -->
<style scoped>
.greeting {
  color : crimson;
}

</style>