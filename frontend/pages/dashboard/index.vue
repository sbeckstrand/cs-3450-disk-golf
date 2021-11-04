<template>
  <div>
    <Nav />
    <b-row>
      <b-col>1 of 3</b-col>
      <b-col>2 of 3</b-col>
      <b-col>3 of 3</b-col>
      <b-col>3 of 4</b-col>
    </b-row>
    <b-button class="bg-primary" >Button</b-button>
  </div>
</template>

<script>
export default {
  created() {
    console.log(this.$auth.user)
  }
}
</script>
