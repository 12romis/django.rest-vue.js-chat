<template>
    <div>
        <div v-for="dialog in dialogs">
            <h3>{{dialog.user.username}} (<span class="date">{{dialog.date}}</span>)</h3>
            <p>{{dialog.text}}</p>
        </div>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "dialog",
        props: {
            id: ''
        },
        data() {
            return {
                dialogs: '',
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
        },
        methods: {
            loadDialog() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/dialog',
                    type: 'GET',
                    props: ["id"],
                    data: {
                        room: this.id
                    },
                    success: (response) => {
                        this.dialogs = response.data.data
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
