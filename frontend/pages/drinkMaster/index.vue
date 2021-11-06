<template>
  <div>
    <Nav />
        <div>
            <b-button href="/drinkMaster/create" class="mt-3">
                Add drink
            </b-button>
        </div>
        <div v-for="drink in drinks" :key="drink.id">
            {{ drink }} 
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
    async asyncData({ $axios, $config }) {
            const drinks = await $axios.$get('/api/drinks/')
            return { drinks }
        }
}
</script>

<style>

</style>