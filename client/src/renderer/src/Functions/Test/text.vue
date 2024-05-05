<template>
    <div>
      <el-text>题目</el-text>
    </div>
    <div class="inputGroup">
      <textarea required="" autocomplete="off" v-model="inputValue"></textarea>
      <label for="name">请输入答案</label>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const inputValue = ref('');
  </script>
  
  <style scoped>
  .inputGroup {
    font-family: 'Segoe UI', sans-serif;
    margin: 1em 0 1em 0;
    max-width: 250px; /* Increased maximum width */
    position: relative;
  }
  
  .inputGroup textarea {
    font-size: 100%;
    padding: 0.8em;
    outline: none;
    border: 2px solid rgb(200, 200, 200);
    background-color: transparent;
    border-radius: 20px;
    width: 100%;
    height: 150px; /* Increased height */
    resize: vertical; /* Allow vertical resizing of textarea */
  }
  
  .inputGroup label {
    font-size: 100%;
    position: absolute;
    top: 0;
    left: 0;
    padding: 0.8em;
    margin-left: 0.5em;
    pointer-events: none;
    transition: all 0.3s ease;
    color: rgb(100, 100, 100);
  }
  
  .inputGroup textarea:focus~label,
  .inputGroup textarea:valid~label {
    transform: translateY(-50%) scale(.9);
    margin: 0em;
    margin-left: 1.3em;
    padding: 0.4em;
    background-color: hsl(0, 0%, 100%);
  }
  
  .inputGroup textarea:focus {
    border-color: rgb(150, 150, 200);
  }
  </style>
  