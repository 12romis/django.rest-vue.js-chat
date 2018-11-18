<template>
    <div>
        <mu-appbar style="width: 100%;" color="primary">
            <mu-button icon slot="left">
                <mu-icon value="menu"></mu-icon>
            </mu-button>
            Chat using django rest and vue.js
            <mu-button v-if="!auth" @click="goLogin" flat slot="right">Login</mu-button>
            <mu-button v-else @click="logout" flat slot="right">LogOut</mu-button>
        </mu-appbar>

        <mu-container>
            <mu-row>
                <mu-col span="4">
                    <Room v-if="auth" @openDialog="openDialog"></Room>
                </mu-col>

                <mu-col v-if="dialog.show" id="dialog" span="8">
                    <h2>Room {{dialog.id}}:</h2>
                    <Dialog :id="dialog.id"></Dialog>
                </mu-col>
            </mu-row>
        </mu-container>
    </div>
</template>

<script>
    import Room from '@/components/rooms/Room'
    import Dialog from '@/components/rooms/Dialog'
    import MuContainer from "muse-ui/es5/Grid/Container";

    export default {
        name: "home",
        components: {
            MuContainer,
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
            openDialog(id) {
                this.dialog.id = id;
                this.dialog.show = true
            }
        }
    }
</script>

<style scoped>
    #dialog {
        border: black solid;
        text-align: left;
        margin-top: 10px;
        padding: 10px;
    }

    #dialog h2 {
        text-align: center;
    }
</style>
