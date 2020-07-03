<template>
    <div id="app">
        <app-main/>
    </div>
</template>

<script>

import main from './components/main.vue'

export default {
    name: 'App',
    components: {
        "app-main": main,
    },
}
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
    }
    * {        
        margin: 0px;
        padding: 0px;
    }
</style>
