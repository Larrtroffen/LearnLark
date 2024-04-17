<template class="container">
    <div class="post-card">
      <el-row>
        <el-col span="8">
          <el-image src="" fit="cover" class="post-image"></el-image>
        </el-col>
        <el-col span="16">
          <div class="post-info">
            <!---<router-link class="post-title">标题</router-link>-->
            <div class="post-description">
              <el-text>简介</el-text>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
  </template>
  
  <style scoped>
  .container {
    margin-bottom: 20px;
  }
  
  .post-card {
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    overflow: hidden;
  }
  
  .post-image {
    width: 100%;
    height: 100%;
    border-top-left-radius: 8px;
    border-bottom-left-radius: 8px;
  }
  
  .post-info {
    padding: 20px;
  }
  
  .post-title {
    font-size: 20px;
    font-weight: bold;
    color: #333;
    text-decoration: none;
  }
  
  .post-description {
    margin-top: 10px;
    color: #666;
  }
  
  </style>
  