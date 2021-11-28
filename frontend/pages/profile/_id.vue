<template>
    <div>
        <p>ID: {{ user.id }}</p>
        <p>Username: {{ user.username }}</p>
        <p>Email: {{ user.email }}</p>
        <p>Groups: {{ user.groups }}</p>
        <p>Balance: {{ user.balance }}</p>

        <b-button v-if="!user.groups.some(group => group.name === 'drink_meister')" @click="addRole('drink_meister')">Make Drink Meister</b-button>
        <b-button v-if="!user.groups.some(group => group.name === 'manager')" @click="addRole('manager')">Make Manager</b-button>
        <b-button v-if="!user.groups.some(group => group.name === 'sponsor')" @click="addRole('sponsor')">Make Sponsor</b-button>
    </div>
</template>

<script>
export default {
    async asyncData({ params, $axios, $auth }) {
        console.log($auth.user.groups)
        
        if ($auth.user.groups.some(group => group.name === 'manager')) {
            const user = await $axios.$get(`/api/users/${params.id}`)
            return { user }
        }
        else {
            return {}
        }

    },
    methods: {
        async addRole(role) {
            try {
                let url = ""
                url = `/api/updateRole/`
                await this.$axios.put(url, {
                    id: this.user.id,
                    newRole: role
                });
                this.$toasted.global.defaultSuccess({
                    msg: `Role Updated.`
                })
                this.user.groups.push({'name': role})
            }
            catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    msg: `Failed to update Role.`
                })       
            }
        }
    },
    created() {
        if (!this.$auth.user.groups.some(group => group.name === 'manager')) {
            this.$router.push("/dashboard")
        }
    },
    
}
</script>

<style>

</style>