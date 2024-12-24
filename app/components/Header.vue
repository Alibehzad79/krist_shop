<template>
  <div class="sticky top-0 backdrop-blur-3xl">
    <UContainer>
      <nav class="flex justify-between items-center p-5">
        <div>
          <NuxtLink to="/">
            <h1 class="text-3xl font-bold text-black dark:text-white">Kristo</h1>
          </NuxtLink>
        </div>
        <div class="items-center justify-between gap-5 w-full hidden lg:flex">
          <UNavigationMenu :items="items" class="justify-center" />
        </div>
        <div class="items-center justify-between gap-5 hidden lg:flex">
          <UModal title="Search" v-model:open="openSearch">
            <Icon name="solar:magnifer-linear" size="30" class="cursor-pointer" @click="openSearch = true" />
            <template #body>
              <div class="flex items-center gap-2">
                <UInput class="w-full" size="xl" placeholder="Men, Women, ..." />
                <UButton label="Search" size="xl" variant="soft" class="cursor-pointer" @click="openSearch = false" />
              </div>
            </template>
          </UModal>
          <Icon name="solar:heart-linear" size="30" class="cursor-pointer" />
          <UPopover v-model:open="openCart" arrow="">
            <Icon name="solar:bag-3-linear" size="30" class="cursor-pointer" @click="openCart = true" />

            <template #content>
              <div class="w-96 p-5">
                <CartItem v-for="x in 4"
                  title="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Culpa, perferendis!"
                  image="/images/item.jpg" count="1" price="80.00" size="S" />
                <div class="flex justify-between my-5">
                  <span class="font-bold">Subtotal</span>
                  <span>$320.00</span>
                </div>
                <div class="flex flex-col w-full gap-5">
                  <UButton size="xl" class="justify-center cursor-pointer" label="View Cart" variant="outline" />
                  <UButton size="xl" class="justify-center cursor-pointer" label="Checkout" variant="solid" />
                </div>
              </div>
            </template>
          </UPopover>
          <div class="flex items-center gap-1">
            <NuxtLink to="/accounts/login">
              <UButton label="Login" size="xl" class="cursor-pointer" />
            </NuxtLink>
            <NuxtLink to="/accounts/register">
              <UButton label="Register" size="xl" variant="ghost" class="cursor-pointer" />
            </NuxtLink>
          </div>
        </div>
        <USlideover title="Menu" class="lg:hidden" close-icon="i-lucide-circle-x" :close="{
          variant: 'ghost',
          class: 'text-xl'
        }">
          <UButton icon="i-lucide-menu" color="neutral" variant="subtle" size="xl" class="lg:hidden" />

          <template #body class="lg:hidden">
            <div class="flex items-center gap-2 mb-5">
              <UInput type="search" class="w-full" size="xl" placeholder="Men, Women, ..." />
              <UButton label="search" size="xl" />
            </div>
            <UNavigationMenu orientation="vertical" :items="items" />
            <div class="mt-5">
              <div class="grid grid-cols-4 items-center">
                <NuxtLink to="/fav">
                  <Icon name="solar:heart-linear" size="30" class="cursor-pointer" />
                </NuxtLink>
                <NuxtLink to="/cart">
                  <Icon name="solar:bag-3-linear" size="30" class="cursor-pointer" />
                </NuxtLink>
                <NuxtLink to="/accounts/login">
                  <UButton label="Login" size="xl" class="cursor-pointer" />
                </NuxtLink>
                <NuxtLink to="/accounts/register">
                  <UButton label="Register" size="xl" variant="ghost" class="cursor-pointer" />
                </NuxtLink>
              </div>
            </div>
          </template>
        </USlideover>
      </nav>
    </UContainer>
  </div>
</template>

<script setup>
const items = ref([
  {
    label: "Home",
    icon: "i-lucide-home",
    to: "/",
    class: "text-md"
  },
  {
    label: 'Shop',
    icon: 'i-lucide-store',
    class: "text-md",
    children: [
      {
        label: 'Men',
        to: "/categories/men"
      },
      {
        label: 'Women',
        to: "/categories/women"
      },
      {
        label: 'Kids',
        to: "/categories/kids"
      },
      {
        label: 'Footwear',
        to: "/categories/footwear"
      },
    ]
  },
  {
    label: 'Our Story',
    icon: 'i-lucide-circle-fading-plus',
    to: '/stories',
    class: "text-md",
  },
  {
    label: 'Contact Us',
    icon: 'i-lucide-phone',
    to: '/contact',
    class: "text-md",
  },
])

const openSearch = ref(false)
const openCart = ref(false)
</script>

<style></style>