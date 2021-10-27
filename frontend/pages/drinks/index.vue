<template>
  <div>
    <Nav/>
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

                <b-button href="#" variant="primary">Order (Placeholder for now)</b-button>
            </b-card>
        </b-col> 
        </div>
        </b-row>
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