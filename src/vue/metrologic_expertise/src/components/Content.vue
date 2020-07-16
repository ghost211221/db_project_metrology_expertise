<template>
    <div class="content">
        <p v-if="showInitFileDialog">Выберите файл<file-select v-model="file" v-on:input="onFileSelect"></file-select></p>
        <!-- <p v-if="file">{{file.name}}</p> -->
        <!-- <div class="text-document" v-if="showDocumentText" v-html="documentText"></div> -->
        
        <div class="spinner" v-if="!showInitFileDialog && !showDocumentText">
          <p>
            Идет загрузка документа.<br/>
            <br/>
          </p>
          <Spinner></Spinner>          
         </div>

        <TextEditModal
          v-bind:text="textModalEdit"
          v-show="isModalVisible "
          v-on:save="closeModal"
          v-on:close="closeModal">
        </TextEditModal>
        <div class="text-document" v-if="showDocumentText">
          <div  v-for="item in documentText.data" :key="item.ref">
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
import Spinner from 'vue-simple-spinner'

export default {
  name: 'Content',
  props: [
    'showInitFileDialog',
    'documentText',
    'showDocumentText'
  ],
  components: {
    FileSelect,
    TextEditModal,
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
      ccanCreateSpan: false,
    }
  },
  methods: {
    onmousedown (event) {
      this.firstEl = event.target.className
      console.log(event)
    },
    onmouseup (event) {
      this.secondEl = event.target.className
      this.textModalInit = window.getSelection().toString()
      this.textModalEdit = window.getSelection().toString()
      this.isModalVisible = true
      this.highlight()
    },
    getSelectedRange () {
      if (window.getSelection) {
        const sel = window.getSelection()
        if (sel.getRangeAt && sel.rangeCount) {
          this.selectedRange = sel.getRangeAt(0)
        }
      } else if (document.selection) {
        this.selectedRange = document.selection.createRange()
      }
    },
    surroundSelection () {
      const span = document.createElement('span')
      span.className = 'highlight'
      span.style.backgroundColor = '#D05555'
      // span.addEventListener("click", () => {
      //   console.log('click');
      // })
      if (window.getSelection) {
        var sel = window.getSelection()
        if (sel.rangeCount) {
          var range = this.selectedRange.cloneRange()
          range.surroundContents(span)
          sel.removeAllRanges()
          sel.addRange(range)
        }
      }
    },
    highlight () {
      console.log('try to highlight')
      this.getSelectedRange()
      if (this.selectedRange && this.textModalInit) {
        this.surroundSelection()
      }
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
        document_id: this.documentText.document_id,
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
    onFileSelect () {
      this.canShowSpinner = true
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
      background-color: #AAAAAA;
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
  .page {
      width: 790pt;
      background-color: white;
  }

  .text-hello {
    font-size: 18pt;
    color: #101030;
    height: calc(100vh - 50px);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .text-document {
    overflow: auto;
  }

  .highlight {
    background-color: #D05555;
  }
</style>
