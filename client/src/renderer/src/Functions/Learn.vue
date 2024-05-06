<template>
<div class="questionnaire-container">
  <header class="header">
    <div class="header-left">
      <p>问题 1 / 5</p>
    </div>
    <div class="header-right">
      <!-- 计时器组件位置（HTML结构示意，实际计时功能需通过JavaScript实现） -->
      <span role="timer" aria-label="计时器"></span>
    </div>
  </header>

  <main class="question-content">
    <!-- 问题内容将动态加载的位置 -->
    <div class="question-placeholder">这里是题目内容</div>
  </main>

  <footer>
    <button class="next-question-button" disabled>下一题</button>
  </footer>

  <!-- 边栏装饰 -->
  <aside class="sidebar-decoration">
    <!-- 使用SVG作为边栏装饰 -->
    <svg viewBox="0 0 100 100" preserveAspectRatio="none">
      <path d="M0 0 Q 50 100 100 0" stroke="#55ACEE" stroke-width="1" fill="none"></path>
    </svg>
  </aside>
</div>
</template>
<style scoped>
.questionnaire-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

.header-left {
  font-size: 1.2rem;
}

.header-right {
  /* 你可以根据实际需要调整计时器样式 */
}

.question-content {
  flex-grow: 1;
  overflow-y: auto;
  padding: 2rem;
}

.next-question-button {
  padding: 10px 20px;
  background-color: #409EFF;
  color: white;
  border: none;
  cursor: pointer;
  outline: none;
  border-radius: 4px;
  margin: 0 auto;
  display: block;
  font-size: 16px;
  transition: background-color 0.3s;
}

.next-question-button[disabled] {
  background-color: #ccc;
  cursor: not-allowed;
}

.sidebar-decoration {
  position: absolute;
  top: 0;
  right: 0;
  width: 10px;
  height: 100%;
  overflow: hidden;
}
</style>
<script setup>


</Script>