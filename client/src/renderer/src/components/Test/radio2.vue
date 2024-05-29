<template>
    <div>
        <div class="question-section">
            <el-text class="question-text">{{ serial }} 下列哪个城市被誉为“水城”？</el-text>
        </div>
        <div class="radio-buttons">
            <label class="radio-button" v-for="(option, index) in options" :key="index">
                <input type="radio" class="ui-checkbox" :value="option" v-model="selectedOption">
                <el-text class="radio-label">{{ abcd[index] }}. {{ option }}</el-text>
            </label>
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
    font-size: 22px; /* Increased font size */
    font-weight: bold;
    color: #333; /* White color for better contrast */
}

/* Radio buttons container */
.radio-buttons {
    width: 100%;
}

.radio-button {
    display: flex;
    align-items: center;
    padding: 10px;
    margin-bottom: 10px; /* Add space between radio buttons */
    background-color: #fff; /* White background for options */
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.radio-button:hover {
    background-color: #e0e7ff; /* Light blue hover effect */
    transform: translateY(-2px); /* Slight lift effect on hover */
}

.radio-label {
    font-size: 18px; /* Adjusted font size */
    color: #333; /* Dark color for better readability */
}

/* Checkbox settings */
.ui-checkbox {
    --primary-color: #1677ff;
    --secondary-color: #fff;
    --primary-hover-color: #4096ff;
    /* checkbox */
    --checkbox-diameter: 20px;
    --checkbox-border-radius: 5px;
    --checkbox-border-color: #d9d9d9;
    --checkbox-border-width: 1px;
    --checkbox-border-style: solid;
    /* checkmark */
    --checkmark-size: 1.2;
    flex-shrink: 0;
}

.ui-checkbox,
.ui-checkbox *,
.ui-checkbox *::before,
.ui-checkbox *::after {
    box-sizing: border-box;
}

.ui-checkbox {
    appearance: none;
    width: var(--checkbox-diameter);
    height: var(--checkbox-diameter);
    border-radius: var(--checkbox-border-radius);
    background: var(--secondary-color);
    border: var(--checkbox-border-width) var(--checkbox-border-style) var(--checkbox-border-color);
    transition: all 0.3s;
    cursor: pointer;
    position: relative;
    margin-right: 10px;
}

.ui-checkbox::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    box-shadow: 0 0 0 calc(var(--checkbox-diameter) / 2.5) var(--primary-color);
    border-radius: inherit;
    opacity: 0;
    transition: all 0.5s cubic-bezier(0.12, 0.4, 0.29, 1.46);
}

.ui-checkbox::before {
    top: 40%;
    left: 50%;
    content: "";
    position: absolute;
    width: 4px;
    height: 7px;
    border-right: 2px solid var(--secondary-color);
    border-bottom: 2px solid var(--secondary-color);
    transform: translate(-50%, -50%) rotate(45deg) scale(0);
    opacity: 0;
    transition: all 0.1s cubic-bezier(0.71, -0.46, 0.88, 0.6), opacity 0.1s;
}

/* Checkbox actions */
.ui-checkbox:hover {
    border-color: var(--primary-color);
}

.ui-checkbox:checked {
    background: var(--primary-color);
    border-color: transparent;
}

.ui-checkbox:checked::before {
    opacity: 1;
    transform: translate(-50%, -50%) rotate(45deg) scale(var(--checkmark-size));
    transition: all 0.2s cubic-bezier(0.12, 0.4, 0.29, 1.46) 0.1s;
}

.ui-checkbox:active:not(:checked)::after {
    transition: none;
    box-shadow: none;
    opacity: 1;
}
</style>