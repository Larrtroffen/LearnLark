<template>
  <div class="container">
    <el-row class="header">
      <el-col :span="24">
        <div class="header-content">
          <div class="title">绿创共享汇</div>
          <div class="timer">30:00</div>
        </div>
      </el-col>
    </el-row>
    <div>
      <danxuan>
      </danxuan>
    </div>
    <el-row class="footer">
      <el-col :span="24">
        <el-button type="primary" @click="submitAnswer" :disabled="isDisabled(answer)">下一题</el-button>
      </el-col>
    </el-row>
  </div>
  ]
</template>

<script setup>
import danxuan from './Test/radio.vue';
</script>

<style scoped>
.container {
  background-color: #f5f5f5;
  padding: 20px;
}

.header {
  background-color: #ffffff;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.title {
  font-size: 20px;
  color: #333;
}

.timer {
  font-size: 16px;
  color: #999;
}

.question {
  background-color: #ffffff;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.question-title {
  font-size: 16px;
  color: #333;
}

.question-body {
  padding: 10px;
}

.footer {
  background-color: #ffffff;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.footer button {
  width: 100%;
  height: 40px;
  font-size: 16px;
  background-color: #0095ff;
  color: #ffffff;
  border: none;
  cursor: pointer;
  transition: all 0.3s;
}

.footer button:hover {
  background-color: #0081cc;
}
</style>
