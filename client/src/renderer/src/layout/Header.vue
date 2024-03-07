<script setup lang="ts">

</script>

<template>
  <el-header>
    <div class="top-bar">
      <el-row>
        <el-col :span="4">
          <el-button >学习</el-button>
          <el-button round>测试</el-button>
          <img class="logo" src="..\pics\logo1.png" alt="Logo">
          <el-button round>记录</el-button>
          <el-button round>我的</el-button>
        </el-col>
      </el-row>
    </div>
  </el-header>
  </template>

<style scoped>
  .top-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
}
.logo {
  width: 100px; 
  height: auto;
}
.el-row {
  margin: 10px 0;
}

</style>