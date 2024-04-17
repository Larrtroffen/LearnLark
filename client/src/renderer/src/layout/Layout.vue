<script setup lang="ts">
import Login from '@renderer/user/Login.vue';
import Register from '@renderer/user/Register.vue';
import Learn from '@renderer/Functions/Learn.vue';
import Mission from '@renderer/Functions/Mission.vue';
import Test from '@renderer/Functions/Test.vue';
import Personal from '@renderer/Functions/Personal.vue';
const show_login = false
const show_register = false
const show_search = false
const show_mission = false
const show_test = false
const show_person = true
</script>

<template>
    <div v-if="show_login" class="login-style">
        <Login>
        </Login>
    </div>
    <div v-if="show_register">
        <Register>
        </Register>
    </div>
    <div v-if="show_search">
        <Learn>
        </Learn>
    </div>
    <div v-if="show_mission">
        <Mission>
        </Mission>
    </div>
    <div v-if="show_test">
        <Test>
        </Test>
    </div>
    <div v-if="show_person">
        <Personal>
            </Personal>
    </div>
</template>

<style>
.login-style {
    display: grid;
    place-items: center;
    margin-top: 30px;
}
</style>