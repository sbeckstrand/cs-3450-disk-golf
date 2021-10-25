<template>
  <div>
    <Nav/>
    <div v-for="drink in drinks" :key="drink.name">
    <b-card
        :title= drinks.Name
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