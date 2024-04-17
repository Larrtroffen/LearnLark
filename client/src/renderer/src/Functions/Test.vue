<template>
    <div id="app">
      <h1>测试</h1>
  
      <!-- 单选题 -->
      <div>
        <h2>单选题</h2>
        <div>
          <p>单选题内容</p>
          <el-radio-group>
            <el-radio>选项1</el-radio>
            <el-radio>选项2</el-radio>
            <el-radio>选项3</el-radio>
          </el-radio-group>
        </div>
      </div>
  
      <!-- 多选题 -->
      <div>
        <h2>多选题</h2>
        <div>
          <p>多选题内容</p>
          <el-checkbox-group>
            <el-checkbox>选项1</el-checkbox>
            <el-checkbox>选项2</el-checkbox>
            <el-checkbox>选项3</el-checkbox>
          </el-checkbox-group>
        </div>
      </div>
  
      <!-- 简答题 -->
      <div>
        <h2>简答题</h2>
        <div>
          <p>简答题内容</p>
          <el-input></el-input>
        </div>
      </div>
  
      <!-- 提交按钮 -->
      <el-button>提交</el-button>
    </div>
  </template>
  
  <script setup lang="ts">
    // Add TypeScript logic here if needed
  </script>
  