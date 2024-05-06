<script setup lang="ts">
import Test from '@renderer/Functions/Test.vue';
import Personal from '@renderer/Functions/Personal.vue';
import Mission_ini from '@renderer/Functions/Mission_ini.vue';
import Login from '@renderer/user/Login.vue';
import Register from '@renderer/user/Register.vue';
import learing from '@renderer/Functions/Learn.vue'
</script>

<template>
   <div>
        <Test>
        </Test>
        <Personal>
            </Personal>
            <Mission_ini>
                </Mission_ini>
                <Login>
                    </Login>
                    <Register>
                        </Register>

    </div>

<div>
<learing>
    </learing>
    </div>
</template>

<style>
.login-style {
    display: grid;
    place-items: center;
    margin-top: 30px;
}
</style>