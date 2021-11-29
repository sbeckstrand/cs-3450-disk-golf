<template>
    <div>
        <Nav/>
        <p>ID: {{ user.id }}</p>
        <p>Username: {{ user.username }}</p>
        <p>Email: {{ user.email }}</p>
        <p>Groups: {{ user.groups }}</p>
        <p>Balance: {{ user.balance }}</p>

        <b-button v-if="!user.groups.some(group => group.name === 'drink_meister')" variant="success" @click="addRole('drink_meister')">Add Drink Meister Role</b-button>
        <b-button v-else variant="danger" @click="removeRole('drink_meister')">Remove Drink Meister Role</b-button>

        <b-button v-if="!user.groups.some(group => group.name === 'manager')" variant="success" @click="addRole('manager')">Make Manager</b-button>
        <b-button v-else variant="danger" @click="removeRole('manager')">Remove Manager Role</b-button>

        <b-button v-if="!user.groups.some(group => group.name === 'sponsor')" variant="success" @click="addRole('sponsor')">Make Sponsor</b-button>
        <b-button v-else variant="danger" @click="removeRole('sponsor')">Remove Sponsor Role</b-button>

        <b-form  @submit.stop.prevent @submit="updateBalance(balance)" class="border border-light p-3 mt-5 rounded bg-white">
                <label>Update Balance</label>
                <b-form-input
                    v-model="balance"
                    type="number"
                    required>
                </b-form-input>

                <b-button class="mt-3"
                    variant="primary"
                    type="submit">
                    Update
                </b-button>
            </b-form>

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
                    newRole: role,
                    action: 'add'
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
        },
        async removeRole(role) {
            try {
                let url = ""
                url = `/api/updateRole/`
                await this.$axios.put(url, {
                    id: this.user.id,
                    newRole: role,
                    action: 'remove'
                });
                this.$toasted.global.defaultSuccess({
                    msg: `Role removed.`
                })
                this.user.groups = this.user.groups.filter(function( obj ) {
                    return obj.name !== role;
                })
            }
            catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    msg: `Failed to remove role.`
                })       
            }
        },
        async updateBalance(updateAmount) {
            try {
                const url = `/api/updateBalance/`
                let updateAction = ""

                if (updateAmount >= 0) {
                    updateAction = "add"
                } else {
                    updateAction = "substract"
                }

                await this.$axios.put(url, {
                    id: this.user.id,
                    amount: updateAmount,
                    action: updateAction
                });
                this.$toasted.global.defaultSuccess({
                    msg: `Balance Updated.`
                })
                this.user.balance += parseInt(this.balance)
            }
            catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    msg: `Failed to update Balance.`
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