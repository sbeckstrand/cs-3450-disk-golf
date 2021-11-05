<template>
  <div>
      <Nav />
      {{ tournament }}
  </div>
</template>

<script>
export default {
    async asyncData({ params, $axios }) {
        const tournament = await $axios.$get(`/api/tournaments/${params.id}`)
        return { tournament }
    },
}
</script>

<style>

</style>