import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/movies/HomeView.vue'
import MovieDetailView from '@/views/movies/MovieDetailView.vue'
import MovieListView from '@/views/movies/MovieListView.vue'
import LogInView from '@/views/accounts/LogInView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'
import MyPageView from '@/views/accounts/MyPageView.vue'
import MovieHashTag from '@/components/movies/MovieHashTag.vue'
import MovieItem from '@/components/movies/MovieItem.vue'
import MovieRecommend from '@/components/movies/MovieRecommend.vue'
import MovieUpcoming from '@/components/movies/MovieUpcoming.vue'
import Review from '@/components/movies/Review.vue'
import ReviewItem from '@/components/movies/ReviewItem.vue'
import MyPageHome from '@/components/accounts/MyPageHome.vue'
import MyPageUserEdit from '@/components/accounts/MyPageUserEdit.vue'
import MyPageUserEditDetail from '@/components/accounts/MyPageUserEditDetail.vue'
import { useAccountStore } from '@/stores/account';

// const AccountStore = useAccountStore()

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/movies',
      name: 'MovieListView',
      component: MovieListView,
      children: [
        {
          path: 'recommend', name: 'MovieRecommend', component: MovieRecommend,
          beforeEnter: (to, from) => {
            if (!useAccountStore().isLogin) {
              alert(`로그인이 필요합니다.`)
              return { name: 'LogInView' }
            }
          }
        },
        { path: 'upcoming', name: 'MovieUpcoming', component: MovieUpcoming },
      ],
    },
    {
      path: '/movies/:movie_id',
      name: 'MovieDetailView',
      component: MovieDetailView
    },
    {
      path: '/mypage/:username',
      name: 'MyPageView',
      component: MyPageView,
      children: [
        { path: 'home', name: 'MyPageHome', component: MyPageHome },
        { path: 'edit-info', name: 'MyPageUserEdit', component: MyPageUserEdit },
      ],
      beforeEnter: (to, from) => {
        if (!useAccountStore().isLogin) {
          alert(`로그인이 필요합니다.`)
          return { name: 'LogInView' }
        }
      }

    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },

  ]
})

router.beforeEach((to, from, next) => {
  window.scrollTo(0, 0);
  next();
});

export default router
