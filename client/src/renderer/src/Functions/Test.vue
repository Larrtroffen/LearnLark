<template>
  <div id="app">
    <h1>测试</h1>

    <!-- 单选题 -->
    <div>

      <div class="container">
        <el-text class="title">单选题</el-text>
      </div>
      <radio>
      </radio>
    </div>
    <!-- 多选题 -->
    <div>
      <el-text class="title">多选题</el-text>
      <checkbox>
      </checkbox>
    </div>
    <!-- 简答题 -->
    <div>
      <el-text class="title">简答题</el-text>
      <jianda>
      </jianda>
    </div>

    <!-- 提交按钮 -->
    <el-button class="button" >提交</el-button>
  </div>
</template>

<script setup lang="ts">
import radio from '@renderer/Functions/Test/radio.vue'
import checkbox from '@renderer/Functions/Test/checkbox.vue'
import jianda from '@renderer/Functions/Test/text.vue'
</script>

<style scoped>
.title{
  font-size: 24px;
}
.button {
  position: relative;
  display: inline-block;
  margin: 15px;
  padding: 15px 30px;
  text-align: center;
  font-size: 18px;
  letter-spacing: 1px;
  text-decoration: none;
  line-height: 0.3;
  color: #55ACEE;
  background: transparent;
  cursor: pointer;
  transition: ease-out 0.5s;
  border: 2px solid #55ACEE;
  border-radius: 10px;
  box-shadow: inset 0 0 0 0 #55ACEE;
}

.button:hover {
  color: white;
  box-shadow: inset 0 -100px 0 0 #55ACEE;
}

.button:active {
  transform: scale(0.9);
}
</style>