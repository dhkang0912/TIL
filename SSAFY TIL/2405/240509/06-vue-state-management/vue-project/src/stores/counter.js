import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

// pinia가 적용되더라도 prop을 혼용해서 씀

export const useCounterStore = defineStore('counter', () => {
  
  let id = 0
  const todos = ref([
  ])

  const addTodo = function(todoText){
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false,
    })
  }

  const deleteTodo = function(todoId){
    // console.log(todoId)
    // todos 상태에서 인자로 전달된 todo(삭제 대상)을 찾아서 & 삭제를 한 새로운 배열을 반환

    // 삭제 대상의 인덱스를 찾기
    const index = todos.value.findIndex((todo)=>todo.id === todoId)
    // console.log(index)
    
    // 찾은 인덱스를 활용하여 todos에서 삭제 후 새로운 todos로 교체
    todos.value.splice(index, 1)

  }

  const updateTodo = function(todoId){
    // 전달 받은 todoId(수정 대상)을 활용
    // console.log(todoId)

    // todos 배열을 순회하면서 id가 일치하면 idDone을 반대로 바꾸고
    // 변경된 새로운 배열을 반환 => map을 써서 새로운 배열로 갈아끼워짐
    todos.value = todos.value.map((todo)=>{
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  const doneTodoCount = computed(()=>{
    const doneTodos = todos.value.filter((todo)=>todo.isDone)
    return doneTodos.length
  })

  return { id, todos, addTodo, deleteTodo, updateTodo, doneTodoCount }
}, {persist:true})
