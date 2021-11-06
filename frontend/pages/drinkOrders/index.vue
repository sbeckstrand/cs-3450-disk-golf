<template>
  <div>
    <Nav/>
    <b-row>
    <div v-for="order in drinkOrders" :key="order.client">
        <b-col>
            <b-card
                :title= "users[order.client-1].username"
                tag="article"
                style="max-width: 20rem;"
                class="mb-2"
            >
                    <b-card-text>
                        {{drinks[order.drink-1].name}}
                    </b-card-text>
                    <b-button class="mt-3"
                    variant="danger"
                    @click="delOrder(order)">
                    Fill order
                    </b-button>

                
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
            const users = await $axios.$get('/api/users/')
            const drinks = await $axios.$get('/api/drinks/')
            return { drinkOrders,users,drinks }
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
            },
            async getInfo(order){

            }
        }
}
</script>

<style>

</style>