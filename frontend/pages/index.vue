<template>
  <div>
    <Nav />
        <b-container>
            <b-row class="d-flex justify-content-center">
                <b-col cols="12" md="4">
                    <b-card class="p-3 mt-5 rounded" style="background-color: rgba(245, 245, 245, 0.3); ">
                      <div id="HASH" class="card-block special-card">
                      <span>
                        <b-button
                            variant="primary"
                            href="/signUp">
                            Sign Up
                        </b-button>
                      </span>
                      <span>
                        <b-button
                            variant="primary"
                            href="/login">
                            Login
                        </b-button>
                      </span>
                      </div>
                    </b-card>
                </b-col>
            </b-row>
        </b-container>

  </div>
</template>

<script>
export default {
  auth: 'guest'
}
</script>

<style>
body {
  background-image: url('https://www.chicagotribune.com/resizer/fDSmU4a0Nyy0Qpmk3uBW3uT1d_Q=/1200x0/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/CULYIVZ2S5GJZO6HYZKSCAP5VE.jpg');
  background-size: cover;
  background-repeat: no-repeat;
}
#HASH {
  display: flex;
  justify-content: space-between;
}
</style>