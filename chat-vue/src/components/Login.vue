<template>
    <div>
        <input v-model="login" type="text" placeholder="Login" />
        <input v-model="password" type="password" placeholder="Password" />
        <button @click="setLogin">Login</button>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "login",
        data(){
            return {
                login: '',
                password: ''
            }
        },
        methods: {
            setLogin(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/token/create',
                    type: 'POST',
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        // sessionStorage.setItem('auth_token', response.data.attributes.auth_token);
                        localStorage.setItem('auth_token', response.data.attributes.auth_token)
                        this.$router.push({name: 'home'})
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
        }
    }
</script>

<style scoped>

</style>
