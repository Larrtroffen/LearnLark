<template>
  <div class="wrapper">
    <div class="content">
      <div class="banner">
        <h2>制定您的学习计划</h2>
        <p>让我们一起迈向知识的海洋！</p>
      </div>
      <el-form class="form-container">
        <el-form-item label="学习天数">
          <i class="el-icon-date"></i>
          <el-input type="number" placeholder="输入天数" />
          <el-date-picker class="custom-datepicker" v-model="studyDateRange" type="daterange" start-placeholder="开始日期"
            end-placeholder="结束日期" @change="calculateStudyDays" />
        </el-form-item>
        <el-form-item label="任务名称">
          <el-input placeholder="输入任务名称" />
        </el-form-item>
        <el-form-item label="题目类型">
          <el-select placeholder="请选择题目类型">
            <el-option label="选择类型" value="type"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary">保存任务</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="sidebar sidebar-right"></div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

interface DateRange {
  start: Date;
  end: Date;
}

const studyDays = ref<string | null>(null);
const studyDateRange = ref<DateRange[]>([]);
const calculateStudyDays = () => { };
</script>

<style scoped>
.wrapper {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  min-height: 100vh;
  background: linear-gradient(to right, #f0f4f8, #d9e4f5);
}

.sidebar {
  width: 15%;
  background-color: #f2f2f2;
}

.content {
  width: 70%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  border-radius: 10px;
}

.banner {
  background: linear-gradient(to bottom, #98def3, #1ccef2);
  color: white;
  padding: 20px;
  text-align: center;
  border-radius: 10px 10px 0 0;
  position: relative;
  z-index: 1;
  width: 100%;
  margin-bottom: 0; /* Remove bottom margin */
  margin-top: 0%;
}

.form-container {
  width: 100%;
  background-color: rgba(255, 255, 255, 0.9);
  padding: 0 30px 30px; /* Remove top padding */
  background-image: url('../pics/tem.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-blend-mode: multiply;
  border-radius: 0 0 10px 10px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  position: relative;
}

.form-container::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(255, 255, 255, 0.7);
  z-index: -1;
  pointer-events: none;
}

.el-form {
  width: 80%;
  margin: auto;
}

.el-form-item {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.el-form-item__label {
  width: 100px;
  color: #606266;
  font-weight: 500;
}

.el-input,
.el-date-editor,
.el-select .el-input {
  width: 100%;
  height: 40px;
  line-height: 40px;
  border-radius: 4px;
  border-color: #dcdfe6;
}

.el-input__inner,
.el-select .el-input__inner {
  padding: 0 15px;
  font-size: 14px;
  color: #333;
}

.custom-datepicker {
  margin-top: 10px;
}

.el-button {
  width: 100px;
  margin: auto;
  color: #fff;
}

@media (max-width: 768px) {
  .content {
    width: 90%;
  }

  .el-form {
    width: 100%;
  }

  .el-form-item__label {
    width: 80px;
  }
}

@media (max-width: 600px) {
  .wrapper {
    flex-direction: column;
  }

  .sidebar {
    display: none;
  }

  .content {
    width: 100%;
  }

  .el-form {
    width: 100%;
  }
}
</style>