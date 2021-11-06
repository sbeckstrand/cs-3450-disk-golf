<template>
    <b-form  @submit.stop.prevent @submit="sendDrink" class="border border-light p-3 mt-5 rounded bg-white">
        <div class="mb-3"> 
            <label>Name</label>
            <b-form-input 
                v-model="editableDrink.name"
                type="text"
                ref="name"
                class="mb"
                required>
            </b-form-input>
        </div>

        <div class="mb-3"> 
            <label>Description</label>
            <b-form-textarea 
                v-model="editableDrink.description"
                rows="3"
                max-rows="6"
                class="mb"
                required>
            </b-form-textarea>
        </div>
        
        <label>Price</label>
        <b-form-input
            v-model="editableDrink.price"
            type="number"
            step=".01"
            required>
        </b-form-input>

        <label>Type</label>
            <b-form-input 
            v-model="editableDrink.type"
            type="text"
            ref="name"
            class="mb"
            required>
        </b-form-input>

        <b-button class="mt-3"
            variant="primary"
            type="signup">
            {{ editableDrink.id ? 'Edit' : 'Create' }}
        </b-button>
    </b-form>
</template>

<script>
export default {
    data()  {
        return {
            editableDrink: {}
        }
    }, 
    props: {
        drink: Object
    },
    watch: {
        drink: {
            handler (drink) {
                if (drink) {
                    console.log(drink)
                    this.editableDrink = drink
                }
            },
            deep: true,
            immediate: true
        }
    }, 
    methods: {
        async sendDrink() {
            try {
                let url = ""
                let context = ""
                if (this.drink && this.drink.id) {
                    url = `/api/drinks/${this.drink.id}/`
                    context = "edite"
                    await this.$axios.put(url, {
                        name: this.drink.name,
                        description: this.drink.description,
                        price: this.drink.price,
                        type: this.drink.type,
                        
                    });
                } else {
                    url = `/api/drinks/`
                    context = "create"
                    await this.$axios.post(url, {
                        name: this.drink.name,
                        description: this.drink.description,
                        price: this.drink.price,
                        type: this.drink.type,
                    });
                }
                this.$router.push("/drinks/");
                this.$toasted.global.defaultSuccess({
                    msg: `Drink ${context}d`
                })
            }
            catch (err) {
                console.log(err)
                this.$toasted.global.defaultError({
                    msg: `Failed to save drink.`
                })       
            }
        }
    }
}
</script>

<style>

</style>