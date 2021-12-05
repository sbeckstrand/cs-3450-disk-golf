<template>
    <div>
        <Nav />
        <b-container>
            <b-row>
                <b-col>
                    <b-button href="/tournaments/create" class="mt-5" variant="success">
                        Create Tournament
                    </b-button>
                </b-col>
            </b-row>
            <b-row>
                <b-col>
                    <h3 class="mt-5">Active Tournaments</h3>
                    <b-list-group>
                        <div v-for="tournament in tournaments" :key="tournament.id">
                            <b-list-group-item v-if="tournament.active == true">
                                <p><b>Name:</b> {{ tournament.name }}</p>
                                <p><b>Description:</b> {{ tournament.description }}</p>
                                <p><b>Holes:</b> {{ tournament.holes }}</p>
                                <a :href="`/tournaments/${tournament.id}`"><b-button variant="primary">Details</b-button></a>
                            </b-list-group-item>
                        </div>
                    </b-list-group>
                </b-col>
            </b-row>
            <b-row>
                <b-col>
                    <h3 class="mt-5">Concluded Tournaments</h3>
                    <b-list-group>
                        <div v-for="tournament in tournaments" :key="tournament.id">
                            <b-list-group-item v-if="tournament.active == false">
                                <p><b>Name:</b> {{ tournament.name }}</p>
                                <p><b>Description:</b> {{ tournament.description }}</p>
                                <p><b>Holes:</b> {{ tournament.holes }}</p>
                                <a :href="`/tournaments/${tournament.id}`"><b-button variant="primary">Details</b-button></a>
                            </b-list-group-item>
                        </div>
                    </b-list-group>
                </b-col>
            </b-row>
        </b-container>

        
        
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

