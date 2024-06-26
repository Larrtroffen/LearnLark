<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useStore } from 'vuex'
import axios from 'axios'

const store = useStore()
const userEmail = ref(store.state.userEmail) // 使用 ref 包装 userEmail
const questions = ref<any[]>([])
const currentQuestionIndex = ref(0)
const selectedOption = ref<string>('')

// 根据问题number字段存储用户的答案
const userAnswers = ref<{ [key: number]: string }>({})

// 页面加载时从后端获取测试题目
onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/get_test', {
      params: {
        userEmail: userEmail.value // 使用 .value 从 ref 中获取值
      }
    })
    questions.value = response.data.map((item) => ({
      content: item.content,
      number: item.number, // 直接使用后端返回的number字段
      correctOption: item.correct_answer,
      options: [
        { label: 'A', text: item.selections_A },
        { label: 'B', text: item.selections_B },
        { label: 'C', text: item.selections_C },
        { label: 'D', text: item.selections_D }
      ]
    }))
  } catch (error) {
    console.error('Error fetching questions:', error)
  }
})

// 计算百分制成绩
const calculateGrade = () => {
  let score = 0
  questions.value.forEach((question) => {
    if (userAnswers.value[question.number] === question.correctOption) {
      score += 10 // 每题10分，满分为100分（10题）
    }
  })
  return score
}

// 提交答案
const handleNextClick = async () => {
  if (selectedOption.value) {
    // 提取选中选项的label并保存
    const selectedLabel = questions.value[currentQuestionIndex.value].options.find(option => option.text === selectedOption.value).label;
    userAnswers.value[questions.value[currentQuestionIndex.value].number] = selectedLabel;
    selectedOption.value = '';

    if (currentQuestionIndex.value < questions.value.length - 1) {
      currentQuestionIndex.value++;
    } else {
      try {
        const grade = calculateGrade();
        const response = await axios.post('http://127.0.0.1:8000/api/save_test', {
          userEmail: userEmail.value,  // 使用 .value 从 ref 中获取值
          grade: grade  // 确保 grade 是整数
        });
        alert(`提交成功。您的得分是：${response.data.grade}`);
      } catch (error) {
        alert('提交失败');
      }
    }
  } else {
    alert('请选择一个选项');
  }
};

// 倒计时的总时长（15分钟）
const totalSeconds = 900
const remainingSeconds = ref(totalSeconds)
// 初始化倒计时进度为 100%
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
  const sortedColors = colors.sort((a, b) => a.percentage - b.percentage)
  const matchingColorRate = sortedColors.find(crate => percentage.value < crate.percentage)
  return matchingColorRate ? matchingColorRate.color : '#20a0ff'
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
    <div class="content-section" v-if="questions.length">
      <h1 class="test-title">测试</h1>
      <div class="question-section">
        <h2 class="question-type">单选题</h2>
        <div>
          <div class="question-section">
            <el-text class="question-text">{{ currentQuestionIndex + 1 }}. {{ questions[currentQuestionIndex].content }}</el-text>
          </div>
          <div class="options-container">
            <div class="check_container" v-for="(option, index) in questions[currentQuestionIndex].options" :key="index">
              <input :id="'radio-' + index" class="hidden" type="radio" :name="'option'" :value="option.text" v-model="selectedOption">
              <label class="checkbox" :for="'radio-' + index"></label>
              <el-text class="radio-label">{{ option.text }}</el-text>
            </div>
          </div>
        </div>
      </div>
    </div>
    <el-button class="submit-button" @click="handleNextClick">{{ currentQuestionIndex < questions.values.length - 1 ? '下一题' : '提交' }}</el-button>
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
  top: 5%;
  /* 调整计时器距离顶部的距离 */
  right: 15px;
  /* 计时器距离右侧的距离 */
  width: 150px;
  /* 可以根据需要调整计时器的大小 */
  height: auto;
  /* 自动调整高度以适应内容 */
  z-index: 1000;
  /* 确保计时器在其他内容之上 */
  margin-bottom: 30px;
  display: flex;
  flex-direction: column;
  align-items: center; /* 垂直居中对齐 */
  justify-content: center; /* 水平居中对齐 */
  transform: scale(0.7); /* 数值小于1会缩小，根据需要调整 */
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
.question-section {
    margin-bottom: 20px;
    text-align: left;
}

.question-text {
    font-size: 20px;
    font-weight: bold;
    color: #333;
}

.options-container {
    width: 100%;
}

.check_container {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    padding: 10px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease;
}

.check_container:hover {
    background-color: #e0e7ff;
}

.check_container:last-child {
    margin-bottom: 0; /* Remove bottom margin for the last item */
}

.checkbox {
    position: relative;
    width: 24px;
    height: 24px;
    border: 2px solid #212fab;
    border-radius: 50%;
    cursor: pointer;
    display: block;
    transition: all 0.3s linear;
    margin-right: 10px;
    flex-shrink: 0; 
}

.checkbox::after {
    content: "";
    position: absolute;
    top: 10%;
    left: 30%;
    width: 6px;
    height: 12px;
    opacity: 0;
    transform: rotate(45deg) scale(0);
    border-right: 4px solid #ffffff;
    border-bottom: 4px solid #ffffff;
    transition: all 0.3s linear;
}

.hidden {
    display: none !important;
}

input[type="radio"]:checked + .checkbox::after {
    opacity: 1 !important;
    transform: rotate(45deg) scale(1) !important;
}

input[type="radio"]:checked + .checkbox {
    background: #212fab;
    border: none;
}
</style>