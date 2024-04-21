<template>
    <el-menu mode="horizontal">
        <el-menu-item>主页
        </el-menu-item>
        <el-menu-item>英语
        </el-menu-item>
        <el-menu-item>数学
        </el-menu-item>
        <el-menu-item>语文
        </el-menu-item>
        <el-menu-item>其它
        </el-menu-item>
    </el-menu>
    <div>
        <math_result>
            </math_result>
        </div>
        <div>
            <videoplayer>
                </videoplayer>
            </div>
    <el-pagination :total="100" />
</template>

<style>

</style>

<script setup lang="ts">

import math_result from '@renderer/Functions/Learn/math_result.vue';
import videoplayer from './video_components/videoplayer.vue';
</script>