<template>
    <div class="content">
        <p v-if="showInitFileDialog">Выберите файл<file-select v-model="file" v-on:input="onFileSelect"></file-select></p>
        <!-- <p v-if="file">{{file.name}}</p> -->
        <div class="text-document" v-if="showDocumentText" v-html="documentText" ref="target"></div>
        <div class="text-hello" v-if="canShowHello()">
          <p>
            Добро пожаловать! <br/>
            Для начала работы нажмите на кнопку "Новый документ" для загрузки нового документа. <br/>
            Или нажмите кнопку "Загрузить документ" для выбора одного из старых документов. <br/>
          </p>
        </div>
        <TextEditModal :text="textModal" v-if="showModal" @close="$emit('showModal = false')"></TextEditModal>
    </div>
</template>

<script>
import FileSelect from './FileSelect.vue'
import TextEditModal from './TextEditModal'
export default {
  name: 'Content',
  props: [
    'showInitFileDialog',
    'documentText',
    'showDocumentText'
  ],
  components: {
    FileSelect,
    TextEditModal
  },
  data () {
    return {
      showModal: false,
      textModal: '',
      file: null
    }
  },
  methods: {
    testFunction () {
      console.log('text selected')
      this.textModal = window.getSelection().toString()
      this.showModal = true
    },
    canShowHello () {
      return !this.showInitFileDialog && !this.documentText && !this.file
    },
    canShowFileDialog () {
      return this.showInitFileDialog
    },
    onFileSelect (fileName) {
      this.$emit('onFileSelect', this.file)
    }
  },
  mounted () {
    document.addEventListener('mouseup', event => {
      if (event.target === this.$refs.target || event.target.contains(this.$refs.target)) {
        console.log('connect test fuction')
        this.testFunction()
      }
    })
    document.querySelectorAll('p, li').forEach(item => {
      item.addEventListener('mouseup', event => {
        console.log(item)
        this.testFunction()
      })
    })
  },
  watch: {
    documentText: function (newVal, oldVal) { // watch it
      console.log(newVal, oldVal)
      console.log(document.querySelectorAll('p, li'))
      document.querySelectorAll('p, li').forEach(item => {
        item.addEventListener('mouseup', event => {
          console.log(item)
          this.testFunction()
        })
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .content {
      color: black;
      font-size: 12pt;
      display: flex;
      flex-direction: column;
      align-items: center;
  }
  .page {
      width: 790pt;
  }

  .text-hello {
    font-size: 18pt;
    color: #101030;
    height: calc(100vh - 50px);
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
