
<template>
  <div>
    <h1>Todo Project</h1>
    <h2>완료된 Todo : {{ store.doneTodoCount }}</h2>
    <TodoList/>
    <TodoForm/>
  </div>
</template>

<script setup>
import TodoForm from './components/TodoForm.vue';
import TodoList from './components/TodoList.vue';
import { useCounterStore } from './stores/counter';

const store = useCounterStore()









// // 파일 이름이 모듈이어서 파일 확장자를 적지 않아도 됨
//   import { useCounterStore } from '@/stores/counter';

//   const store = useCounterStore()

//   // 중앙 저장소 store에 있는 값 가져오기
//   // 중앙 저장소에 있는 값들은 참조해오는 것, 조작은 이렇게 할 수 없음
//     // -> 조작하기 위해서는 중앙 저장소에서 조작을 위한 액션을 만들어서 조작해야함
//   // component에서는 store에 상태를 추가 못함
//   // 왜 .value 안해도 나오지?

//   // state
//   console.log(store.count)
//   const newNumber = store.count +1

//   // gatters
//   console.log(store.doubleCount)
</script>

<style scoped>

</style>
