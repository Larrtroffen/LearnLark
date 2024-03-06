import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import router from './router/router'

import 'element-plus/dist/index.css'
import App from './App.vue'

const app = createApp(App)

app.use(router)
app.use(ElementPlus)
app.mount('#app')