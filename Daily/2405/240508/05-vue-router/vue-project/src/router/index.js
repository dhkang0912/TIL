import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import LoginView from '@/views/LoginView.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserHome from '@/components/UserHome.vue'

const isAuthenicated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // 한꺼번에 로딩을 하면 초기 로딩이 너무 오래 걸리기 때문에 그 탭에 들어갈 때 로딩을 하겠다는 코드
      component: () => import('../views/AboutView.vue')
    },
    {
      // 다이나믹 라우팅 매치
      // 앞에 /는 필수, 끝나는 /는 없음
      path: '/user/:userId',
      // name: 'user',
      component : UserView,

      children: [
        // 중첩될 때는 슬래시 안 적음
        {path:'', name:'user', component:UserHome},
        {path: 'profile', name: 'user-profile', component: UserProfile},
        {path: 'posts', name: 'user-posts', component: UserPosts},
      ]
    },
    {
      path:'/login',
      name:'login',
      component: LoginView,

      beforeEnter: (to, from) => {
        if (isAuthenicated === true) {
          console.log('이미 로그인 상태입니다.')
          return {name:'home'}
        }
      },
    }
    
  ]
})

// // 이동하기 직전에 호출됨
// router.beforeEach((to, from) => {
//   const isAuthenicated = false

//   // 로그인이 되어있지 않고 + 이동하는 곳이 로그인이 아니라면
//   if (!isAuthenicated && to.name !== 'login') {
//     console.log('로그인이 필요합니다.')
//     return {name:'login'}
//   }
//   // console.log(to)
//   // console.log(from)
// })

export default router
