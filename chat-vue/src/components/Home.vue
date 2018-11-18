<template>
    <div>
        <h1>Chat using django rest and vue.js</h1>
        <button v-if="!auth" @click="goLogin">Login</button>
        <button v-else @click="logout">LogOut</button>
        <Room v-if="auth" @openDialog="openDialog"></Room>
        <div v-if="dialog.show" id="dialog">
            <h2>Room {{dialog.id}}:</h2>
            <Dialog :id="dialog.id"></Dialog>
        </div>

    </div>
</template>

<script>
    import Room from '@/components/rooms/Room'
    import Dialog from '@/components/rooms/Dialog'

    export default {
        name: "home",
        components: {
            Room,
            Dialog
        },
        data() {
            return {
                dialog: {
                    id: '',
                    show: false
                }
            }
        },
        computed: {
            auth() {
                let auth_token = localStorage.getItem('auth_token');
                if (auth_token) {
                    return true;
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            logout() {
                localStorage.removeItem('auth_token');
                window.location = '/'
            },
            openDialog(id){
                this.dialog.id = id;
                this.dialog.show = true
            }
        }
    }
</script>

<style scoped>
    #dialog{
        border: black solid;
        text-align: left;
        margin: 10px;
        padding: 10px;
    }
    #dialog h2{
        text-align: center;
    }
</style>
