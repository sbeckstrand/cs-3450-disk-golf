<template>
  <div>
        <Nav />
        {{ tournament }}
        <b-button variant="primary" @click="sponsorTournament()">Sponsor This Tournament</b-button>
        <h1>Sponsors</h1>
        <div v-for="sponsorship in sponsorships" :key="sponsorship.id">
            <div v-if="sponsorship.tournament == tournament.id">
                {{sponsorship}}
                <img :src="`http://localhost:8000${logos.find(element => element.sponsor = sponsorship.sponsor).logo}`" />
            </div>
        </div>
  </div>
</template>

<script>
export default {
    async asyncData({ params, $axios }) {
        const t = await $axios.$get(`/api/tournaments/${params.id}`)
        const s = await $axios.$get(`/api/sponsorships/`)
        const l = await $axios.$get(`/api/logo/`)
        console.log(l)
        return { 
            tournament: t, 
            sponsorships: s,
            logos: l
        }
    },
    methods: {
        async sponsorTournament() {
            try {
                let url = ""
                url = `/api/sponsorships/`
                await this.$axios.post(url, {
                    tournament: this.tournament.id,
                    sponsor: this.$auth.user.id
                });
                this.sponsorships = await this.$axios.$get(`/api/sponsorships/`)
                this.$toasted.global.defaultSuccess({
                    msg: `Tournament Sponsored!`
                })
            }
            catch (err) {
                let message = ""
                if (err.response.data.non_field_errors[0]) {
                    message = err.response.data.non_field_errors[0]
                }
                else {
                    message = err
                }
                this.$toasted.global.defaultError({
                    msg: `${message}`
                })       
            }
        }
    }
}
</script>

<style>

</style>d