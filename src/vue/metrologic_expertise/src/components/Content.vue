<template>
    <div class="content">
        <p v-if="showInitFileDialog">Выберите файл<file-select v-model="file" v-on:input="onFileSelect"></file-select></p>
        <!-- <p v-if="file">{{file.name}}</p> -->
        <!-- <div class="text-document" v-if="showDocumentText" v-html="documentText"></div> -->
        <TextEditModal
          :text="textModal"
          v-show="isModalVisible "
          @close="closeModal">
        </TextEditModal>
        <div class="text-document" v-if="showDocumentText">
          <div  v-for="item in documentText" :key="item.type">
            <!-- {{ item.TYPE }} -->
            <p  class="document-paragraph"
                v-bind:ref="elementIndex(item, 'paragraph')"
                v-bind:class="elementIndex(item, 'paragraph')"
                v-if="item.TYPE == 'paragraph' && item.VALUE[0]"
                v-on:mouseup="testFunction">
                  {{ item.VALUE[0].VALUE }}
            </p>
            <br v-if="item.TYPE == 'paragraph' && !item.VALUE[0]"/>
          </div>
        </div>
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
      isModalVisible: false,
      textModal: '',
      file: null
    }
  },
  methods: {
    testFunction () {
      this.textModal = window.getSelection().toString()
      this.isModalVisible = true
    },
    canShowHello () {
      return !this.showInitFileDialog && !this.documentText && !this.file
    },
    canShowFileDialog () {
      return this.showInitFileDialog
    },
    showModal () {
      this.isModalVisible = true
    },
    closeModal () {
      this.isModalVisible = false
    },
    onFileSelect (fileName) {
      this.$emit('onFileSelect', this.file)
    },
    elementIndex (element, type) {
      return type + '-' + this.documentText.indexOf(element)
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
