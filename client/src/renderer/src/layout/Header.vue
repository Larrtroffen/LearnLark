<script setup lang="ts">

</script>

<template>
    <div class="top-bar">
          <el-button class="link-btn">
            <div>学习</div>
          </el-button>
          <div class="sep1"></div>
          <el-button class="link-btn">
            <div>测试</div>
          </el-button>
          <div class="sep"></div>
          <img class="logo" src="..\pics\logo1.png" alt="Logo">
          <div class="sep"></div>
          <el-button class="link-btn">
            <div>记录</div>
          </el-button>
          <div class="sep1"></div>
          <el-button class="link-btn">
            <div>我的</div>
          </el-button>
    </div>
  </template>

<style scoped>
  .top-bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
}
.logo {
  width: 100px; 
  height: auto;
}
.sep {
  width: 20px;
}
.sep1 {
  width: 40px;
}
.link-btn {
  color: #000;
  background-color: #fff;
  border: none;
  border-bottom: 2px solid #72b0ed;
  font-size: 18px;
  padding: 10px 20px;
  cursor: pointer;
}
</style>