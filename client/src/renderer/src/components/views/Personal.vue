<template>
    <div class="container">
      <div class="profile-section">
        <div class="avatar">
          <img src="../pics/tem.jpg" alt="Avatar" />
        </div>
        <div class="profile-info">
          <div class="name-section">
            <span>个人信息</span>
            <el-button type="text" icon="el-icon-edit" @click="editProfile">编辑</el-button>
          </div>
          <div class="details">
            <div class="detail-row">
              <div class="detail-icon">
                <img src="../pics/cat2.png" alt="Icon" />
              </div>
              <div class="detail-text">
                <span v-if="!editing">{{ name }}</span>
                <el-input v-else v-model="name" placeholder="输入姓名"></el-input>
              </div>
            </div>
            <div class="detail-row">
              <div class="detail-icon">
                <img src="../pics/dian.png" alt="Icon" />
              </div>
              <div class="detail-text">
                <span v-if="!editing">{{ birthday }}</span>
                <el-date-picker v-else v-model="birthday" placeholder="选择生日"></el-date-picker>
              </div>
            </div>
            <el-button v-if="editing" type="primary" @click="saveProfile">保存</el-button>
          </div>
        </div>
        <div class="cat">
          <Vue3Lottie width="200px" height="200px" :animation-data="cat_json" />
        </div>
      </div>
      <div class="history">
        <div slot="header">
          <span>个人中心</span>
        </div>
        <div class="body">
          <el-collapse class="menu">
            <el-collapse-item class="menu-item" title="未完成">
              <p v-for="record in jilu" :key="record" class="infinite-list-item">{{ record }}</p>
            </el-collapse-item>
            <el-collapse-item class="menu-item" title="已完成">
              <p v-for="record in jilu" :key="record" class="infinite-list-item">{{ record }}</p>
            </el-collapse-item>
          </el-collapse>
        </div>
        <el-dialog></el-dialog>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import Vue3Lottie from 'vue3-lottie';
  import cat_json from '@renderer/components/pics/cat2.json';
  
  const jilu = ["学习了一次", "学习了两次", "学习了三次", "学习了四次", "学习了一次", "学习了两次", "学习了三次", "学习了四次"];
  
  const name = ref('张三');
  const birthday = ref('');
  const editing = ref(false);
  
  const editProfile = () => {
    editing.value = true;
  };
  
  const saveProfile = () => {
    editing.value = false;
    // Save the profile information here
  };
  </script>
  
  <style scoped>
  :root {
    --text-color: #333; /* 主文字颜色 */
    --bg-color: #f9f9f9; /* 背景颜色 */
    --border-color: #dddddd; /* 边框颜色 */
    --primary-color: #5b9bd5; /* 主题色 */
    --shadow-color: rgba(0, 0, 0, 0.1); /* 阴影颜色 */
  }
  
  .container {
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 20px;
    background-color: var(--bg-color);
  }
  
  .profile-section {
    display: flex;
    gap: 30px;
    align-items: center; /* 对齐头像和个人信息 */
  }
  
  .avatar {
    width: 120px;
    height: 120px;
    border: 2px solid var(--border-color);
    overflow: hidden; /* 隐藏图片外的部分 */
  }
  
  .avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover; /* 确保图片覆盖整个区域 */
  }
  
  .profile-info {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  
  .name-section {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 22px;
    font-weight: bold;
    color: var(--text-color);
  }
  
  .details {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .detail-row {
    display: flex;
    align-items: center;
    gap: 10px; /* 增加图标和文字之间的间距 */
  }
  
  .detail-icon {
    width: 20px;
    height: 20px;
  }
  
  .detail-icon img {
    width: 100%;
    height: 100%;
  }
  
  .cat {
    margin-left: auto; /* 将动画放到右边 */
    top: 10%;
    filter: drop-shadow(0 0 10px var(--shadow-color));
  }
  
  .history {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 3px 6px var(--shadow-color);
    overflow: hidden; /* 改善阴影效果 */
  }
  
  .history .body {
    display: flex;
    flex-direction: column;
    padding: 20px;
  }
  
  .menu {
    border-top: 1px solid var(--border-color);
  }
  
  .menu-item {
    transition: max-height 0.3s ease; /* 过渡效果 */
  }
  
  .menu-item.is-active {
    max-height: 200px;
    overflow-y: auto;
    transition: max-height 0.3s ease; /* 过渡效果 */
  }
  
  .el-collapse-item__title {
    font-weight: bold; /* 标题文字 */
    color: var(--primary-color); /* 标题颜色 */
  }
  </style>