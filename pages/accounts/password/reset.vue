<script setup>
import { Button, InputText, ProgressSpinner, Dialog } from 'primevue';
useSeoMeta({
    title: "Reset Password",
})

const load = ref(true)
const value = ref(null)
const visible = ref(false)
tryOnMounted(() => {
    load.value = false
})

</script>

<template>
    <div>
        <div v-if="load" class="flex justify-center items-center h-screen">
            <ProgressSpinner />
        </div>
        <div class="flex justify-between gap-10 items-center" v-if="!load">
            <div class="hidden lg:flex w-1/2 relative">
                <img src="/images/reset-password.jpg" alt="Login Page Image" class="h-screen" loading="lazy"
                    draggable="false" />
                <span class="absolute ms-10 mt-10 font-bold text-4xl select-none drop-shadow">Krist</span>
            </div>
            <div class="w-full lg:w-1/2 flex flex-col p-10">
                <NuxtLink to="/accounts/login" class="mb-5 flex items-center gap-1">
                    <Icon name="solar:alt-arrow-left-line-duotone" size="20" />
                    <span>Back</span>
                </NuxtLink>
                <h6 class="font-bold text-5xl">Forgot Password</h6>
                <span class="text-gray-500 mt-5">Enter your registered email address. we’ll send you a code to reset your password.</span>
                <form class="flex flex-col gap-5 mt-10 w-full">
                    <InputText v-model="value" size="large" class="justify-center" placeholder="Enter Email" />
                    <Button label="Send Code" size="large" class="mt-5" @click="visible = true" />
                </form>
            </div>
        </div>
        <Dialog v-model:visible="visible" modal :style="{ width: '25rem' }">
            <div class="flex flex-col gap-5 items-center">
                <Icon size="50" name="solar:check-circle-bold" class="text-green-500" />
                <span class="text-xl font-bold">Sent Code Successfuly.</span>
                <Button label="Confirm" class="mt-5 w-full" @click="navigateTo('/accounts/otp/confirm-reset-code')" />
            </div>
        </Dialog>
    </div>
</template>