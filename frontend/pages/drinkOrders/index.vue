<template>
  <div>
    <Nav/>
    <b-container>
        <b-row>
            <b-col>
                <h3 class="mt-5">Drink Orders</h3>
                <div v-if="drinkOrders.length < 1">
                    <p>No Drink Orders at the moment!</p>
                </div>
                <div v-else>
                    <b-list-group>
                        <b-list-group-item v-for="order in drinkOrders" :key="order.client">
                            <p>Client: {{ users[order.client-1].username }}</p>
                            <p>Drink: {{drinks[order.drink-1].name}}</p>
                            <b-button
                                variant="danger"
                                @click="delOrder(order)">
                                Fill order
                            </b-button>
                        </b-list-group-item>     
                    </b-list-group>
                </div>
            </b-col>
        </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
    async asyncData({ $axios, $config }) {
            const drinkOrders = await $axios.$get('/api/orders/')
            const users = await $axios.$get('/api/users/')
            const drinks = await $axios.$get('/api/drinks/')
            return { drinkOrders,users,drinks }
        },
        data() {
            return {
                fields: ['drink', 'client', 'Fill']
            }
        },
        methods: {
            async delOrder(order) {
                try {
                    const orderIndex = this.drinkOrders.findIndex(t => t.id === order.id)
                    await this.$axios.delete(`/api/orders/${order.id}`)
                    this.drinkOrders.splice(orderIndex, 1)
                } catch (err) {
                    console.log(err)
                    this.$toasted.global.defaultError({
                        msg: "Failed to fill order."
                    }) 
                }
            }
        }
}
</script>

<style>

</style>