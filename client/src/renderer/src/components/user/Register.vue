<template>
  <div id="form-ui" class="registration-form">
    <el-form ref="form" :model="form" :rules="rules" label-width="0" class="demo-ruleForm">
      <h2 class="welcome-line-1">LearnLark</h2>
      <p class="welcome-line-2">开始你的学习之旅！</p>
      <div class="input-form">
      <el-form-item prop="email">
        <el-input v-model="form.email" placeholder="邮箱地址"></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input v-model="form.password" type="password" placeholder="密码"></el-input>
      </el-form-item>
      <el-form-item prop="confirmPassword">
        <el-input v-model="form.confirmPassword" type="password" placeholder="确认密码"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" id="submit-button" native-type="submit" :loading="loading"
          @click.prevent="onSubmit">注册</el-button>
      </el-form-item>
      </div>
      <div class="forgot-pass">
        <span>已有账号？<router-link to="/login">点击登录</router-link></span>
      </div>
    </el-form>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { ElMessage } from 'element-plus';

const form = reactive({
  email: '',
  password: '',
  confirmPassword: ''
});

const rules = reactive({
  email: [{ required: true, message: '请输入邮箱地址', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
  confirmPassword: [{ required: true, message: '请确认密码', trigger: 'blur' }]
});

const loading = ref(false);

const onSubmit = () => {
  if (formRef.value.validate()) {
    console.log('submit!');
    loading.value = true;
    setTimeout(() => {
      loading.value = false;
      ElMessage.success('表单提交成功！');
    }, 2000);
  } else {
    console.log('error submit!!');
  }
};

const formRef = ref(null);

onMounted(() => {
  // 初始化逻辑
});
</script>

<style scoped>
.registration-form {
  width: 100%;
  max-width: 300px;
  margin: 0 auto;
  padding: 25px;
  background-color: #ffffffcb;
  box-shadow: 0 15px 60px rgba(85, 172, 238, 0.9);
  border-radius: 20px;
}

.welcome-line-1 {
  color: #55ACEE;
  font-weight: 600;
  font-size: 40px;
  text-align: center;
  margin-bottom: 17px;
}

.welcome-line-2 {
  color: #55ACEE;
  font-size: 18px;
  text-align: center;
}

.el-form-item {
  display: flex;
  align-items: center;
  /* 水平居中 */
  flex-direction: column;
  justify-content: center;
}


.el-input {
  width: 250px;

}

.el-input__inner:focus {
  border-color: #55ACEE !important;
}

#submit-button {
  width: 250px;
  font-weight: 600;
  font-size: 14px;
  border-radius: 8px;
  cursor: pointer;
  transition: all ease-in-out .3s;
  margin-top: 40px;
  text-align: center;
}

#submit-button:hover {
  background-color: #55ACEE;
  color: #161616;
}

.forgot-pass {
  text-align: center;
}
</style>
