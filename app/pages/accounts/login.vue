<template>
  <div>
    <div class="flex items-center gap-10">
      <div class="hidden lg:flex w-1/2">
        <img src="/images/login.jpg" alt="Login" class="h-screen w-full">
      </div>
      <div class="w-full lg:w-1/2 flex flex-col gap-5">
        <div class="flex flex-col gap-2">
          <h1 class="text-3xl font-bold">Welcome 👋</h1>
          <span class="text-gray-500">Please login here</span>
        </div>
        <div class="flex flex-col gap-5 w-full">
          <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
            <UFormField label="Email" name="email">
              <UInput v-model="state.email" class="w-96" size="xl" />
            </UFormField>

            <UFormField label="Password" name="password">
              <UInput v-model="state.password" :type="showPassword ? 'text' : 'password'" class="w-96" size="xl"
                :ui="{ trailing: 'pe-1' }">
                <template #trailing>
                  <Icon :name="showPassword ? 'solar:eye-linear' : 'solar:eye-closed-bold'" size="30"
                    class="cursor-pointer" @click="showPassword = !showPassword" />
                </template>
              </UInput>
            </UFormField>

            <UButton label="Login" type="submit" size="xl" :loading="btnLoading"
              class="w-96 justify-center cursor-pointer" />
          </UForm>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
useSeoMeta({
  title: "Login"
})

import * as z from 'zod'
import type { FormSubmitEvent } from '#ui/types'

const schema = z.object({
  email: z.string().email('Invalid email'),
  password: z.string()
})

type Schema = z.output<typeof schema>
const state = reactive<Partial<Schema>>({
  email: undefined,
  password: undefined
})
const btnLoading = ref(false)
const toast = useToast()
async function onSubmit(event: FormSubmitEvent<Schema>) {
  btnLoading.value = true
  toast.add({ title: 'Login Successfuly', color: 'success', duration: 3000 })
  setTimeout(() => {
    navigateTo('/')
  }, 3000);
}
const showPassword = ref(false)
</script>

<style></style>