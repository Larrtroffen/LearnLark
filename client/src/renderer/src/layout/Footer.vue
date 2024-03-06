<script setup lang="ts">
</script>
<template>
  <el-footer>
    <div class="footer">
      <div class="footer-item">
        <h3>产品</h3>
      </div>
      <div class="footer-item">
        <h3>关于</h3>
      </div>
      <div class="footer-item">
        <h3>联系</h3>
      </div>
    </div>
  </el-footer>
</template>

<style>
  .footer {
    display: flex;
    justify-content: space-around;
    padding: 20px 0;
  }
  .footer-item {
    display: flex;
    flex-direction: column;
  }
  .footer-item h3 {
    font-size: 16px;
    margin-bottom: 10px;
  }
  .footer-item ul {
    list-style: none;
    padding: 0;
  }
  .footer-item ul li {
    margin-bottom: 10px;
  }
</style>