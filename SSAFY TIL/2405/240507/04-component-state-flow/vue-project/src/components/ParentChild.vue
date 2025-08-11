<template>
  <div>
    {{ myMsg }}
    {{ dynamicProps }}
    <ParentGrandChild 
      :my-msg="myMsg"
      @update-name="updateName"
    />
    <button @click="$emit('someEvent')">버튼</button>
    <button @click="buttonclick">버튼2</button>
    <button @click="emitArgs">추가 인자 전달</button>

  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'

// 내려 받은 props를 선언
// 받는 쪽은 자바스크립트, 받는 쪽의 문법을 지킴
// defineProps(['myMsg'])

// defineProps({
//   myMsg : String,
// })

const props = defineProps({
  // 여러가지 타입의 가능성
  // myMsg : [String, Object],
  myMsg : {
    type : String,
    // 필수인자로 디버깅할 때 유효성 검사를 통해 알 수 있음
    required:true,
  },
  dynamicProps : String,

})

console.log(props)
console.log(props.myMsg)

const emit = defineEmits(['myFocus', 'emitArgs', 'updateName'])

const buttonclick = function (){
  emit('myFocus')
}

const emitArgs = function(){
  emit('emitArgs', 1, 2, 3)

}

const updateName = function(){
  emit('updateName')
}

</script>



<style scoped>

</style>