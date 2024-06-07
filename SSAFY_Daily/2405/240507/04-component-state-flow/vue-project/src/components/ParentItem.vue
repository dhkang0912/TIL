<template>
  <div>
    <p>{{ myProp }} </p>
  </div>
</template>

<script setup>
defineProps({
  myProp: Object,
})
</script>

<style scoped>

</style>