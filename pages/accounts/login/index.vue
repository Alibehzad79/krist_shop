<script setup>
import { InputText, Button, InputGroup, InputGroupAddon, Checkbox, ProgressSpinner } from 'primevue';
useSeoMeta({
    title: "Login"
})

const load = ref(true)

tryOnMounted(() => {
    load.value = false
})


const showPass = ref(false)

</script>

<template>
    <div>
        <div v-if="load" class="flex justify-center items-center h-screen">
            <ProgressSpinner />
        </div>
        <div class="flex justify-between gap-10 items-center" v-if="!load">
            <div class="hidden lg:flex w-1/2 relative">
                <img src="/images/login.jpg" alt="Login Page Image" class="h-screen" loading="lazy" draggable="false" />
                <span class="absolute ms-10 mt-10 font-bold text-4xl select-none drop-shadow">Krist</span>
            </div>
            <div class="w-full lg:w-1/2 flex flex-col p-10">
                <h6 class="font-bold text-5xl">Welcome 👋</h6>
                <span class="text-gray-500">Please login here</span>
                <form class="flex flex-col gap-5 mt-10 w-full">
                    <InputText id="email" placeholder="Email Address" size="large" />
                    <InputGroup>
                        <InputText id="password" :type="showPass ? 'text' : 'password'" placeholder="Password"
                            size="large" />
                        <InputGroupAddon>
                            <Button severity="primary" variant="text" @click="showPass = !showPass">
                                <Icon :name="showPass ? 'solar:eye-broken' : 'solar:eye-closed-broken'" size="20" />
                            </Button>
                        </InputGroupAddon>
                    </InputGroup>
                    <div class="flex flex-row justify-between items-center">
                        <div class="flex items-center gap-3">
                            <Checkbox id="rememberMe" value="Remember me" />
                            <label for="rememberMe">Remember me</label>
                        </div>
                        <NuxtLink to="/accounts/reset-password">Forgot Password?</NuxtLink>
                    </div>
                    <Button label="Login" size="large" class="mt-10"/>
                </form>
            </div>
        </div>
    </div>
</template>