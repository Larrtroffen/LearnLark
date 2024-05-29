<template>
  <div class="top-bar">
    <el-button class="link-btn" @="toLearn">
      <div>学习</div>
    </el-button>
    <div class="sep1"></div>
    <el-button class="link-btn" @="toTest">
      <div>测试</div>
    </el-button>
    <div class="sep"></div>
    <img class="logo" src="..\pics\logo1.png" alt="Logo" />
    <div class="sep"></div>
    <el-button class="link-btn" @="toTask">
      <div>任务</div>
    </el-button>
    <div class="sep1" id="login"></div>
    <el-button class="link-btn" id="login" @="personal">
      <div>我的</div>
    </el-button>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

const toLearn = () => {

}

const toTest = () => {

}

const toTask = () => {

}

const personal = () => {

}
</script>


<style scoped>
.top-bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
}

.logo {
  width: 100px;
  height: auto;
}

.sep {
  width: 20px;
}

.sep1 {
  width: 40px;
}

.link-btn {
  color: #000;
  background-color: #fff;
  border: none;
  border-bottom: 2px solid #72b0ed;
  font-size: 18px;
  padding: 10px 20px;
  cursor: pointer;
}

.link-btn:hover {
  color: #000;
  background-color: #fff;

  border-bottom: 2px solid #72b0ed;
  border-top: 2px solid #72b0ed;
  font-size: 18px;
  padding: 10px 20px;
  cursor: pointer;
}
</style>
