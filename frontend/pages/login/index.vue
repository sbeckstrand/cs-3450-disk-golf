<template>
    <div>
        <b-container>
            <b-row class="d-flex justify-content-center">
                <b-col cols="12" md="6">
                    <b-form  @submit.stop.prevent class="border border-light p-3 mt-5 rounded bg-white">
                        
                        <div class="mb-3"> 
                            <label>Username</label>
                            <b-form-input 
                                v-model="user.username"
                                type="text"
                                class="mb">
                            </b-form-input>
                        </div>
                        
                        <label>Password</label>
                        <b-form-input
                            v-model="user.password"
                            type="password">
                        </b-form-input>
                        <b-button class="mt-3"
                            variant="primary"
                            @click="login">
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
        async login() {
            try {
                await this.$auth.loginWith('local', {
                    data: this.user
                })
                this.$toasted.global.defaultSuccess({
                    msg: "Login Successful!"
                })
            } catch (err) {
                this.$toasted.global.defaultError({
                    msg: "Login failed"
                })
            }
        }
    }
}
</script>

<style>

body {
    background-color: #BC8DA7;
}
</style>