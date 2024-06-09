<script setup lang="ts">
import Footer from "./Footer.vue";
import Layout from "./Layout.vue";
import Header from "./Header.vue";
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <Header />
      </el-header>
      <el-main>
        <Layout />
      </el-main>
      <el-footer>
        <Footer />
      </el-footer>
    </el-container>
  </div>
</template>

<style scoped>
.common-layout {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}
</style>