<template>
  <div>
    <div class="flex gap-2">
      <div>
        <img :src="image" class="w-[6rem]" :alt="title">
      </div>
      <div class="flex flex-col justify-between w-full">
        <span class="line-clamp-1">{{ title }}</span>
        <span class="font-bold line-clamp-1">{{count}} x ${{price}}</span>
        <div class="flex justify-between 100 w-full gap-5">
          <span>size: {{size}}</span>
          <UButton icon="i-lucide-trash" size="xl" color="error" variant="soft" class="cursor-pointer" />
        </div>
      </div>
    </div>
    <USeparator class="my-3" />
  </div>
</template>

<script lang="ts" setup>

const props = defineProps([
  'title',
  'count',
  'price',
  'size',
  'image',
])


</script>

<style></style>