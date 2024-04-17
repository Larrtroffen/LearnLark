<template>
    <el-container>
        <el-aside>
            <div>
                <el-button icon="">未完成任务
                </el-button>
            </div>
            <div>
                <el-button>主线任务
                </el-button>
            </div>
            <div>
                <el-button>支线任务
                </el-button>
            </div>
            <div>
                <el-button>宗门任务
                </el-button>
            </div>
        </el-aside>
        <el-main>
            <el-container>
                <el-aside>
                    <div>
                        <el-collapse> 数学
                            <el-collapse-item>
                                <div>计算1+1</div>
                                <div>计算2—2</div>
                            </el-collapse-item>
                        </el-collapse>
                    </div>

                    <div>
                        <el-collapse> 英语
                            <el-collapse-item>
                                <div>abondon</div>
                                <div>abonst</div>
                            </el-collapse-item>
                        </el-collapse>
                    </div>
                    </el-aside>
                    <el-main>
                        <div>
                        <h2>标题</h2>
                        <h3>副标题</h3>
                    </div>
                    <el-divider>
                    </el-divider>
                    <div>
                        <el-text>
                            任务具体内容
                        </el-text>
                    </div>
                    <div>
                        <el-text>任务奖励
                        </el-text>
                        <el-icon>
                        </el-icon>
                    </div>
                    <div>
                        <el-button>跳转学习
                        </el-button>
                    </div>
                        </el-main>
                </el-container>


        </el-main>
    </el-container>
</template>
 
