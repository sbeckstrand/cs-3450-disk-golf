<template>
  <div>
        <b-container>
            <b-row class="d-flex justify-content-center">
                <b-col cols="12" md="6">
                    <b-form  @submit.stop.prevent @submit="signup" class="border border-light p-3 mt-5 rounded bg-white">
                        <div class="mb-3"> 
                            <label>Username</label>
                            <b-form-input 
                                v-model="user.username"
                                type="text"
                                class="mb"
                                required>
                            </b-form-input>
                        </div>

                        <div class="mb-3"> 
                            <label>Email</label>
                            <b-form-input 
                                v-model="user.email"
                                type="email"
                                class="mb"
                                required>
                            </b-form-input>
                        </div>
                        
                        <label>Password</label>
                        <b-form-input
                            v-model="user.password"
                            type="password"
                            required>
                        </b-form-input>
                        <b-button class="mt-3"
                            variant="primary"
                            type="signup">
                            Login
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
            user: {}
        }
    },
    methods: {
        async signup() {
            try {
                await this.$axios.post('api/signup/', {
                    username: this.user.username,
                    email: this.user.email,
                    password: this.user.password,
                    groups: "['player']"
                })

                await this.$auth.loginWith('local', {
                    data: this.user
                })

                this.$toasted.global.defaultSuccess({
                    msg: "Signup Successful!"
                })
            }
            catch (err) {
                for (const inError in err.response.data) {
                    this.$toasted.global.defaultError({
                        msg: err.response.data[inError][0]
                    })
                }
                
            }
        }
    },
    auth: 'guest'
}
</script>

<style>

</style>