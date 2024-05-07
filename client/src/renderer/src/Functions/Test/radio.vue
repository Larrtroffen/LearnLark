<template>
    <div>
        <div class="question-section">
            <el-text class="question-text">下列哪个城市被誉为“水城”？</el-text>
        </div>
        <div class="radio-buttons">
            <label class="radio-button">
                <input type="radio" name="option" value="option1">
                <div class="radio-circle"></div>
                <el-text class="radio-label">A. 威尼斯</el-text>
            </label>
            <label class="radio-button">
                <input type="radio" name="option" value="option2">
                <div class="radio-circle"></div>
                <el-text class="radio-label">B. 巴黎</el-text>
            </label>
            <label class="radio-button">
                <input type="radio" name="option" value="option3">
                <div class="radio-circle"></div>
                <el-text class="radio-label">C. 纽约</el-text>
            </label>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

// Define a ref for selectedOption
const selectedOption = ref<string>('');
</script>

<style scoped>
.question-section {
    margin-bottom: 20px;
}

.question-text {
    font-size: 20px;
    font-weight: bold;
}

.radio-label {
    font-size: 16px;
    margin-left: 10px; /* 为选项字母和内容之间增加一些空间 */
}


.radio-buttons {
    display: flex;
    gap: 15px;
    flex-direction: column;
    color: white;
}

.radio-button {
    display: flex;
    align-items: center;
    align-items: start;
    margin-bottom: 10px;
    cursor: pointer;
}

.radio-button input[type="radio"] {
    display: none;
}

.radio-circle {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    border: 2px solid #aaa;
    position: relative;
    margin-right: 10px;
}

.radio-circle::before {
    content: "";
    display: block;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: #ddd;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0);
    transition: all 0.2s ease-in-out;
}

.radio-button input[type="radio"]:checked+.radio-circle::before {
    transform: translate(-50%, -50%) scale(1);
}

.radio-button:nth-of-type(1) input[type="radio"]:checked+.radio-circle::before {
    background-color: #ff6600;
}

.radio-button:nth-of-type(2) input[type="radio"]:checked+.radio-circle::before {
    background-color: #299bd8;
}

.radio-button:nth-of-type(3) input[type="radio"]:checked+.radio-circle::before {
    background-color: #26be00;
}

.radio-label {
    font-size: 16px;
    font-weight: bold;
}

.radio-button:hover .radio-circle {
    border-color: #555;
}

.radio-button:hover input[type="radio"]:checked+.radio-circle::before {
    background-color: #555;
}

.content_text {
    font-size: 16px;
}
</style>