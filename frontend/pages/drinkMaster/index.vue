<template>
  <div>
    <Nav />
    <b-container>
        <b-row>
            <b-col>
                <b-button href="/drinkMaster/create" class="mt-5" variant="success">
                    Add New Drink
                </b-button>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <b-list-group>
                    <h3 class="mt-5">Existing Drinks</h3>
                    <b-list-group-item v-for="drink in drinks" :key="drink.id">
                        <p><b>Name:</b> {{ drink.name }}</p>
                        <p><b>Description:</b> {{ drink.description }}</p>
                        <p><b>Price:</b> {{ drink.price }}</p>
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
                    </b-list-group-item>
                </b-list-group>
            </b-col>
        </b-row>
    </b-container>
        
        
        
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
                this.drinks.splice(drinkIndex, 1)
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