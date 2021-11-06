<template>
  <div>
    <Nav/>
    <b-row>
    <div v-for="order in drinkOrders" :key="order.client">
        <b-col>
            <b-card
                :title= "order.client.username"
                tag="article"
                style="max-width: 20rem;"
                class="mb-2"
            >
                    <b-card-text>
                        ${{order.drink.name}}
                    </b-card-text>

                <b-button href="#" variant="primary">Complete Order (Placeholder for now)</b-button>
            </b-card>
        </b-col> 
        </div>
        </b-row>
  </div>
</template>

<script>
export default {
    async asyncData({ $axios, $config }) {
            const drinkOrders = await $axios.$get('/api/orders/')
            return { drinkOrders }
        }
}
</script>

<style>

</style>