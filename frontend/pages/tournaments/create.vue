<template>
    <div>
        <Nav />
        <b-container>
            <b-row class="d-flex justify-content-center">
                <b-col cols="12" md="6">
                    <b-form  @submit.stop.prevent @submit="addTournament" class="border border-light p-3 mt-5 rounded bg-white">
                        <div class="mb-3"> 
                            <label>Name</label>
                            <b-form-input 
                                v-model="tournament.name"
                                type="text"
                                class="mb"
                                required>
                            </b-form-input>
                        </div>

                        <div class="mb-3"> 
                            <label>Description</label>
                            <b-form-textarea 
                                v-model="tournament.description"
                                rows="3"
                                max-rows="6"
                                class="mb"
                                required>
                            </b-form-textarea>
                        </div>
                        
                        <label>Holes</label>
                        <b-form-input
                            v-model="tournament.holes"
                            type="number"
                            required>
                        </b-form-input>

                        <label>Participants</label>
                        <b-form-input
                            v-model="tournament.participants"
                            type="number"
                            required>
                        </b-form-input>

                        <label>Start Date</label>
                        <b-form-datepicker
                            v-model="tournament.startDate"
                            required>
                        </b-form-datepicker>

                        <label>Start Time</label>
                        <b-form-timepicker
                            v-model="tournament.startTime"
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
  </div>
  
  
</template>

<script>
export default {
    data() {
        return {
            tournament: {}
        }
    },
    methods: {
        async addTournament() {
            try {
                await this.$axios.post('/api/tournaments/', {
                    name: this.tournament.name,
                    description: this.tournament.description,
                    holes: this.tournament.holes,
                    participants: this.tournament.participants,
                    startDate: this.tournament.startDate + " " + this.tournament.startTime
                });
                console.log(this.tournament.startTime)
                this.$router.push("/tournaments/");
                this.$toasted.global.defaultSuccess({
                    msg: "Tournament: " + this.tournament.name + " Created"
                })
            }
            catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    
                    msg: "Failed to create tournament."
                })       
            }
        }
    }
}
</script>

<style>

</style>