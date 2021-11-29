<template>
    <div>
        <Nav/>

        <b-form   class="border border-light p-3 mt-5 rounded bg-white" @submit.stop.prevent @submit="uploadImage(file)" >
            <div class="mb-3"> 
                <label>Logo</label>
                <b-form-file 
                    v-model="file"
                    type="file" 
                    name="file" 
                    accept="image/jpeg, image/png"
                    class="mb"
                    required
                    @change="onFileChange">
                </b-form-file>
            </div>

            <b-button class="mt-3"
            variant="primary"
            type="submit">
                Upload Image
            </b-button>

        </b-form>
        <img v-if="logo" :src="`http://localhost:8000${logo.logo}`" />   
    </div>
</template>

<script>
export default {
    async asyncData({ $axios, $auth }) {
        const logos = await $axios.$get('/api/logo/')
        let logo
        for (const item in logos) {
            
            if (logos[item].sponsor === $auth.user.id) {
                logo = logos[item]
            }
        }
        console.log(logo)
        return { logo }
    },
    data() {
        return {
            file: null
        }
    },
    methods: {
        onFileChange(e) {
            const files = e.target.files || e.dataTransfer.files;
            if (!files.length) {
                return;
            }
            this.file = files[0];
            this.file = this.createImage(files[0]);
        },
        createImage(file) {
            // let image = new Image();
            const reader = new FileReader();
            const vm = this;
            reader.onload = e => {
                vm.preview = e.target.result;
            };
            reader.readAsDataURL(file);
        },
        async uploadImage() {
            const config = {
                headers: { "content-type": "multipart/form-data; boundary=63c5979328c44e2c86934" }
            };
            try {
                const formData = new FormData()
                formData.append('logo', this.file, this.file.name)
                formData.append('sponsor', this.$auth.user.id)
                await this.$axios.put("/api/logo/", formData, config)
                this.$router.push("/sponsor/");
                this.$toasted.global.defaultSuccess({
                    msg: `Logo Uploaded`
                })
                
                const logos = await this.$axios.$get('/api/logo/')
                let logo
                for (const item in logos) {
                    
                    if (logos[item].sponsor === this.$auth.user.id) {
                        logo = logos[item]
                    }
                }

                this.logo = logo
            } 
            catch (err) {
                this.$toasted.global.defaultError({
                    msg: `Failed to upload Logo`
                })   
            }
        }
    }
}
</script>

<style>

</style>