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
                @click="delDrink(drink)">
                Delete
            </b-button>
            <b-button class="mt-3"
                variant="secondary"
                :href="'/drinkMaster/edit/' + drink.id">
                
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
        },
        methods: {
        async delDrink(drink) {
            try {
                const drinkIndex = this.drinks.findIndex(t => t.id === drink.id)
                await this.$axios.delete(`/api/drinks/${drink.id}`)
                this.tournaments.splice(drinkIndex, 1)
            } catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    msg: "Failed to delete drink."
                }) 
            }
        }
    }
}
</script>

<style>

</style>