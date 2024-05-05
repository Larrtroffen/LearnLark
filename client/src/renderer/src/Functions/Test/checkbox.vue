
<template>
  <el-form>
    <el-form-item>
      <h3>Question Title Here</h3>
      <el-checkbox-group v-model="checkedOptions">
        <el-checkbox
          v-for="(option, index) in options"
          :key="index"
          :label="option.value"
          :class="{ 'animate-option': true, 'selected': option.value in checkedOptions }"
          @change="handleCheckboxChange"
        >
          {{ option.text }}
        </el-checkbox>
      </el-checkbox-group>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref } from 'vue';

const checkedOptions = ref([]);
const options = [
  { value: 'option1', text: 'Option 1' },
  { value: 'option2', text: 'Option 2' },
  { value: 'option3', text: 'Option 3' },
];

const handleCheckboxChange = (value) => {
  // 可以在这里处理选项变化的逻辑
};
</script>

<style scoped>
::v-deep(.el-checkbox__inner) { /* 修改选择器以针对复选框内部元素 */
  /* 隐藏Element Plus默认的复选框图标 */
  display: none;
}
::v-deep(.el-checkbox__input) {
  position: relative;
  top: 1px;
  width: 27px;
  height: 27px;
  border: 1px solid #c8ccd4;
  border-radius: 3px;
  vertical-align: middle;
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

/* 由于Element Plus组件结构，直接应用.checked可能不适用，
   需要查看实际DOM结构以找到正确的方式标记选中状态 */
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