<template>
  <div class="modal-backdrop">
    <div class="modal">
      <div class="modal-container">
          <div class="text">
            <textarea class="text" v-model="editedText"></textarea>
          </div>
        <div class="btn-panel">
          <button class="btn btn-close" @click="close">Закрыть</button>
          <button class="btn btn-save" @click="save">Применить</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TextEditModal',
  props: ['text'],
  data: function () {
    return {
      editedText: ''
    }
  },
  methods: {
    close () {
      this.$emit('close')
    },
    save () {
      this.$emit('save', this.editedText)
    }
  },
  watch: {
    // эта функция запускается при любом изменении вопроса
    text: function () {
      this.editedText = this.text
    }
  }
}
</script>

<style lang="css" scoped>
  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .modal {
    background-color: #FFE5C3;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    width: 600pt
  }
  textarea {
    font-size: 16pt;
    min-height: 100pt;

    width: 500pt;
    margin-left: 25pt;
    margin-right: 25pt;
  }
  .btn-panel {
    display: flex;
    justify-content: space-between;
  }

  .btn {
    font-size: 12pt;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 40px;
    width: 200px;
    margin: 5px;
    background-color: #4E7C4E;
  }

  .btn:hover {
    background-color: #4A784A;
  }
  .btn:clicked {
    background-color: #3E6C3E;
  }
</style>
