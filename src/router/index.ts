import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      name: '',
      path: '/',
      redirect: '/index',
    },
    {
      name: 'index',
      path: '/index',
      component: () => import('@/views/Index.vue'),
    },
  ],
})

export default router
