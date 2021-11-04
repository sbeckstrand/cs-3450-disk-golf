<template>
    <b-form  @submit.stop.prevent @submit="sendTournament" class="border border-light p-3 mt-5 rounded bg-white">
        <div class="mb-3"> 
            <label>Name</label>
            <b-form-input 
                v-model="editableTournament.name"
                type="text"
                ref="name"
                class="mb"
                required>Test
            </b-form-input>
        </div>

        <div class="mb-3"> 
            <label>Description</label>
            <b-form-textarea 
                v-model="editableTournament.description"
                rows="3"
                max-rows="6"
                class="mb"
                required>
            </b-form-textarea>
        </div>
        
        <label>Holes</label>
        <b-form-input
            v-model="editableTournament.holes"
            type="number"
            required>
        </b-form-input>

        <label>Participants</label>
        <b-form-input
            v-model="editableTournament.participants"
            type="number"
            required>
        </b-form-input>

        <label>Start Date</label>
        <b-form-datepicker
            v-model="editableTournament.startDate"
            required>
        </b-form-datepicker>

        <label>Start Time</label>
        <b-form-timepicker
            v-model="editableTournament.startTime"
            required>
        </b-form-timepicker>

        <b-button class="mt-3"
            variant="primary"
            type="signup">
            {{ editableTournament.id ? 'Edit' : 'Create' }}
        </b-button>
        {{ editableTournament }}
    </b-form>
</template>

<script>
export default {
    data()  {
        return {
            editableTournament: {}
        }
    }, 
    props: {
        tournament: Object
    },
    watch: {
        tournament: {
            handler (tournament) {
                if (tournament && tournament.id ) {
                    console.log(tournament)
                    this.editableTournament = tournament

                }
            },
            deep: true,
            immediate: true
        }
    }, 
    methods: {
        async sendTournament() {
            try {
                let url = ""
                let context = ""
                if (this.tournament && this.tournament.id) {
                    url = `/api/tournaments/${this.tournament.id}/`
                    context = "edite"
                } else {
                    url = `/api/tournaments/`
                    context = "create"
                }
                await this.$axios.put(url, {
                    name: this.tournament.name,
                    description: this.tournament.description,
                    holes: this.tournament.holes,
                    participants: this.tournament.participants,
                    startDate: this.tournament.startDate + " " + this.tournament.startTime
                });
                this.$router.push("/tournaments/");
                this.$toasted.global.defaultSuccess({
                    msg: `Tournament ${context}d`
                })
            }
            catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    msg: `Failed to save tournament.`
                })       
            }
        }
    }
}
</script>

<style>

</style>