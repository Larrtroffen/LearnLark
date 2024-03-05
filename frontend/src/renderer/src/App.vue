<script setup lang="ts">
import Topbar from './components/Topbar.vue'

const ipcHandle = () => window.electron.ipcRenderer.send('ping')
</script>

<template>
  <Topbar />
  
</template>
