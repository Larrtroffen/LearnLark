
<template>
  <el-form>
    <el-form-item>
      <div class="question-container">
        <el-form-item>
          <span class="question-text">Which city is known as the "City of Water"?</span>
        </el-form-item>
        <el-checkbox-group v-model="checkedOptions" class="options-container">
          <el-checkbox
            v-for="(option, index) in options"
            :key="index"
            :label="option.value"
            :class="{ 'animate-option': true, 'selected': option.value in checkedOptions }"
            @change="handleCheckboxChange"
          >
          <div class="option-content">
              <span class="option-value">{{ option.value }}</span>
              <span>{{ option.text }} </span>
1           </div>
          </el-checkbox>
        </el-checkbox-group>
      </div>
    </el-form-item>
  </el-form>
</template>

<style scoped>
.question-container {
  display: flex;
  flex-direction: column;

}

.question-text {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}
.option-value {
  font-weight: bold;
  color: #6871f1;
}
.option-content {
  display: flex;
  align-items: baseline; /* 使得文字基线对齐 */
  gap: 5px; /* 选项值和文本之间的间距 */
}
.options-container {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap; /* 允许选项换行 */
  gap: 30px 30px; /* 增加选项间的水平和垂直间距 */
}
::v-deep(.el-checkbox__label) {
  flex: 1;
  white-space: normal;
  font-size: 16px;
  word-break: break-word; 
}

::v-deep(.el-checkbox__inner) { 
  display: none;
}

::v-deep(.el-checkbox__input) {
  display: block;
  position: relative;
  top: 1px;
  width: 27px;
  height: 27px;
  border: 1px solid #c8ccd4;
  border-radius: 3px;
  transition: background 0.1s ease;
  cursor: pointer;
  display: block;

}

::v-deep(.el-checkbox__input):after {
  content: '';
  position: absolute;
  top: 2px;
  left: 8px;
  width: 7px;
  height: 14px;
  opacity: 0;
  transform: rotate(45deg) scale(0);
  border-right: 2px solid #fff;
  border-bottom: 2px solid #fff;
  transition: all 0.3s ease;
  transition-delay: 0.15s;
}

::v-deep(.is-checked .el-checkbox__input) {
  border-color: transparent;
  background: #6871f1;
  animation: jelly 0.6s ease;
}

::v-deep(.is-checked .el-checkbox__input):after {
  opacity: 1;
  transform: rotate(45deg) scale(1);
}

.cntr {
  position: relative;
}

@keyframes jelly {
  from {
    transform: scale(1, 1);
  }
  30% {
    transform: scale(1.25, 0.75);
  }
  40% {
    transform: scale(0.75, 1.25);
  }
  50% {
    transform: scale(1.15, 0.85);
  }
  65% {
    transform: scale(0.95, 1.05);
  }
  75% {
    transform: scale(1.05, 0.95);
  }
  to {
    transform: scale(1, 1);
  }
}

.hidden-xs-up {
  display: none!important;
}
</style>

<script setup lang="ts">
import { ref } from 'vue';

const checkedOptions = ref([]);
const options = [
  { value: 'A', text: '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111' },
  { value: 'B', text: '' },
  { value: 'C', text: '' },
];

const handleCheckboxChange = (value) => {
  // 可以在这里处理选项变化的逻辑
};
</script>
