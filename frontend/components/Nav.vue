<template>
  <div>
      <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="/">Disk Golf</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
            <b-nav-item href="/dashboard">Dashboard</b-nav-item>
            <b-nav-item href="/drinks">Drinks</b-nav-item>
            <b-nav-item href="/tournaments">Tournaments</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
    

        <div>
            <b-nav-item-dropdown right>
                <!-- Using 'button-content' slot -->
                <template #button-content>
                    <em>User</em>
                </template>
                <div v-if="$auth.loggedIn">
                  <b-dropdown-item href="#">Profile</b-dropdown-item>
                  <b-dropdown-item href="/logout">Sign Out</b-dropdown-item>
                </div>
                <div v-else>
                  <b-dropdown-item href="/login">Log In</b-dropdown-item>
                </div>
                

                
            </b-nav-item-dropdown>
        </div>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  </div>
</template>

<script>
export default {
  created() {
    console.log(this.$auth.loggedIn)
  }
}


</script>

<style>

</style>