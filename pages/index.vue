<script setup>
import { Button, InputText } from 'primevue';

function toggleDarkMode() {
    document.documentElement.classList.toggle('my-app-dark');
}

</script>

<template>
    <div>
        <h1>Index Page</h1>
        <Button label="change theme" @click="toggleDarkMode" />
        <NuxtLink to="/accounts/login">Login</NuxtLink>|
        <NuxtLink to="/accounts/register">register</NuxtLink>
    </div>
</template>
<style scoped></style>