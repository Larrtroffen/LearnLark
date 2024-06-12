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
          <el-date-picker 
            class="custom-datepicker" 
            v-model="studyDateRange" 
            type="daterange" 
            start-placeholder="开始日期"
            end-placeholder="结束日期" 
            @change="calculateStudyDays" 
          />
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
              :value="type.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="saveTask">保存任务</el-button>
        </el-form-item>
      </el-form>
    </div>
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
    const response = await axios.get('http://127.0.0.1:8000/api/question_type');
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
    await axios.post('http://127.0.0.1:8000/api/mission_save', payload);
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
  background: linear-gradient(to right, #f0f4f8, #d9e4f5);
}


.content {
  width: 100%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

.banner {
  width: 100%;
  background: linear-gradient(to bottom, #98def3, #1ccef2);
  color: white;
  padding: 20px;
  text-align: center;
  border-radius: 10px 10px 0 0;
  margin-bottom: 20px;
}

.form-container {
  width: 100%;
  background-color: rgba(255, 255, 255, 0.9);
  padding: 30px;
  border-radius: 0 0 10px 10px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  background: linear-gradient(to top, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.6)),
              url('../pics/bg.jpg') no-repeat center center;
  background-size: cover;
  position: relative;
  backdrop-filter: blur(5px); /* 添加虚化效果 */
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
  margin: 0 auto;
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

.custom-datepicker {
  :not(:first-child) {
    margin-top: 10px;
  }
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