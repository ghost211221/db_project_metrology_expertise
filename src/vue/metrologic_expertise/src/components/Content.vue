<template>
    <div class="content">
        <p v-if="showInitFileDialog">Выберите файл<file-select v-model="file" v-on:input="onFileSelect"></file-select></p>
        <!-- <p v-if="file">{{file.name}}</p> -->
        <!-- <div class="text-document" v-if="showDocumentText" v-html="documentText"></div> -->
        <TextEditModal
          v-bind:text="textModalEdit"
          v-show="isModalVisible "
          v-on:save="closeModal">
        </TextEditModal>
        <div class="text-document" v-if="showDocumentText">
          <div  v-for="item in documentText" :key="item.ref">
            <div
                v-bind:class="item.class"
                v-bind:style="item.style"
                v-bind:ref="item.ref">

              <div v-for="child in item.children" :key="child.ref">
                <p
                  v-if="child.type === 'p'"
                  v-bind:ref="child.ref"
                  v-bind:style="child.style"
                  v-bind:class="child.class"
                  v-on:mousedown="onmousedown"
                  v-on:mouseup="onmouseup">

                  {{ child.text }}
                </p>
              </div>
            </div>

            <!-- <p  class="document-paragraph"
                v-bind:ref="elementIndex(item, 'paragraph')"
                v-bind:class="elementIndex(item, 'paragraph')"
                v-if="item.TYPE == 'paragraph' && item.VALUE[0]"
                v-on:mousedown="onmousedown"
                v-on:mouseup="onmouseup">
                  {{ item.VALUE[0].VALUE }}
            </p> -->
            <!-- <br v-if="item.TYPE == 'paragraph' && !item.VALUE[0]"/> -->
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
      textModalInit: '',
      textModalEdit: '',
      file: null,
      firstEl: '',
      secondEl: '',
      editedTextStruct: {}
    }
  },
  methods: {
    onmousedown (event) {
      this.firstEl = event.target.className
    },
    onmouseup (event) {
      this.secondEl = event.target.className
      this.textModalInit = window.getSelection().toString()
      this.textModalEdit = window.getSelection().toString()
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
    closeModal (editedText) {
      this.isModalVisible = false
      this.editedTextStruct = {
        fistEl: this.firstEl,
        secondEl: this.secondEl,
        initText: this.textModalInit,
        editText: editedText
      }
      console.log(this.editedTextStruct)
      if (this.textModalInit !== editedText) {
        this.$emit('sendStruct', this.editedTextStruct)
      }
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
