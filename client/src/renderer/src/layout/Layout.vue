<script setup lang="ts">
import Test from '@renderer/Functions/Test.vue';
import Personal from '@renderer/Functions/Personal.vue';
import Mission_ini from '@renderer/Functions/Mission_ini.vue';
import Learn from '@renderer/Functions/Learn.vue';
import Login from '@renderer/user/Login.vue';
</script>

<template>
    <div>
        <Test>
        </Test>
    </div>
    <div>
        <Personal>
        </Personal>
    </div>
    <div>
        <Mission_ini>
        </Mission_ini>
    </div>
    <div>
        <Learn>
        </Learn>
    </div>
    <Login>
        </Login>

</template>

<style>
.login-style {
    display: grid;
    place-items: center;
    margin-top: 30px;
}
</style>