<template>
  <div>
    <h1>DetailView</h1>
    <div v-if="article">
      <p>{{ article.id }}</p>
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
      <p>{{ article.created_at }}</p>
      <p>{{ article.updated_at }}</p>
    </div>

  </div>
</template>

<script setup>
import axios from 'axios'
import {onMounted, ref} from 'vue'
import {useRoute} from 'vue-router'
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()

const route = useRoute()
const article = ref(null)

// axios에 대한 동작을 기다리지 않아서 axios 작업이 완료 되기 전에 콧수염 템플릿이 완료되면 정보가 없는 것으로 나옴
onMounted(()=>{
  axios({
    method:'get',
    url:`${store.API_URL}/api/v1/articles/${route.params.id}`
  })
  .then((response)=>{
    console.log(response.data)
    article.value = response.data
  })
  .catch((error)=>{
    console.log(error)
  })
})


</script>

<style>

</style>
