<template>
    <div>
        <div v-for="dialog in dialogs">
            <h3>{{dialog.user.username}} (
                <small class="date">{{dialog.date}}</small>
                )
            </h3>
            <p>{{dialog.text}}</p>
        </div>
        <br>
        <!--<hr>-->
        <mu-text-field v-model="msg" placeholder="Write here your message to the chat"
                       multi-line :rows="2" :rows-max="8" full-width>
        </mu-text-field>
        <mu-flex justify-content="center" align-items="center">
            <mu-button round color="success" @click="sendMsg">Send message</mu-button>
        </mu-flex>
    </div>
</template>

<script>
    export default {
        name: "dialog",
        props: {
            id: ''
        },
        data() {
            return {
                dialogs: '',
                msg: ''
            }
        },
        created() {
            let auth_token = localStorage.getItem('auth_token');
            if (auth_token) {
                $.ajaxSetup({
                    headers: {'Authorization': 'Token ' + auth_token}
                })
            }
            this.loadDialog();
            setInterval(() => {
                this.loadDialog();
            }, 5000);
        },
        methods: {
            loadDialog() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/dialog/',
                    type: 'GET',
                    data: {
                        room: this.id
                    },
                    success: (response) => {
                        this.dialogs = response.data.data
                    }
                })
            },
            sendMsg() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/dialog/',
                    type: 'POST',
                    data: {
                        room: this.id,
                        text: this.msg
                    },
                    success: (response) => {
                        this.loadDialog()
                    },
                    error: (response) => {
                        var errors = '';
                        response.responseJSON.errors.forEach(function(error){
                            errors += error['detail']
                        });
                        alert(errors);
                    }
                })
            }
        },
        watch: {
            id: {
                handler(val, oldVal) {
                    this.loadDialog();
                }

            }
        }
    }
</script>

<style scoped>
    .date {

    }
</style>
