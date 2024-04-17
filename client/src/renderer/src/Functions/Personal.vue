<template>
    <div>
        <div>
            <div>
                <img />
            </div>
            <div>
                <div>
                    <div>
                        <span></span>
                    </div>
                    <div>
                        <img/>
                        <span>姓名</span>
                    </div>
                    <div>
                        <span></span>
                    </div>
                    <div>
                        <el-button>编辑</el-button>
                        <el-button></el-button>
                    </div>
                </div>
            </div>
        </div>
        <div>
            <div>
                <el-card>
                    <div>
                        <span>个人中心</span>
                    </div>
                    <el-menu>
                        <el-menu-item>
                            <videoitem></videoitem>
                            <i></i>
                            <span>已学习</span>
                        </el-menu-item>
                        <el-menu-item>
                            <i></i>
                            <span>未完成</span>
                        </el-menu-item>
                        <el-menu-item>
                            <i></i>
                            <span>收藏</span>
                        </el-menu-item>
                    </el-menu>
                </el-card>
            </div>
            <div>
            </div>
        </div>
        <el-dialog></el-dialog>
    </div>


    <div>
        <setting>
            </setting>
        </div>
</template>

<script setup lang="ts">
import videoitem from './video_components/videoitem.vue';   
import setting from '@renderer/user/setting.vue';
</script>