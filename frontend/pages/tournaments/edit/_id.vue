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
    async asyncData({ params, $axios }) {
        const tournament = await $axios.$get(`/api/tournaments/${params.id}`)
        const date = new Date(tournament.startDate)
        tournament.startDate = date.toISOString().substring(0,10)
        tournament.startTime = date.toISOString().substring(11,19) 
        return { tournament }
    }
}
</script>

<style>

</style>