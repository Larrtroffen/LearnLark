<template>
    <div class="container">
        <div class="profile-section">
            <div class="avatar">
                <img src="..\pics\tem.jpg" alt="Avatar" />
            </div>
            <div class="profile-info">
                <div class="name-section">
                    <span>个人信息</span>
                </div>
                <div class="details">
                    <div class="detail-row">
                        <div class="detail-icon">
                            <img src="..\pics\tem.jpg" alt="Icon" />
                        </div>
                        <div class="detail-text">
                            <span>姓名</span>
                        </div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-icon">
                            <img src="..\pics\tem.jpg" alt="Icon" />
                        </div>
                        <div class="detail-text">
                            <span>其他信息</span>
                        </div>
                    </div>
                </div>
                <div class="action-buttons">
                    <el-button type="primary">编辑</el-button>
                    <el-button type="danger">删除</el-button>
                </div>
            </div>
        </div>
        <div class="card-section">
            <el-card class="menu-card">
                <div slot="header">
                    <span>个人中心</span>
                </div>
                <el-menu class="menu-list">
                    <el-menu-item class="menu-item">
                        <i class="menu-icon"></i>
                        <span>已学习</span>
                    </el-menu-item>
                    <el-menu-item class="menu-item">
                        <i class="menu-icon"></i>
                        <span>未完成</span>
                    </el-menu-item>
                    <el-menu-item class="menu-item">
                        <i class="menu-icon"></i>
                        <span>收藏</span>
                    </el-menu-item>
                </el-menu>
            </el-card>
        </div>
        <el-dialog></el-dialog>
    </div>

</template>

<script setup lang="ts">
import videoitem from './video_components/videoitem.vue';
</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.profile-section {
    display: flex;
    gap: 20px;
}

.avatar {
    width: 100px;
    height: 100px;
}

.avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
}

.profile-info {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.name-section {
    font-size: 20px;
    font-weight: bold;
}

.details {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.detail-row {
    display: flex;
    align-items: center;
}

.detail-icon {
    width: 20px;
    height: 20px;
}

.detail-icon img {
    width: 100%;
    height: 100%;
}

.action-buttons {
    display: flex;
    gap: 10px;
}

.card-section {
  width: 100%;
}

.menu-card {
  width: 100%;
}

.menu-list {
  width: 100%;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 5px;
}

.menu-icon {
  width: 20px;
  height: 20px;
}

</style>