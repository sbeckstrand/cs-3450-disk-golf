<template>
    <div>
        <div v-for="user in users" :key="user.id">
            <div>
                {{ user }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    async asyncData({ $axios }) {
        const users = await $axios.$get('/api/users/')
        return { users }
    },
}
</script>

<style>

</style>