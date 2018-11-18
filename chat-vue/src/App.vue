<template>
    <div id="app">
        <img src="./assets/logo.png" id="logo">
        <router-view/>
    </div>
</template>

<script>
    export default {
        name: 'App',
        // created(){
        //     let auth_token = localStorage.getItem('auth_token');
        //     if(auth_token){
        //         $.ajaxSetup({
        //             headers: {'Authorization': 'Token ' + auth_token}
        //         })
        //     }
        // }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
    #logo{
        max-height: 75px;
    }
</style>
