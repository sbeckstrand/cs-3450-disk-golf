<template>
  <div>
      <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">NavBar</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
            <b-nav-item href="#">Dashboard</b-nav-item>
            <b-nav-item href="drinks">Drinks</b-nav-item>
            <b-nav-item href="tournaments">Tournaments</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
    

        <div :v-if="isLoggedIn">
            <b-nav-item-dropdown right>
                <!-- Using 'button-content' slot -->
                <template #button-content>
                    <em>User</em>
                </template>
                <b-dropdown-item href="#">Profile</b-dropdown-item>
                <b-dropdown-item href="logout">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
        </div>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>