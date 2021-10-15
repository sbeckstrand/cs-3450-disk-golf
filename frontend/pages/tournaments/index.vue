<template>
    <div>
        <Nav />
        <div v-for="tournament in tournaments" :key="tournament.id">
        {{ tournament }}
        </div>
    </div>
    
</template>

<script>
export default {
    async asyncData({ $axios, $config }) {
        const tournaments = await $axios.$get('/api/tournaments/')
        return { tournaments }
    }
}
</script>

<style>

</style>