<script setup lang="ts">
import Login from '@renderer/user/Login.vue';
import Register from '@renderer/user/Register.vue';
const show_login = true
const show_register = false
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
</template>

<style>
.login-style{
    display: grid;
    place-items: center;
    margin-top: 30px;
}
</style>
  