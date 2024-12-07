<script setup>
import { Button, InputOtp, ProgressSpinner, Dialog } from 'primevue';
useSeoMeta({
    title: "Email Verification",
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
                <img src="/images/verify-email.jpg" alt="Login Page Image" class="h-screen" loading="lazy"
                    draggable="false" />
                <span class="absolute ms-10 mt-10 font-bold text-4xl select-none drop-shadow">Krist</span>
            </div>
            <div class="w-full lg:w-1/2 flex flex-col p-10">
                <NuxtLink to="/accounts/register" class="mb-5 flex items-center gap-1">
                    <Icon name="solar:alt-arrow-left-line-duotone" size="20" />
                    <span>Back</span>
                </NuxtLink>
                <h6 class="font-bold text-5xl">Enter Code</h6>
                <span class="text-gray-500 mt-5">We have share a code of your registered email address
                    robertfox@example.com</span>
                <form class="flex flex-col gap-5 mt-10 w-full">
                    <InputOtp v-model="value" size="large" class="justify-center" />
                    <Button label="Verify" size="large" class="mt-5" @click="visible = true" />
                </form>
            </div>
        </div>
        <Dialog v-model:visible="visible" modal :style="{ width: '25rem' }">
            <div class="flex flex-col gap-5 items-center">
                <Icon size="50" name="solar:check-circle-bold" class="text-green-500" />
                <span class="text-xl font-bold">Your Account has been verified</span>
                <Button label="Back to Login" class="mt-5 w-full" @click="navigateTo('/accounts/login')" />
            </div>
        </Dialog>
    </div>
</template>