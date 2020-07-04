<template>
    <label class="file-select">
        <div class="select-button">
            <!-- <span >Текущий файл: {{value.name}}</span> -->
            <span >Выберите файл</span>
        </div>
        <input type="file" @change="handleFileChange"/>
    </label>
</template>

<script>
export default {
  props: {
    value: File
  },

  methods: {
    handleFileChange (e) {
      const fileExt = e.target.files[0].name.match(/\.([0-9A-Za-z_]+)$/)
      for (var ext of fileExt) {
        if (ext === '.docx') {
          this.$emit('input', e.target.files[0])
          return
        }
      }
      alert('Выбран не верный файл. Допускаются только файлы в формате .docx')
    }
  }
}
</script>

<style scoped>
    .file-select > .select-button {
        padding: 1rem;

        color: white;
        background-color: #2EA169;

        border-radius: .3rem;

        text-align: center;
        font-weight: bold;
    }

    .file-select :hover {
      background-color: #35A977;
    }

    .file-select > input[type="file"] {
        display: none;
    }
</style>
