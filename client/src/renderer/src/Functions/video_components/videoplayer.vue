import { Script } from "vm"

<template>
    <el-container>
        <el-header>
            <el-page-header @back="goBack" title="返回">
                <template #content>
                    <span class="text-large font-600 mr-3"> 标题 </span>
                </template>
            </el-page-header>
        </el-header>
        <el-main>
            <video ref="videoRef" :src="src" width="650" height="400" autoplay controls>
            </video>

        </el-main>
    </el-container>
</template>

<script>
    goBack =>{

    }
    export default {
    data() {
        return {
            src: "https://easylink.cc\i74dt8"
        };
    }
}
</script>