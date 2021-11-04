<template>
    <div>
        <Nav />
        <b-container>
            <b-row class="d-flex justify-content-center">
                <b-col cols="12" md="6">
                    <TournamentForm :tournament="tournament"/>
                </b-col>
            </b-row>
        </b-container>
  </div>
  
  
</template>

<script>
export default {
    data() {
        return {
            tournament: {}
        }
    }
}
</script>

<style>

</style>