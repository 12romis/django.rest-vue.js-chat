<template>
    <div>
        <h1>Chat using django rest and vue.js</h1>
        <button v-if="!auth" @click="goLogin">Login</button>
        <button v-else @click="logout">LogOut</button>
        <room v-if="auth"></room>
    </div>
</template>

<script>
    import Room from '@/components/Room'

    export default {
        name: "home",
        components: {
            Room
        },
        computed:{
            auth(){
                let auth_token = localStorage.getItem('auth_token');
                if(auth_token){
                    return true;
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            logout(){
                localStorage.removeItem('auth_token');
                window.location = '/'
            }
        }
    }
</script>

<style scoped>

</style>
