<template>
    <div>
        <Nav/>
        <b-container>
            <b-row>
                <b-col>
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
                </b-col>
                <b-col>
                    <b-img v-if="logo" :src="`http://localhost:8000${logo.logo}`" thumbnail fluid rounded center alt="logo" class="mt-5"></b-img> 
                </b-col>
            </b-row>
            <b-row>
                <b-col>
                    <h3 class="mt-3">Sponsored Tournaments</h3>
                    <b-list-group>
                        <b-list-group-item v-for="sponsorship in sponsorships" :key="sponsorship.id">
                            <div v-if="sponsorship.sponsor == $auth.user.id">
                                <div :set="tournament = tournaments.find(element => element.id === sponsorship.tournament)">
                                    <h4>{{ tournament.name }}</h4>
                                    <p>{{ tournament.description }}</p>
                                    <p>{{ sponsorship }}</p>
                                </div>
                                <b-button variant="danger" @click="delSponsorship(sponsorship)">Remove Sponsorship</b-button>
                            </div>
                        </b-list-group-item>
                    </b-list-group>
                    
                </b-col>
            </b-row>
        </b-container>
          
        

    </div>
</template>

<script>
export default {
    async asyncData({ $axios, $auth }) {
        const t = await $axios.$get(`/api/tournaments/`)
        const s = await $axios.$get(`/api/sponsorships/`)
        const logos = await $axios.$get('/api/logo/')
        let l
        for (const item in logos) {
            
            if (logos[item].sponsor === $auth.user.id) {
                l = logos[item]
            }
        }
        return { 
            logo: l,
            tournaments: t,
            sponsorships: s
         }
    },
    data() {
        return {
            file: null,
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
        },
        async delSponsorship(sponsorship) {
            try {
                const sponsorshipIndex = this.sponsorships.findIndex(s => s.id === sponsorship.id)
                await this.$axios.delete(`/api/sponsorships/${sponsorship.id}`)
                this.sponsorships.splice(sponsorshipIndex, 1)
                this.$toasted.global.defaultSuccess({
                    msg: `Removed Sponsorship`
                })
            } catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    msg: "Failed to remove Sponsorship"
                }) 
            }
        }
    }
}
</script>

<style>

</style>