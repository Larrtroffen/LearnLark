
<template>
  <div id="form-ui">
    <el-form 
      @submit.prevent="handleSubmit" 
      id="custom-form" 
      :model="form"
      status-icon
      label-position="top"
    >
      <div id="form-body">
        <div id="welcome-lines">
          <div id="welcome-line-1">LearnLark</div>
          <div id="welcome-line-2">开始你的学习之旅！</div>
        </div>
        <el-form-item prop="email">
          <el-input 
            v-model="form.email" 
            placeholder="邮箱地址" 
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input 
            v-model="form.password" 
            placeholder="密码" 
            show-password
            clearable
          ></el-input>
        </el-form-item>
        <el-button id="submit-button" type="primary" native-type="submit">登陆</el-button>
        <div id="forgot-pass">
          <a href="#">忘记密码?</a>
        </div>
      </div>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue';
import { ElForm, ElInput, ElButton } from 'element-plus';

const form = reactive({
  email: '',
  password: ''
});

const handleSubmit = (event: Event) => {
  event.preventDefault();
  // 登录逻辑处理
};
</script>

<style scoped>
#form-ui {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

#custom-form {
  width: 300px;
  height: 400px;
  background-color: #ffffffcb;
  box-shadow: 0px 15px 60px #55ACEE;
  border-radius: 20px;
  padding: 25px;
}

#welcome-lines {
  text-align: center;
  line-height: 1;
}

#welcome-line-1 {
  color: #55ACEE;
  font-weight: 600;
  font-size: 40px;
}

#welcome-line-2 {
  color: #55ACEE;
  font-size: 18px;
  margin-top: 17px;
}

.el-form-item {
  margin-top: 40px;
}

.el-input__inner {
  color: #55ACEE;
  font-size: 13.4px;
  border-color: #e3e3e3;
  border-radius: 8px;
}

.el-input__inner:focus {
  border-color: #55ACEE;
}

#submit-button {
  width: 100%;
  font-weight: 600;
  font-size: 14px;
  border-radius: 8px;
  cursor: pointer;
  transition: all ease-in-out .3s;
  margin-top: 40px;
}

#submit-button:hover {
  background-color: #55ACEE;
  color: #161616;
}

#forgot-pass {
  text-align: center;
  margin-top: 10px;
}

#forgot-pass a {
  color: #868686;
  font-size: 12px;
  text-decoration: none;
}
</style>
