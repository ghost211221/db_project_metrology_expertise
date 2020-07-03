<template>
  <div class="modal">
    <div class="modal-container">
        <div class="text">
          <textarea class="text" v-model="text"></textarea>
        </div>
      <div class="btn-panel">
        <button class="btn btn-close" @click="$emit('close')">Закрыть</button>
        <button class="btn btn-save" @click="save">Применить</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TextEditModal',
  props: ['text'],
  methods: {
    save (e) {
      // this.$emit('input', e.target.value)
      console.log(this.text)
      this.$emit('close')
    }
  }
}
</script>

<style lang="css" scoped>
  .modal {
    background-color: #FFE5C3;
    min-height: 50pt;
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
