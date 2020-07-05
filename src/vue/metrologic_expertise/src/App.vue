<template>
    <div id="app">
        <div class="nav-bar">
            <app-navigation v-on:toggleInitFileDialog="toggleInitFileDialog()"/>
        </div>
        <div class="container">
            <div class="header">
                <app-header/>
            </div>
            <div class="content">
                <app-content
                  v-bind:showInitFileDialog="showInitFileDialog"
                  v-bind:documentText="documentHTML"
                  v-bind:showDocumentText="showDocumentText"
                  v-on:onFileSelect="onFileSelect"
                />
            </div>
        </div>
    </div>
</template>

<script>
import Navigation from './components/Navigation.vue'
import Header from './components/Header.vue'
import Content from './components/Content.vue'

import axios from 'axios'

export default {
  name: 'App',
  components: {
    'app-navigation': Navigation,
    'app-header': Header,
    'app-content': Content
  },
  data () {
    return {
      showInitFileDialog: false,
      selectedFile: null,
      API: 'http://127.0.0.1:5000',
      documentHTML: '',
      showDocumentText: false
    }
  },
  methods: {
    getJson () {
      return fetch(this.API + '/healthcheck')
        .then(result => result.json())
        .catch(error => this.$refs.error.setText(error))
    },
    toggleInitFileDialog () {
      this.showInitFileDialog = true
      this.showDocumentText = false
    },
    onFileSelect: function (file) {
      this.showInitFileDialog = false
      this.selectedFile = file
      this.submitFile()
    },
    submitFile () {
      const formData = new FormData()
      formData.append('file', this.selectedFile)
      axios.post(this.API + '/file-upload',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      ).then(data => {
        this.showDocumentText = true
        this.documentHTML = data.data.html
      })
        .catch(function () {
          console.log('FAILURE!!')
        })
    }
  },
  beforeMount () {
    this.getJson()
      .then(data => {
        console.log(data)
      }
      )
  },
  mounted () {
    const fascript = document.createElement('script')
    fascript.setAttribute('crossorigin', 'anonymous')
    document.head.appendChild(fascript)
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
