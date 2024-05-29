<template>
  <div class="app-container">
    <el-header class="test_header">
      <div class="head-left">
        <span>{{ number }}</span>
      </div>
    </el-header>
    <el-main class="test_main">
      <transition name="animate__animated animate__bounce" enter-active-class="animate__swing" leave-active-class="animate__fadeOutTopLeft">
        <radio />
      </transition>
    </el-main>
    <el-footer class="test_footer">
      <div class="switch_buttons">
        <el-button class="updown" @click="prevQuestion">
          上一题
        </el-button>
        <el-button class="updown" @click="nextQuestion">
          下一题
        </el-button>
      </div>
      <div class="submit_button">
        <el-button class="Btn" @click="submit">
          提交
          <svg t="1716798805138" class="svgIcon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2140" xmlns:xlink="http://www.w3.org/1999/xlink">
            <path d="M414.273133 1024a19.76097 19.76097 0 0 1-19.741211-20.488101l8.762126-237.513979a19.749115 19.749115 0 0 1 4.202738-11.471084l503.439415-641.372015-822.359463 475.187017 249.409882 129.274208c9.688823 5.021748 13.47267 16.947289 8.450922 26.635125-5.023724 9.687835-16.946301 13.471682-26.635125 8.449934L38.362218 606.82539a19.758006 19.758006 0 1 1-0.793324-34.650361l932.344942-538.738859a19.759982 19.759982 0 0 1 29.505118 19.454706l-109.172395 912.697585a19.758994 19.758994 0 0 1-28.848132 15.124522L609.347756 847.568976l-181.518965 171.052626a19.754055 19.754055 0 0 1-13.555658 5.378398z m28.276109-250.126145l-6.748685 182.935685 156.731307-147.692555a19.76097 19.76097 0 0 1 22.780144-3.091294l239.112482 126.310359L950.834551 126.32913 442.549242 773.873855z" p-id="2141"></path>
          </svg>
        </el-button>
      </div>
    </el-footer>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import radio from '@renderer/components/Test/radio.vue'

const number = ref('问题 1/10');
const router = useRouter();

const prevQuestion = () => {
  router.push('/personal');
}

const nextQuestion = () => {
  // Add your logic for next question
}

const submit = () => {
  // Add your logic for submit
}
</script>

<style scoped>
@import 'animate.css/animate.min.css';

.app-container {
  display: flex;
  flex-direction: column;
  background-color: #f0f4f8;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 0 auto;
  width: 80%;
  height: auto;
  margin-top: 20px;
  padding: 20px;
  overflow: hidden;
}

.test_header {
  display: flex;
  justify-content: space-between;
  align-items: left;
  padding: 10px;
  border-radius: 10px 10px 0 0;
  color: rgb(0, 0, 0);
  font-size: 18px;
}

.test_main {
  flex: 1;
  padding: 20px;
  background: #ffffff;
  border-radius: 0 0 10px 10px;
  margin-top: 10px;
}

.test_footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  margin-top: 20px;
}

.switch_buttons {
  display: flex;
  align-items: center;
}

.submit_button {
  display: flex;
  justify-content: center;
  align-items: center;
}

.updown {
  --button-bg-color: #409EFF;
  --button-text-color: #fff;
  --button-hover-bg-color: #66B1FF;
  --button-border-color: transparent;
  --button-focus-shadow: 0 0 2px 0 var(--button-bg-color);
  --button-active-bg-color: #3A8EE6;
  padding: 8px 16px;
  font-size: 14px;
  border-radius: 4px;
  transition: all 0.3s;
  cursor: pointer;
  margin-right: 10px;
}

.updown:hover {
  background-color: var(--button-hover-bg-color);
}

.Btn {
  width: 130px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgb(15, 15, 15);
  border: none;
  color: white;
  font-weight: 600;
  gap: 8px;
  cursor: pointer;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.103);
  position: relative;
  overflow: hidden;
  transition-duration: .3s;
}

.svgIcon {
  width: 16px;
  height: 16px;
  fill: currentColor;
}

.svgIcon path {
  fill: white;
}

.Btn::before {
  width: 130px;
  height: 130px;
  position: absolute;
  content: "";
  background-color: white;
  border-radius: 50%;
  left: -100%;
  top: 0;
  transition-duration: .3s;
  mix-blend-mode: difference;
}

.Btn:hover::before {
  transition-duration: .3s;
  transform: translate(100%, -50%);
  border-radius: 0;
}

.Btn:active {
  transform: translate(5px, 5px);
  transition-duration: .3s;
  transition: transform .1s;
}
</style>