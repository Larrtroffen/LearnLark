import { createRouter, createWebHistory } from 'vue-router'

// Import components
import radio from '@renderer/components/Test/radio.vue'
import radio1 from '@renderer/components/Test/radio1.vue'
import radio2 from '@renderer/components/Test/radio2.vue'
import Login from '@renderer/components/user/Login.vue'
import Register from '@renderer/components/user/Register.vue'
import Learn from '@renderer/components/views/Learn.vue'
import MissionIni from '@renderer/components/views/Mission_ini.vue'
import Personal from '@renderer/components/views/Personal.vue'
import Test from '@renderer/components/views/Test.vue'
import Footer from '@renderer/layout/Footer.vue'
import Header from '@renderer/layout/Header.vue'
import Layout from '@renderer/layout/Layout.vue'

// Define routes
const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/radio', component: radio},
  { path: '/radio1', component: radio1},
  { path: '/radio2', component: radio2},
  { path: '/learn', component: Learn},
  { path: '/missionini', component: MissionIni},
  { path: '/personal', component: Personal},
  { pate: '/test', component: Test},
  { pate: '/layout', component: Layout},
  { pate: '/footer', component: Footer},
  { pate: '/header', component: Header},
]

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router