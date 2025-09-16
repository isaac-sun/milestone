<template>
  <button class="rate-button" @click="$emit('fetch-data')">
    View Rates
  </button>
</template>

<script>
export default {
  name: 'RateButton'
}
</script>