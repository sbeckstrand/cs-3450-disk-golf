<template>
  <div>
    <Nav />
    <b-container>
      <b-row>
        <div v-if="participation.length < 1">
          <h2>Not currently enrolled in any tournaments!</h2>
        </div>
        <div v-else>
          <h2>Current Tournaments</h2>
          <div v-for="part in participation" :key="part.id">
            {{ part }}
          </div>
        </div>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  async asyncData({ params, $axios, $auth }) {
      const t = await $axios.$get(`/api/tournaments/`)
      const p = await $axios.$get(`/api/participants/?user=${$auth.user.id}`)
      return { 
          tournaments: t,
          participation: p
      }
  },
  created() {
    if (this.$auth.user.groups.includes("manager")) {
      console.log(this.$auth.user.groups)
    } 
  }
}
</script>
