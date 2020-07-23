<template>
    <div class="content">
        <div class="content serverError" v-if="serverError">
          Нет связи с сервером.
          Повторите попытку позже.
        </div>
        <p v-if="showInitFileDialog">Выберите файл<file-select v-model="file" v-on:input="onFileSelect"></file-select></p>
        
        <div class="spinner" v-if="!showInitFileDialog && !showDocumentText && !canShowHello()">
          <p>
            Идет загрузка документа.<br/>
            <br/>
          </p>
          <Spinner></Spinner>          
        </div>

        <MainDocComp v-if="showDocumentText"
          :docJSON="documentText"
          :canCreateSpan="canCreateSpan"
          @addedSpan="onAddedSpan"
          @textSelected="onTextSelected"
          @textHighlighted="$emit('textHighlighted')"

        ></MainDocComp>

        <TextEditModal
          v-bind:text="textModalEdit"
          v-show="isModalVisible"
          v-on:save="saveModal"
          v-on:close="closeModal">
        </TextEditModal>
        
        <div class="text-hello" v-if="canShowHello()">
          <p>
            Добро пожаловать! <br/>
            Для начала работы нажмите на кнопку "Новый документ" для загрузки нового документа. <br/>
            Или нажмите кнопку "Загрузить документ" для выбора одного из старых документов. <br/>
          </p>
        </div>
    </div>
</template>

<script>
import FileSelect from './FileSelect.vue'
import TextEditModal from './TextEditModal'
import MainDocComp from './documentComponents/MainDocComp'
import Spinner from 'vue-simple-spinner'

export default {
  name: 'Content',
  props: [
    'showInitFileDialog',
    'documentText',
    'showDocumentText',
    'serverError'
  ],
  components: {
    FileSelect,
    TextEditModal,
    MainDocComp,
    Spinner
  },
  data () {
    return {
      isModalVisible: false,
      textModalInit: '',
      textModalEdit: '',
      file: null,
      firstEl: '',
      secondEl: '',
      editedTextStruct: {},
      selectedRange: null,
      canCreateSpan: false,
      lastSpanId: ''
    }
  },
  methods: {
    onFileSelect () {
      this.canShowSpinner = true
      this.$emit('onFileSelect', this.file)
    },
    canShowHello () {
      return !this.showInitFileDialog && !this.documentText && !this.file
    },
    canShowFileDialog () {
      return this.showInitFileDialog
    },
    onTextSelected (selectedText, showModal) {
      if (showModal && selectedText !== '') {
        this.isModalVisible = showModal        
      }
      this.textModalInit = selectedText
      this.textModalEdit = selectedText
    },
    showModal () {
      this.isModalVisible = true
    },
    saveModal (editedText) {
      this.isModalVisible = false
      this.editedTextStruct = {
        document_id: this.documentText.document_id,
        fistEl: this.firstEl,
        secondEl: this.secondEl,
        initText: this.textModalInit,
        editText: editedText
      }
      if (this.textModalInit !== editedText) {
        this.$emit('sendStruct', this.editedTextStruct)
      } else {
        this.deleteSpan()
      }
    },
    closeModal () {
      this.isModalVisible = false  
      this.deleteSpan()
    },
    textHighlighted () {
    },
    onAddedSpan (spanId) {
      this.lastSpanId = spanId
    },
    deleteSpan () {
      document.getElementById(this.lastSpanId).replaceWith(document.getElementById(this.lastSpanId).innerText)
    }
  },
  mounted () {
  },
  watch: {
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
      background-color: #AAAAAA;
  }

  .serverError {
    justify-content: center;
    font-size: 24pt;
    background-color: #AA3030;
    height: 10vh;
    width: calc(100vw - 200px);
  }
  
  .spinner {    
    font-size: 18pt;
    color: #101030;
    height: calc(100vh - 50px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
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
