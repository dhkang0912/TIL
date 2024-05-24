
import { ref, computed, onMounted } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useAccountStore } from './account'


export const useMovieStore = defineStore('movie', () => {
  const url = `http://127.0.0.1:8000`
  const AccountStore = useAccountStore()
  const imgUrl = ref('https://image.tmdb.org/t/p/original/')

  const movies = ref([])
  const genres = ref([])
  const actors = ref([])

  // 44개를 불러옴
  const upcomingMovies = ref([])

  const recommendedMovies = ref([])

  const likedMovies = ref([])

  const getMovies = function () {
    axios({
      method: 'get',
      url: `${url}/movies/`
    })
      .then((res) => {
        // console.log(res)
        movies.value = res.data

        upcomingMovies.value = movies.value.filter((movie) => {
          return movie.status === false
        })

      })
      .catch((error) => {
        console.log(error)
      })
  }

  const getGenres = function () {
    axios({
      method: 'GET',
      url: `${url}/movies/genres/`
    }).then((res) => {
      genres.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }

  const getActors = function () {
    axios({
      method: 'GET',
      url: `${url}/movies/actors/`
    }).then((res) => {
      actors.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }

  const getRecommendedMovies = function () {
    axios({
      method: 'GET',
      url: `${url}/movies/recommended/`,
      headers: {
        Authorization: `Token ${AccountStore.token}`
      }
    }).then((res) => {
      recommendedMovies.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }

  // const getlikedMovies = function () {
  //   axios({
  //     method: 'GET',
  //     url: `${url}/movies/recommended/`,
  //     headers: {
  //       Authorization: `Token ${AccountStore.token}`
  //     }
  //   }).then((res) => {
  //     recommendedMovies.value = res.data
  //   }).catch((err) => {
  //     console.log(err)
  //   })
  // }


  return { movies, genres, actors, url, imgUrl, upcomingMovies, getMovies, getGenres, getActors, getRecommendedMovies, recommendedMovies }
}, { persist: true })
