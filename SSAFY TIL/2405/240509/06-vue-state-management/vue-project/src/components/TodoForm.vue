<template>
  <div>
    <!-- vue에서 선택하기 위한 ref 속성이 있음 -->
    <form @submit.prevent="createTodo(todoText)" ref="formElem">
      <input type="text" v-model="todoText">
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const todoText = ref('')
// 선택하기 위해 쓴 것이라 값은 null
// ref 변수로 속성에 작성한 것과 이름을 동일하게 선언
const formElem = ref(null)
console.log(formElem)

const createTodo = function(todoText){
  store.addTodo(todoText)
  // querySelector로 Dom을 조작하지 않음
  // ref 속성을 통해 접근
  formElem.value.reset()

}

</script>

<style scoped>

</style>