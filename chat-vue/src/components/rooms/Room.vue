<template>
    <div>
        <mu-paper v-for="room in rooms" class="demo-paper room" :z-depth="3">
            <p @click="openDialog(room.id)" class="room-title">
                Room {{room.id}} by {{room.creator.username}} at {{room.date}}.
            </p>
            <div class="room-members">
                 Members of room:
                <ul class="invited">
                    <li v-for="u in room.invited">{{u.username}}</li>
                </ul>
            </div>
        </mu-paper>
    </div>
</template>

<script>
    export default {
        name: "room",
        components: {},
        data() {
            return {
                rooms: '',
            }
        },
        created() {
            let auth_token = localStorage.getItem('auth_token');
            if (auth_token) {
                $.ajaxSetup({
                    headers: {'Authorization': 'Token ' + auth_token}
                })
            }
            this.loadRoom()
        },
        methods: {
            loadRoom() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/room',
                    type: "GET",
                    success: (response) => {
                        this.rooms = response.data.data
                    }
                })
            },
            openDialog(id) {
                this.$emit("openDialog", id)
            }
        }

    }
</script>

<style scoped>
    p.room-title {
        cursor: pointer;
        font-weight: bold;
        margin-bottom: 0;
    }

    .room-members {
        text-align: left;
        padding-left: 5px;
    }

    .room {
        text-align: left;
        padding-left: 5px;
        list-style: none;
        margin: 10px;
    }
    ul.invited{
        list-style: circle;
        margin-top: 0;
    }
</style>
