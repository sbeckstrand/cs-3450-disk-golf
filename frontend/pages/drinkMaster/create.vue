<template>
    <div>
        <Nav />
        <b-container>
            <b-row class="d-flex justify-content-center">
                <b-col cols="12" md="6">
                    <DrinkForm :drink="drink"/>
                </b-col>
            </b-row>
        </b-container>
  </div>
  
  
</template>

<script>
export default {
    data() {
        return {
            drink: {}
        }
    }
}
</script>

<style>

</style>