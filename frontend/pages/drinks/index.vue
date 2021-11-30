<template>
  <div>
    <Nav/>
    <h3>Balance: {{ user.balance }}</h3>
    <b-row>
        <div v-for="drink in drinks" :key="drink.name">
            <b-col>
                <b-card
                    :title= "drink.name"
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2"
                >
                    <b-card-text>
                        ${{drink.price}}
                    </b-card-text>
                    <b-card-text>
                        {{drink.description}}
                    </b-card-text>
                    <b-card-text>
                        Type: {{drink.type}}
                    </b-card-text>

                    <b-button @click="placeOrder(drink)" variant="primary">Order</b-button>
                </b-card>
            </b-col> 
        </div>
    </b-row>
  </div>
</template>

<script>
export default {
    async asyncData({ $axios, $auth }) {
            const drinks = await $axios.$get('/api/drinks/')
            const user = await $axios.$get(`/api/users/${$auth.user.id}`)
            return { drinks, user }
        },
        methods: {
            async placeOrder(drink){
                try {
                    if (this.user.balance >= drink.price) {
                        await this.$axios.post(`/api/orderDrink/`, {
                            user_id: this.$auth.user.id,
                            name: drink.name,
                            drink_id: drink.id
                        });

                        await this.$axios.put('/api/updateBalance/', {
                            id: this.$auth.user.id,
                            amount: Math.ceil(drink.price),
                            action: 'subtract'
                        })
                        this.user.balance -= Math.ceil(drink.price)

                        this.$router.push("/drinks/");
                        this.$toasted.global.defaultSuccess({
                            msg: `Drink ordered`
                        })
                    } 
                    else {
                        throw new Error('Balance is too low')
                    }
                    
                }
                catch (err) {
                    console.log(err)
                    this.$toasted.global.defaultError({
                        msg: err
                    })       
                }
            }
        }
}
</script>

<style>

</style>