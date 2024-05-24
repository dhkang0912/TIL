import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

// local storage 초기화
// window.localStorage.clear()

// Pinia 인스턴스 생성
const pinia = createPinia()

// Pinia에 플러그인 추가
pinia.use(piniaPluginPersistedstate)

// Vue 애플리케이션 생성
const app = createApp(App)

// Pinia를 Vue 앱에 추가
app.use(pinia)

// 라우터 등록
app.use(router)

// 앱을 #app 엘리먼트에 마운트
app.mount('#app')
