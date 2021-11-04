<template>
    <div>
        <Nav />
        <div>
            <b-button href="/tournaments/create" class="mt-3">
                Create Tournament
            </b-button>
        </div>
        <div v-for="tournament in tournaments" :key="tournament.id">
            {{ tournament }} 
            <b-button class="mt-3"
                variant="danger"
                @click="delTournament(tournament)">
                Delete
            </b-button>
            <b-button class="mt-3"
                variant="secondary"
                :href="'/tournaments/edit/' + tournament.id">
                
                Edit
            </b-button>
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
        async delTournament(tournament) {
            try {
                const tournamentIndex = this.tournaments.findIndex(t => t.id === tournament.id)
                await this.$axios.delete('/api/tournaments/' + tournament.id)
                this.tournaments.splice(tournamentIndex, 1)
            } catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    msg: "Failed to delete tournament."
                }) 
            }
        }
    }
}
</script>

<style>

</style>

