<template>
  <div class="wrapper">
    <div class="content">
      <div class="banner">
        <h2>制定您的学习计划</h2>
        <p>让我们一起迈向知识的海洋！</p>
      </div>
      <el-form class="form-container">
        <el-form-item label="学习天数">
          <i class="el-icon-date"></i>
          <el-input type="number" v-model="studyDays" placeholder="天数总计" disabled />
          <el-date-picker class="custom-datepicker" v-model="studyDateRange" type="daterange" start-placeholder="开始日期"
            end-placeholder="结束日期" @change="calculateStudyDays" />
        </el-form-item>
        <el-form-item label="任务名称">
          <el-input v-model="taskName" placeholder="输入任务名称" />
        </el-form-item>
        <el-form-item label="题目类型">
          <el-select v-model="selectedQuestionType" placeholder="请选择题目类型">
            <el-option
              v-for="type in questionTypes"
              :key="type.value"
              :label="type.label"
              :value="type.value">

            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="saveTask">保存任务</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="sidebar sidebar-right"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useStore } from 'vuex';

interface DateRange {
  start: Date;
  end: Date;
}

const store = useStore();
const studyDays = ref<number | null>(null);
const studyDateRange = ref<DateRange | null>(null);
const taskName = ref('');
const selectedQuestionType = ref('');
const questionTypes = ref<Array<{ label: string, value: string }>>([]);

const calculateStudyDays = () => {
  if (studyDateRange.value && studyDateRange.value.length === 2) {
    const [start, end] = studyDateRange.value;
    const startDate = new Date(start);
    const endDate = new Date(end);
    const differenceInTime = endDate.getTime() - startDate.getTime();
    const differenceInDays = differenceInTime / (1000 * 3600 * 24);
    studyDays.value = differenceInDays + 1; // Include the start day
  } else {
    studyDays.value = null;
  }
};

const fetchQuestionTypes = async () => {
  try {
    const response = await axios.get('/localhost/api/question_type');
    if (response.data) {
      questionTypes.value = response.data.map((type: { name: string, id: string }) => ({
        label: type.name,
        value: type.id
      }));
    }
  } catch (error) {
    console.error('Error fetching question types:', error);
  }
};

const saveTask = async () => {
  const payload = {
    days: studyDays.value,
    startDate: studyDateRange.value ? studyDateRange.value[0] : null,
    taskName: taskName.value,
    questionType: selectedQuestionType.value,
    userEmail: store.getters.userEmail // 包含用户邮箱
  };

  try {
    await axios.post('/localhost/api/mission_save', payload);
    alert('保存成功');
  } catch (error) {
    alert('保存失败');
  }
};

onMounted(fetchQuestionTypes);
</script>

<style scoped>
.wrapper {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  min-height: 100vh;
  background: linear-gradient(to right, #f0f4f8, #d9e4f5);
}

.sidebar {
  width: 15%;
  background-color: #f2f2f2;
}

.content {
  width: 70%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  border-radius: 10px;
}

.banner {
  background: linear-gradient(to bottom, #98def3, #1ccef2);
  color: white;
  padding: 20px;
  text-align: center;
  border-radius: 10px 10px 0 0;
  position: relative;
  z-index: 1;
  width: 100%;
  margin-bottom: 0; /* Remove bottom margin */
  margin-top: 0%;
}

.form-container {
  width: 100%;
  background-color: rgba(255, 255, 255, 0.9);
  padding: 0 30px 30px; /* Remove top padding */
  background-image: url('../pics/tem.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-blend-mode: multiply;
  border-radius: 0 0 10px 10px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  position: relative;
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

.el-form {
  width: 80%;
  margin: auto;
}

.el-form-item {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.el-form-item__label {
  width: 100px;
  color: #606266;
  font-weight: 500;
}

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

.custom-datepicker {
  margin-top: 10px;
}

.el-button {
  width: 100px;
  margin: auto;
  color: #fff;
}

@media (max-width: 768px) {
  .content {
    width: 90%;
  }

  .el-form {
    width: 100%;
  }

  .el-form-item__label {
    width: 80px;
  }
}

@media (max-width: 600px) {
  .wrapper {
    flex-direction: column;
  }

  .sidebar {
    display: none;
  }

  .content {
    width: 100%;
  }

  .el-form {
    width: 100%;
  }
}
</style>