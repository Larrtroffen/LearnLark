<template>
    <div>
        <div class="question-section">
            <el-text class="question-text">{{ serial }} 下列哪个城市被誉为“水城”？</el-text>
        </div>
        <div class="options-container">
            <div class="check_container" v-for="(option, index) in options" :key="index">
                <input :id="'radio-' + index" class="hidden" type="radio" :name="'option'" :value="option" v-model="selectedOption">
                <label class="checkbox" :for="'radio-' + index"></label>
                <el-text class="radio-label">{{ abcd[index] }}. {{ option }}</el-text>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
const serial = 1;
const options = ['威尼斯', '阿姆斯特丹', '布鲁日', '苏州'];
const selectedOption = ref<string>('');
const abcd = ['A', 'B', 'C', 'D'];
</script>

<style scoped>
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

