<template>
  <div>
    <Nav/>
    <b-container>
        <b-row>
            <b-col>
                <h5 class="mt-5">Balance: ${{ user.balance }}</h5>
                <h3>Drinks</h3>
                <b-list-group>
                    <b-list-group-item v-for="drink in drinks" :key="drink.name">
                        <p><b>Name:</b> {{ drink.name }}</p>
                        <p><b>Description:</b> {{ drink.description }}</p>
                        <p><b>Price:</b> {{ drink.price }}</p>
                        <b-button @click="placeOrder(drink)" variant="primary">Order</b-button>
                    </b-list-group-item>
                </b-list-group>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                
            </b-col>
        </b-row>
    </b-container>

    
    <b-row>
        
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