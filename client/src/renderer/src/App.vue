<script setup lang="ts">
import { onMounted } from 'vue';
import { useStore } from 'vuex';
import router from './router';

// 获取 store 实例
const store = useStore();

onMounted(() => {
  if (store.getters.isAuthenticated) {
    // 如果用户已登录，则跳转到/home
    router.push('/home');
  } else {
    // 如果用户未登录，则跳转到/login
    router.push('/login');
  }
});
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-main>
        <RouterView />
      </el-main>
    </el-container>
  </div>
</template>

<style>
.common-layout {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}
</style>