import { createApp } from 'vue'
import ElementPlus from 'element-plus'

import 'element-plus/dist/index.css'
import App from './App.vue'
import Vue3Lottie from 'vue3-lottie';

const app = createApp(App)

app.use(ElementPlus)
app.use(Vue3Lottie, { name: 'Vue3Lottie' });
app.mount('#app')
 