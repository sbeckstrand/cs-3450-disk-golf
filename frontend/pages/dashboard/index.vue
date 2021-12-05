<template>
  <div>
    <Nav />
    <b-container>
      <div>
        <div v-if="participation.length < 1">
          <b-row>
            <b-col>
              <h2 class="mt-3">Not currently enrolled in any tournaments!</h2>
              <a href="/tournaments/">Go find some tournaments!</a>
            </b-col>   
          </b-row>
        </div>
        <div v-else>
          <b-row>
            <b-col>
              <h3 class="mt-5">My Active Tournaments</h3>
              <b-list-group>
                <div v-for="part in participation" :key="part.id">
                  <div :set="tournament = tournaments[tournaments.findIndex( t => t.id === part.tournament)]">
                    <b-list-group-item v-if="tournament.active === true">
                      <h5>
                        <a :href="`/tournaments/${part.tournament}`">
                        {{ tournament.name }}
                        </a>
                      </h5>
                      <h6>{{ tournament.holes }} holes</h6>
                      <p>{{ tournament.description }}</p>
                      <p><span class="font-weight-bold">Total Scores:</span> {{ part.score }}</p>
                      <div v-if="part.scores.length < tournament.holes">
                        <p><span class="font-weight-bold">Current Hole:</span> {{ part.scores.length + 1 }}</p>
                        <b-form  @submit.stop.prevent @submit="updateScore(part.currScore, part)">
                          <label><span class="font-weight-bold">Submit Score for Hole:</span> {{ part.scores.length + 1 }}</label>
                          <b-form-input
                              v-model="part.currScore"
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
                      </div>
                    </b-list-group-item>
                  </div>
                </div>
              </b-list-group>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <h3 class="mt-5">My Inactive Tournaments</h3>
              <b-list-group>
                <div v-for="part in participation" :key="part.id">
                  <div :set="tournament = tournaments[tournaments.findIndex( t => t.id === part.tournament)]">
                    <b-list-group-item v-if="tournament.active === false">
                      <h5>
                        <a :href="`/tournaments/${part.tournament}`">
                        {{ tournament.name }}
                        </a>
                      </h5>
                      <h6>{{ tournament.holes }} holes</h6>
                      <p>{{ tournament.description }}</p>
                      <p><span class="font-weight-bold">Total Scores:</span> {{ part.score }}</p>
                    </b-list-group-item>
                  </div>
                </div>
              </b-list-group>
            </b-col>
          </b-row>
        </div>

        <b-row>
          <b-col>
            <h3 class="mt-5">Balance : ${{ user.balance }}</h3>
            <b-form  @submit.stop.prevent @submit="updateBalance(balance)" class="border border-light mt-1 rounded bg-white">
                <label>Increase Balance</label>
                <b-form-input
                    v-model="balance"
                    min="1"
                    type="number"
                    required>
                </b-form-input>

                <b-button class="mt-3"
                    variant="primary"
                    type="submit">
                    Update
                </b-button>
            </b-form>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </div>
</template>

<script>
export default {
  async asyncData({ params, $axios, $auth }) {
      const t = await $axios.$get(`/api/tournaments/`)
      const p = await $axios.$get(`/api/participants/?user=${$auth.user.id}`)
      const u = await $axios.$get(`/api/users/${$auth.user.id}`)
      const s = await $axios.$get(`/api/scores/?user=${$auth.user.id}`)
      let totalScore = 1 // Adjust this to use for loop to get total
      totalScore = 0
      for (const index in p) {
        const partScores = s.filter(s => s.tournament === p[index].tournament)
        let total = 0
        for (const score in partScores) {
          total += partScores[score].value
        }
        p[index].score = total
        p[index].hole = 1
        p[index].scores = partScores
      }
      return { 
          user: u,
          tournaments: t,
          participation: p,
          scores: s,
          total: totalScore
      }
  },
  data() {
    return {
      balance: 0
    } 
  },
  created() {
    if (this.$auth.user.groups.includes("manager")) {
      console.log(this.$auth.user.groups)
    } 
  }, 
  methods: {
    async updateBalance(updateAmount) {
        try {
            const url = `/api/updateBalance/`
            await this.$axios.put(url, {
                id: this.user.id,
                amount: updateAmount,
                action: 'add'
            });
            this.user.balance += parseInt(this.balance)
        }
        catch (err) {
            console.log(err)
            this.$toasted.global.defaultError({
                msg: `Failed to update Balance.`
            })       
        }
    },
    async updateScore(score, part) {
 
      // determine which hole
      try {
        const data = {
          hole: part.scores.length + 1,
          value: score,
          player: this.$auth.user.id,
          tournament: part.tournament
        }
        await this.$axios.post(`/api/scores/`, data)

        this.$toasted.global.defaultSuccess({
            msg: `Score Saved`
        })   

        this.scores.push(data)
        part.scores.push(data)
        part.score += parseInt(score)
  
      } 
      catch (err) {
        this.$toasted.global.defaultError({
              msg: `Failed to save score`
          })   
      }
    }
  }
}
</script>

<style>
body {
  background-image: none;
}
</style>