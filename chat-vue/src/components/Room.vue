<template>
    <div>
        <ul>
            <li v-for="room in rooms">{{room.creator.username}} at {{room.date}}</li>
        </ul>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "room",
        data(){
            return {
                rooms: ''
            }
        },
        created(){
            let auth_token = localStorage.getItem('auth_token');
            if(auth_token){
                $.ajaxSetup({
                    headers: {'Authorization': 'Token ' + auth_token}
                })
            }
            this.loadRoom()
        },
        methods: {
            loadRoom(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/room',
                    type: "GET",
                    success: (response) => {
                        this.rooms = response.data.data
                    }
                })
            }
        }

    }
</script>

<style scoped>

</style>
