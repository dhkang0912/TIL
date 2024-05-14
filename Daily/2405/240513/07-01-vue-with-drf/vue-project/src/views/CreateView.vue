<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title">
      <br>
      <textarea v-model.trim="content"></textarea>
      <input type="submit" value="">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';
import {useRouter} from 'vue-router'
const store = useCounterStore()
const router = useRouter()

const title = ref(null)
const content = ref(null)

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value,
    }
  })
    .then((response) => {
      console.log(response.data)
      router.push({name:'ArticleView'})
  })
    .catch((error)=>{
      console.log(error)
    })
}

</script>

<style></style>
