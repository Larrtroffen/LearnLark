<script setup lang="ts">
    import Footer from './layout/Footer.vue';
    import Header from './layout/Header.vue';
    import Layout from './layout/Layout.vue';
</script>

<template>
    <div class="common-layout">
    <el-container>
      <el-header>
        <Header />
      </el-header>
      <el-main class="el-main">
        <Layout />
      </el-main>
      <el-footer>
        <Footer />
      </el-footer>
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
