<template>
  <div class="questionnaire-container">
    <header class="header">
      <div class="head-left"><span>{{ number }}</span></div>
      <div class="countdown-timer">
        <transition-group name="timer-fade" appear>
          <span class="timer-digit" v-for="(digit, index) in formattedTime" :key="index"
            :class="getAnimationClass(index)">
            {{ digit }}
          </span>
        </transition-group>
      </div>
    </header>

    <main class="question-content">
      <div class="question-placeholder">
        <radio></radio>
      </div>
    </main>

    <footer>
      <button class="next-question-button" disabled>下一题</button>
    </footer>


    <aside class="sidebar-decoration">

    </aside>
  </div>
</template>

<script setup>
import radio from './Test/radio.vue';
const number = '问题  1/10'
import { ref, onMounted, onUnmounted, computed } from 'vue'

const durationInSeconds = 60 * 5 // 5 minutes
let startTime
let timerInterval

const formattedTime = computed(() => {
  const elapsedTime = Math.floor((Date.now() - startTime) / 1000)
  const totalSeconds = Math.min(elapsedTime, durationInSeconds)
  const minutes = Math.floor(totalSeconds / 60)
  const seconds = totalSeconds % 60

  return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`
})

const getAnimationClass = (index) => {
  const animations = ['animate__fadeIn', 'animate__zoomIn', 'animate__pulse']
  return animations[index % animations.length]
}

onMounted(() => {
  startTime = Date.now()
  timerInterval = setInterval(() => {
    // 您可以在这里添加逻辑来处理计时结束的情况
  }, 1000)
})

onUnmounted(() => {
  clearInterval(timerInterval)
})

</script>

<style>
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
  /* 给页面一个淡灰色背景 */
}

.questionnaire-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  /* 改为min-height以适应不同屏幕尺寸 */
  background-color: #ffffff;
  /* 内容区域使用白色背景 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  /* 添加轻微阴影，提升层次感 */
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #409EFF;
  /* 使用主题色作为头部背景 */
  color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* 头部阴影效果 */
}

.header-left {
  font-size: 1.2rem;
}

.header-right {
  display: flex;
  align-items: center;
}

/* 计时器简单样式 */
.header-right>span {
  display: inline-block;
  padding: 0 0.5rem;
  font-weight: bold;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 5px;
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
  font-size: 16px;
  transition: all 0.3s ease;
  /* 添加过渡效果 */
  margin: 1rem auto 0;
  /* 上边距调整 */
}

.next-question-button:hover {
  background-color: #368ee0;
  /* 按钮悬停时的颜色加深 */
}

.next-question-button[disabled] {
  background-color: #ccc;
  cursor: not-allowed;
}

.sidebar-decoration {
  position: absolute;
  top: 0;
  right: 0;
  width: 5px;
  /* 减小宽度以更精致 */
  height: 100%;
  background: linear-gradient(to bottom, #409EFF, #368ee0);
  /* 侧边栏渐变效果 */
  opacity: 0.3;
  /* 设置透明度，不过于抢眼 */
}

.timer-digit {
  display: inline-block;
  margin-right: 5px; /* Adjust as needed */
}

.timer-fade-enter-active,
.timer-fade-leave-active {
  transition: opacity 0.5s ease;
}

.timer-fade-enter-from,
.timer-fade-leave-to {
  opacity: 0;
}


/* 优化滚动条样式 */
.question-content::-webkit-scrollbar {
  width: 8px;
}

.question-content::-webkit-scrollbar-track {
  background-color: #f5f5f5;
}

.question-content::-webkit-scrollbar-thumb {
  background-color: #409EFF;
  border-radius: 4px;
}
</style>