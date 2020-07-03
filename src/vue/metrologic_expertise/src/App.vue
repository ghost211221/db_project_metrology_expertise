<template>
    <div id="app">
        <div class="nav-bar">
            <app-navigation/>
        </div>
        <div class="container">
            <div class="header">
                <app-header/>
            </div>
            <div class="content">
                <app-content/>
            </div>
        </div>
    </div>
</template>

<script>
import Navigation from './components/Navigation.vue'
import Header from './components/Header.vue'
import Content from './components/Content.vue'

export default {
  name: 'App',
  components: {
    'app-navigation': Navigation,
    'app-header': Header,
    'app-content': Content
  },
  methods: {
    getJson () {
      console.log('sending request')
      return fetch('http://127.0.0.1:5000/healthcheck')
        .then(result => result.json())
        .catch(error => this.$refs.error.setText(error))
    }
  },
  beforeMount () {
    this.getJson()
      .then(data => {
        console.log(data)
      }
      )
  }
}
</script>

<style lang="scss">
    * {
        margin: 0px;
        padding: 0px;
    }
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        display: flex;
    }

    .nav-bar {
        width: 200px;
        height: 100vh;
        background-color: #222222;
        display: flex;
    }

    .container {
        width: calc(100vw - 200px);
        height: 100vh;
    }

    .header {
        height: 50px;
        width: calc(100vw - 200px);
        background-color: #DDDDDD;
    }

    .content {
        height: calc(100vh - 50px);
        width: calc(100vw - 200px);
    }
</style>
