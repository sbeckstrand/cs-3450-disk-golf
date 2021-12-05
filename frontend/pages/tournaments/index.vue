<template>
    <div>
        <Nav />
        <div>
            <b-button href="/tournaments/create" class="mt-3">
                Create Tournament
            </b-button>
        </div>
        <div v-for="tournament in tournaments" :key="tournament.id">
            <a :href="`/tournaments/${tournament.id}`">{{ tournament }}</a>
        </div>
        
    </div>
    
</template>

<script>
export default {
    async asyncData({ $axios }) {
        const tournaments = await $axios.$get('/api/tournaments/')
        return { tournaments }
    },
    methods: {
        
    }
}
</script>

<style>

</style>

