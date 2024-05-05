<template>
  <div id="app">
    <div class="timer">
      <div class="cir_per">
        <el-progress type="circle" :percentage="percentage" :color="progressColor" />
      </div>
      <div class="time_text"> <span>{{ timeText }}</span>
      </div>
    </div>
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
    <el-button class="button">提交</el-button>
  </div>
</template>

<script setup lang="ts">
import radio from '@renderer/Functions/Test/radio.vue'
import checkbox from '@renderer/Functions/Test/checkbox.vue'
import jianda from '@renderer/Functions/Test/text.vue'
import { ref, onMounted, onUnmounted, computed } from 'vue'

// 倒计时的总时长（15分钟）
const totalSeconds = 20
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

<style scoped>
.title {
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

.timer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>