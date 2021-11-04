<template>
  <div>
      <Nav />
      <b-container>
            <b-row class="d-flex justify-content-center">
                <b-col cols="12" md="6">
                    <b-form  @submit.stop.prevent @submit="updateTournament" class="border border-light p-3 mt-5 rounded bg-white">
                        <div class="mb-3"> 
                            <label>Name</label>
                            <b-form-input 
                                v-model="updatedTournament.name"
                                type="text"
                                :placeholder="tournament.name"
                                class="mb"
                                required>Test
                            </b-form-input>
                        </div>

                        <div class="mb-3"> 
                            <label>Description</label>
                            <b-form-textarea 
                                v-model="updatedTournament.description"
                                rows="3"
                                :placeholder="tournament.description"
                                max-rows="6"
                                class="mb"
                                required>
                            </b-form-textarea>
                        </div>
                        
                        <label>Holes</label>
                        <b-form-input
                            v-model="updatedTournament.holes"
                            type="number"
                            :placeholder="String(tournament.holes)" 
                            required>
                        </b-form-input>

                        <label>Participants</label>
                        <b-form-input
                            v-model="updatedTournament.participants"
                            type="number"
                            :placeholder="String(tournament.participants)"
                            required>
                        </b-form-input>

                        <label>Start Date</label>
                        <b-form-datepicker
                            v-model="updatedTournament.startDate"
                            :placeholder="tournament.date"
                            required>
                        </b-form-datepicker>

                        <label>Start Time</label>
                        <b-form-timepicker
                            v-model="updatedTournament.startTime"
                            :placeholder="tournament.time"
                            required>
                        </b-form-timepicker>

                        <b-button class="mt-3"
                            variant="primary"
                            type="signup">
                            Create
                        </b-button>
                    </b-form>
                </b-col>
            </b-row>
        </b-container>
      {{ tournament }}
  </div>
</template>

<script>
export default {
    data() {
        return {
            updatedTournament: {}
        }
    },
    async asyncData({ params, $axios }) {
        const tournament = await $axios.$get(`/api/tournaments/${params.id}`)
        const date = new Date(tournament.startDate)
        tournament.date = date.toISOString().substring(0,10)
        tournament.time = date.toISOString().substring(11,19)
        return { tournament }
    },
    methods: {
        async updateTournament() {
            try {
                await this.$axios.put(`/api/tournaments/${this.tournament.id}`, {
                    name: this.updatedTournament.name,
                    description: this.updatedTournament.description,
                    holes: this.updatedTournament.holes,
                    participants: this.updatedTournament.participants,
                    startDate: this.updatedTournament.startDate + " " + this.updatedTournament.startTime
                });
                this.$router.push("/tournaments/");
                this.$toasted.global.defaultSuccess({
                    msg: "Tournament: " + this.updatedTournament.name + " Updated"
                })
            }
            catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    
                    msg: "Failed to update tournament."
                })       
            }
        }
    }
}
</script>

<style>

</style>