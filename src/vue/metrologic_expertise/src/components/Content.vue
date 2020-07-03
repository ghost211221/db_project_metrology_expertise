<template>
    <div class="content">
        <p>My File Selector: <file-select v-model="file"></file-select></p>
        <p v-if="file">{{file.name}}</p>
        <div class="page page-1">
            <p ref="target">
            предварительных испытаний опытных образцов микросхемы интегральной   1943ВХ015, изготовленных в ходе выполнения ОКР «Разработка и освоение серийного производства микросхемы концентратора интерфейса USB 2.0 и микросхемы преобразования интерфейса USB 2.0 в последовательный и параллельный интерфейсы», шифр «Интерфейс-И5».
            </p>
        </div>
        <TextEditModal :text="textModal" v-if="showModal" @close="showModal = false"></TextEditModal>
    </div>
</template>

<script>
import FileSelect from './FileSelect.vue'
import TextEditModal from './TextEditModal'
export default {
  name: 'Content',
  components: {
    FileSelect,
    TextEditModal
  },
  data () {
    return {
      showModal: false,
      textModal: ''
    }
  },
  methods: {
    testFunction () {
      this.textModal = window.getSelection().toString()
      console.log(this.textModal)
      this.showModal = true
    }
  },
  mounted () {
    document.addEventListener('mouseup', event => {
      if (event.target === this.$refs.target || event.target.contains(this.$refs.target)) {
        this.testFunction()
      }
    })
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
</style>
