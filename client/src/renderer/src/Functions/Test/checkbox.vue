<template>
    <div>
      <el-text class="content">题目</el-text>
      <div class="container">
        <el-checkbox-group v-model="checkedOptions" class="check-group">
          <el-checkbox label="A" class="checkbox">
            <el-text>选项A  内容</el-text>
          </el-checkbox>
          <el-checkbox label="B" class="checkbox">
            <el-text>选项B  内容</el-text>
          </el-checkbox>
          <el-checkbox label="C" class="checkbox">
            <el-text>选项C  内容</el-text>
          </el-checkbox>
        </el-checkbox-group>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const checkedOptions = ref([]);
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
  }
  
  .checkbox {
    display: flex;
    position: relative;
    align-items: center;
    padding-left: 30px;
    margin-bottom: 10px;
    cursor: pointer;
  }
  
  .checkbox input[type="checkbox"] {
    position: absolute;
    opacity: 0;
    cursor: pointer;
  }
  

  </style>
  