<script setup lang="ts">
import radio from '@renderer/Functions/Test/radio.vue'
import checkbox from '@renderer/Functions/Test/checkbox.vue'
import jianda from '@renderer/Functions/Test/text.vue'
import { ref, onMounted, onUnmounted, computed } from 'vue'

// 倒计时的总时长（15分钟）
const totalSeconds = 1000
const remainingSeconds = ref(totalSeconds)
// 初始化倒计时进度为100%
const percentage = ref(100)

// 根据当前百分比确定进度条颜色
const getColor = (percentage) => {
  const colors = [
    { color: '#f56c6c', percentage: 20 },
    { color: '#e6a23c', percentage: 40 },
    { color: '#5cb87a', percentage: 60 },
    { color: '#1989fa', percentage: 80 },
    { color: '#6f7ad3', percentage: 100 },
  ]
  // 现在按百分比升序排序
  const sortedColors = colors.sort((a, b) => a.percentage - b.percentage);

  // 查找第一个百分比值大于给定百分比的颜色
  const matchingColorRate = sortedColors.find(crate => percentage < crate.percentage);

  // 返回匹配颜色或默认颜色
  return (matchingColorRate ? matchingColorRate.color : '#20a0ff');
}

const progressColor = ref(getColor(100))

// 格式化时间为 MM:SS
const formatTime = (seconds) => {
  const mins = Math.floor(seconds / 60).toString().padStart(2, '0')
  const secs = (seconds % 60).toString().padStart(2, '0')
  return `${mins}:${secs}`
}
const timeText = computed(() => formatTime(remainingSeconds.value))

let interval

onMounted(() => {
  interval = setInterval(() => {
    if (remainingSeconds.value > 0) {
      remainingSeconds.value--
      percentage.value = Math.floor((remainingSeconds.value / totalSeconds) * 100)
      progressColor.value = getColor(percentage.value)
    } else {
      clearInterval(interval)
    }
  }, 1000)
})

onUnmounted(() => {
  if (interval) {
    clearInterval(interval)
  }
})
</script>



<template>
  <div id="app" class="app-container">
    <div class="timer-wrapper">
      <div class="cir_per">
        <el-progress type="circle" :percentage="percentage" :color="progressColor" />
      </div>
      <div class="time_text"><span>{{ timeText }}</span></div>
    </div>
    <div class="content-section">
      <h1 class="test-title">测试</h1>
      <div class="question-section">
        <section>
          <h2 class="question-type">单选题</h2>
          <radio />
        </section>
        <section>
          <h2 class="question-type">多选题</h2>
          <checkbox />
        </section>
        <section>
          <h2 class="question-type">简答题</h2>
          <jianda />
        </section>
      </div>
    </div>
    <el-button class="submit-button">提交</el-button>
  </div>
</template>

<style>
.app-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  padding: 30px;
  background-color: #ffffff;
}

.timer-wrapper {
  position: fixed;
  top: 10%;
  /* 调整计时器距离顶部的距离 */
  right: 15px;
  /* 计时器距离右侧的距离 */
  width: 150px;
  /* 可以根据需要调整计时器的大小 */
  height: auto;
  /* 自动调整高度以适应内容 */
  z-index: 1000;
  /* 确保计时器在其他内容之上 */
  width: 200px;
  height: 200px;
  margin-bottom: 30px;
  display: flex;
  flex-direction: column;
  align-items: center; /* 垂直居中对齐 */
  justify-content: center; /* 水平居中对齐 */
}

.time_text {
  font-size: 18px;
  color: #55ACEE;
  display: flex;
}

.content-section {
  width: 100%;
  max-width: 800px;
  margin-top: 40px;
}

.test-title {
  font-size: 36px;
  color: #333;
  margin-bottom: 30px;
}

.question-type {
  font-size: 24px;
  color: #55ACEE;
  margin-bottom: 15px;
}

.submit-button {
  position: relative;
  display: inline-block;
  margin-top: 50px;
  padding: 15px 30px;
  font-size: 18px;
  letter-spacing: 1px;
  text-decoration: none;
  line-height: 0.3;
  color: #fff;
  background-color: #55ACEE;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.submit-button:hover {
  background-color: #4ab3f4;
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
}

.submit-button:active {
  transform: translateY(2px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>