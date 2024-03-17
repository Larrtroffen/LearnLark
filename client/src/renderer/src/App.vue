<script setup lang="ts">
    import Header from './layout/Header.vue';
    import Footer from './layout/Footer.vue';
    

</script>

<template>
    <div class="common-layout">
    <el-container>
      <el-header>
        <Header />
      </el-header>
      <el-main>

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
