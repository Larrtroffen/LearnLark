import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import userRouter from './userRouter'
import managerRouter from './managerRouter'

const routes: RouteRecordRaw[] = [
    // 管理端
  ]
  
  const router = createRouter({
    // 路由模式
    history: createWebHistory(),
    routes,
  })
  
export default router