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
import Home from '@renderer/layout/Home.vue'

// Define routes
const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/radio', component: radio},
  { path: '/radio1', component: radio1},
  { path: '/radio2', component: radio2},
  { path: '/',  
    children:[
      { path: '', component:Home},
      { path: 'learn', component: Learn},
      { path: 'missionini', component: MissionIni},
      { path: 'personal', component: Personal},
      { path: 'test', component: Test},
    ]}
]

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router