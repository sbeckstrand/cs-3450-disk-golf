<template>
    <div>
        {{ user }}
    </div>
</template>

<script>
export default {
    async asyncData({ params, $axios }) {
        const user = await $axios.$get(`/api/users/${params.id}`)
        return { user }
    },
}
</script>

<style>

</style>