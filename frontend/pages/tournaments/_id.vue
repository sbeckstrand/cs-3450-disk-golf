<template>
  <div>
    <Nav />
    <b-container>
        <b-row>
            <b-col>
                <h3 class="mt-5">Tournament Details</h3>
                <p><b>Name:</b> {{ tournament.name }}</p>
                <p><b>Description:</b> {{ tournament.description }}</p>
                <p><b>Holes:</b> {{ tournament.holes }}</p>
                <p><b>Prize Pool:</b> {{tournament.pool }}</p>
                <p>
                    <b>Status: </b> 
                    <span v-if="tournament.active == true"> Active </span>
                    <span v-else>Inactive</span>
                </p>
                <b-button v-if="participation.length < 1" 
                    variant="success"
                    @click="toggleParticipation()">
                    Participate in Tournament
                </b-button>
                <b-button v-else
                    variant="danger"
                    @click="toggleParticipation()">
                    Disenroll from tournament
                </b-button>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <h3 class="mt-5">Scores</h3>
                <div class="accordion" role="tablist">
                    <b-card v-for="score in scores" :key="score.id" no-body class="mb-1">
                        <b-card-header header-tag="header" class="p-1" role="tab">
                            <b-button block v-b-toggle="`accordion${score.hole}`" variant="info">Hole: {{ score.hole }}</b-button>
                        </b-card-header>
                        <b-collapse :id="`accordion${score.hole}`" accordion="my-accordion" role="tabpanel">
                            <b-card-body>
                                <b-card-text></b-card-text>
                                <b-form  @submit.stop.prevent @submit="updateScore(score)">
                                    <label>Score</label>
                                    <b-form-input
                                        v-model="score.value"
                                        type="number"
                                        min="-5"
                                        max="30"
                                        required>
                                    </b-form-input>

                                    <b-button class="mt-3"
                                        variant="primary"
                                        type="submit">
                                        Submit
                                    </b-button>
                                </b-form>
                            </b-card-body>
                        </b-collapse>
                    </b-card>
                </div>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <div v-if="$auth.user.groups.some(group => group.name === 'manager')">
                    <h3 class="mt-5">Management Control</h3>
                    <b-button v-if="$auth.user.groups.some(group => group.name === 'manager')"
                        variant="secondary"
                        :href="'/tournaments/edit/' + tournament.id">
                        
                        Edit
                    </b-button>
                    <b-button v-if="$auth.user.groups.some(group => group.name === 'manager')"
                        variant="danger"
                        @click="delTournament(tournament)">
                        Delete
                    </b-button>
                    <b-button v-if="$auth.user.groups.some(group => group.name === 'manager')"
                        variant="info"
                        @click="toggleActive()">
                        <span v-if="tournament.active == true">
                        Mark Tournament as Inactive
                        </span>
                        <span v-if="tournament.active == false">
                        Mark Tournament as Active
                        </span>
                    </b-button>
                </div> 
            </b-col>
        </b-row> 
        <b-row>
            <b-col>
                <h3 class="mt-5">Sponsors</h3>
            </b-col>
        </b-row>
        <b-row>
            <div v-for="sponsorship in sponsorships" :key="sponsorship.id">
                
                <b-col v-if="sponsorship.tournament == tournament.id">
                    <b-img :src="`http://localhost:8000${logos.find(element => element.sponsor === sponsorship.sponsor).logo}`" thumbnail fluid rounded alt="logo"></b-img>
                </b-col>
            </div>
        </b-row>
        <b-row>
            <b-col>
                <b-button v-if="$auth.user.groups.some(group => group.name === 'sponsor')"
                    class="mt-3"
                    variant="primary" 
                    @click="sponsorTournament()">
                    Sponsor This Tournament
                </b-button>
            </b-col>
        </b-row>
    </b-container>   
  </div>
</template>

<script>
export default {
    async asyncData({ params, $axios, $auth }) {
        const t = await $axios.$get('/api/tournaments/')
        const tCurr = await $axios.$get(`/api/tournaments/${params.id}`)
        const s = await $axios.$get(`/api/sponsorships/`)
        const l = await $axios.$get(`/api/logo/`)
        const scores = await $axios.$get(`/api/scores/?user=${$auth.user.id}`)
        const tScores = scores.filter(score => score.tournament === tCurr.id)
        let p = await $axios.$get(`/api/participants/?user=${$auth.user.id}`)
        p = p.filter(element => element.tournament === tCurr.id)
        console.log(p)
        return { 
            tournaments: t,
            tournament: tCurr, 
            sponsorships: s,
            logos: l,
            participation: p,
            scores: tScores
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
        },
        async delTournament(tournament) {
            try {
                const tournamentIndex = this.tournaments.findIndex(t => t.id === tournament.id)
                await this.$axios.delete(`/api/tournaments/${tournament.id}`)
                this.tournaments.splice(tournamentIndex, 1)
                this.$router.push('/tournaments/')
            } catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    msg: "Failed to delete tournament."
                }) 
            }
        },
        async toggleActive() {
            try{
                await this.$axios.put(`/api/toggleTournament/`, {
                    id: this.tournament.id
                })

                if (this.tournament.active === false) {
                    this.tournament.active = true
                } else {
                    this.tournament.active = false
                }
            } catch (err) {

                let context
                if (this.tournament.active === false) {
                    context = "activate"
                    this.tournament.active = true
                } else {
                    context = "deactivate"
                    this.tournament.active = false
                }

                this.$toasted.global.defaultError({
                    msg: `Failed to ${context} tournament.` 
                }) 
            }
            
        },
        async toggleParticipation() {
            if (this.participation.length < 1) {
                try {
                    this.participation = await this.$axios.post(`/api/participants/`, {
                        user: this.$auth.user.id,
                        tournament: this.tournament.id
                    })

                    this.participation = await this.$axios.$get(`/api/participants/?user=${this.$auth.user.id}`)
                    this.participation = this.participation.filter(element => element.tournament === this.tournament.id)

                    //  await this.$axios.$get('/api/participants/', { 
                    //     tournament: this.tournament,
                    //     user: this.$auth.user
                    // })

                    this.$toasted.global.defaultSuccess({
                        msg: `You're now participating in this tournament.` 
                    }) 
                } catch (err) {
                    this.$toasted.global.defaultError({
                        msg: `Failed to enroll in tournament.` 
                    }) 
                }
            } 
            else {
                try {
                    await this.$axios.delete(`/api/participants/${this.participation[0].id}?user=${this.$auth.user.id}`)

                    this.participation = []

                    this.$toasted.global.defaultSuccess({
                        msg: `You are no longer enrolled to this touranment.` 
                    }) 
                } catch (err) {
                    this.$toasted.global.defaultError({
                        msg: `Failed to disenroll from touranment.` 
                    }) 
                }
            }
        },
        async updateScore(score) {
            try {
                console.log(score)
                const data = {
                hole: score.hole,
                value: score.value,
                player: score.player,
                tournament: score.tournament
                }
                await this.$axios.$put(`/api/scores/${score.id}/`, data)

                this.$toasted.global.defaultSuccess({
                    msg: `success.`
                })   
        
            } 
            catch (err) {
                this.$toasted.global.defaultError({
                    msg: `${err}`
                })   
            }
        }
    }
}
</script>

<style>

</style>