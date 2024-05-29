<template>
    <div>
        <div class="question-section">
            <el-text class="question-text">{{ serial }} 下列哪个城市被誉为“水城”？</el-text>
        </div>
        <div class="radio-buttons">
            <label class="container" v-for="(option, index) in options" :key="index">
                <input type="radio" name="option" v-model="selectedOption">
                <div class="checkmark">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon No" viewBox="0 0 1024 1024">
                        <path
                            d="M696.32 563.2H327.68c-28.256 0-51.2-22.976-51.2-51.2 0-28.224 22.944-51.2 51.2-51.2h368.64a51.2 51.2 0 1 1 0 102.4z"
                            fill="#FCBA29" p-id="1450"></path>
                        <path
                            d="M512 1024C229.728 1024 0 794.272 0 512S229.728 0 512 0s512 229.728 512 512-229.728 512-512 512z m0-921.6C286.176 102.4 102.4 286.176 102.4 512S286.176 921.6 512 921.6 921.6 737.824 921.6 512 737.824 102.4 512 102.4z"
                            fill="#FCBA29" p-id="1451"></path>
                    </svg>
                    <p class="No name">{{ abcd[index] }}</p>
                    <svg viewBox="0 0 1024 1024" class="icon Yes" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M512 1024C229.76 1024 0 794.336 0 511.936S229.76 0 512 0s512 229.664 512 511.936S794.368 1024 512 1024z m0-921.632c-225.856 0-409.632 183.808-409.632 409.696 0 225.888 183.776 409.696 409.632 409.696s409.632-183.936 409.632-409.824S737.856 102.336 512 102.336z"
                            fill="#FCBA29" p-id="1168"></path>
                        <path
                            d="M449.568 728.224c-13.632 0-26.656-5.376-36.256-14.976L254.336 554.24a51.168 51.168 0 1 1 72.384-72.416l122.848 122.72 247.68-247.712a51.168 51.168 0 1 1 72.384 72.384l-283.936 284c-9.6 9.6-22.528 14.976-36.16 14.976z"
                            fill="#FCBA29" p-id="1169"></path>
                    </svg>
                    <p class="Yes name">{{ abcd[index] }}</p>
                </div>
                <el-text class="radio-label">{{ option }}</el-text>
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
    font-size: 20px;
    font-weight: bold;
    color: #333;
}

.radio-buttons {
    width: 100%;
}

.container {
    --UnChecked-color: hsl(70, 71%, 85%);
    --checked-color: hsl(55, 100%, 63%);
    --font-color: rgb(249, 178, 70);
    --checked-font-color: var(--font-color);
    --icon-size: 1.5em;
    --anim-time: 0.2s;
    --anim-scale: 0.1;
    --base-radius: 0.8em;
    display: flex;
    align-items: center;
    position: relative;
    cursor: pointer;
    font-size: 20px;
    user-select: none;
    fill: var(--font-color);
    color: var(--font-color);
    margin-bottom: 10px; /* Add margin between radio buttons */
    padding: 10px;
    background-color: #fff; /* Add white background */
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease, transform 0.3s ease;
}

/* Hide the default radio button */
.container input[type="radio"] {
    display: none;
}

/* Base custom radio button */
.checkmark {
    background: var(--UnChecked-color);
    border-radius: var(--base-radius);
    display: flex;
    padding: 0.5em;
    transform: scale(0.7); /* Adjust size as needed */
    transition: background-color 0.3s ease;
}

.icon {
    width: var(--icon-size);
    height: auto;
    filter: drop-shadow(0px 2px var(--base-radius) rgba(0, 0, 0, 0.25));
}

.name {
    margin: 0 0.25em;
}

.Yes {
    width: 0;
}

.name.Yes {
    display: none;
}

/* Hover and active states */
.container:hover .checkmark,
.container:hover .icon,
.container:hover .name {
    transform: scale(0.8);
}

.container:active .checkmark,
.container:active .icon,
.container:active .name {
    transform: scale(calc(1 - var(--anim-scale) / 2));
    border-radius: calc(var(--base-radius) * 2);
}

.checkmark::before {
    content: "";
    opacity: 0.5;
    transform: scale(1);
    border-radius: var(--base-radius);
    position: absolute;
    box-sizing: border-box;
    left: 0;
    top: 0;
    height: 100%;
    width: 100%;
}

.checkmark:hover:before {
    background-color: hsla(0, 0%, 50%, 0.2);
}

.container input:checked + .checkmark:before {
    animation: boon calc(var(--anim-time)) ease;
    animation-delay: calc(var(--anim-time) / 2);
}

/* When the radio button is checked */
.container input:checked + .checkmark {
    background: var(--checked-color);
    fill: var(--checked-font-color);
    color: var(--checked-font-color);
}

.container input:checked ~ .checkmark .No {
    width: 0;
}

.container input:checked ~ .checkmark .name.No {
    display: none;
}

.container input:checked ~ .checkmark .Yes {
    width: var(--icon-size);
}

.container input:checked ~ .checkmark .name.Yes {
    width: auto;
    display: unset;
}

/* Animation */
.container,
.checkmark,
.checkmark:after,
.icon,
.checkmark .name {
    transition: all var(--anim-time);
}

/* Animation keyframes */
@keyframes boon {
    80% {
        transform: scale(1.4);
    }

    99% {
        transform: scale(1.7);
        border: 2px solid var(--UnChecked-color);
    }

    to {
        transform: scale(0);
    }
}
</style>