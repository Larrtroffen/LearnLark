<template>
  <div class="wrapper">
    <div class="sidebar-left"></div>
    <div class="content">
      <div class="banner">
        <h2>制定您的学习计划</h2>
        <p>让我们一起迈向知识的海洋！</p>
      </div>
      <el-form class="form-container">
        <el-form-item label="学习天数">
          <i class="el-icon-date"></i>
          <el-input type="number" />
          <el-date-picker class="custom-datepicker" v-model="studyDateRange" type="daterange" start-placeholder="开始日期"
            end-placeholder="结束日期" @change="calculateStudyDays" />
        </el-form-item>
        <el-form-item label="任务名称">
          <el-input />
        </el-form-item>
        <el-form-item label="题目类型">
          <el-select placeholder="请选择题目类型">
            <el-option />
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary">保存任务</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="sidebar-right"></div>
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
}

.sidebar-left,
.sidebar-right {
  width: 15%;
  background-color: #f2f2f2;
}

.content {
  width: 70%;
  margin: 0 auto;
}

.banner {
  background: linear-gradient(to bottom, #6bd3f3, #00c5ec);
  color: white;
  padding: 20px;
  text-align: center;
  border-radius: 5px 5px 0 0;
  position: relative;
  z-index: 1;
}


/* 容器美化 */
.form-container {
  background-color: #f2f2f2;
  padding: 30px;
  position: relative;
  background-image: url('../pics/tem.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-blend-mode: multiply;
  opacity: 0.95;
  z-index: 1;
  padding-top: 0;
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

.banner {
  background: linear-gradient(to bottom, #6bd3f3, #00c5ec);
  color: white;
  padding: 20px;
  text-align: center;
  border-radius: 5px 5px 0 0;
  position: relative;
  z-index: 1;
  /* 确保横幅在背景覆盖层之上 */
}

.el-form {
  width: 60%;
  margin: auto;
  padding-top: 50px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  background-color: transparent;
  border-radius: 5px;
}

.el-select .el-input.is-focus .el-select__caret,
.el-select .el-input__inner:hover .el-select__caret {
  display: none;
  /* 隐藏默认箭头 */
}

.el-select:before {
  content: "\25BC";
  /* 使用向下的三角形字符作为箭头，也可以用背景图片 */
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  font-size: 0.8em;
  color: #909399;
  /* 箭头颜色 */
  pointer-events: none;
  /* 确保点击箭头也能触发下拉菜单 */
}

/* 自定义下拉菜单的样式 */
.el-select-dropdown {
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  overflow: hidden;
}

.el-select-dropdown__list {
  padding: 0;
  margin: 0;
}

.el-select-dropdown__item {
  padding: 8px 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  user-select: none;
}

.el-select-dropdown__item:hover,
.el-select-dropdown__item.is-hover,
.el-select-dropdown__item:focus {
  background-color: #f5f7fa;
  color: #409eff;
  /* 鼠标悬停或聚焦时的文字颜色 */
}

.el-select-dropdown__item.selected {
  font-weight: 500;
  color: #409eff;
  /* 选中项的文字颜色 */
}

/* 如果需要调整滚动条样式 */
.el-select-dropdown__wrap ::-webkit-scrollbar {
  width: 6px;
}

.el-select-dropdown__wrap ::-webkit-scrollbar-thumb {
  background-color: #b3b3b3;
  border-radius: 3px;
}

.el-select:before {
  content: "";
  position: absolute;
  top: 50%;
  right: 10px;
  /* 根据需要调整位置 */
  transform: translateY(-50%);
  width: 12px;
  height: 12px;
  background-image: url(../pics/fenxiang.svg);
  background-size: contain;
  background-repeat: no-repeat;
  /* ... 根据图标调整样式 ... */
}

.el-select-dropdown {}

.el-form-item {
  display: flex;
  align-items: center;
  padding: 20px;
}

.el-button {
  display: block;
  width: 100px;
  margin: auto;
}

/* 统一输入框样式 */
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

.el-button {
  color: #fff;
}

.el-form-item__label {
  width: 80px;
  color: #606266;
  font-weight: 500;
}

/* 日期选择器的特殊样式 */
.el-date-editor {
  box-sizing: border-box;
}

.el-range-separator {
  line-height: 40px;
}

.el-picker-panel {
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.el-date-table td.available:hover span,
.el-date-table td.current:not(.disabled) span {
  background-color: var(--el-color-primary-light-9);
  color: #409EFF;
}

.el-date-table td.disabled div {
  color: #c0c4cc;
}

@media (max-width: 600px) {
  .el-form {
    width: 90%;
  }
}
</style>
