<template>
  <div>
    <p>My File Selector: <file-select v-model="file"></file-select></p>
    <p v-if="file">{{file.name}}</p>
  </div>
</template>

<script>
import FileSelect from './FileSelect.vue'

export default {
  components: {
    FileSelect
  },

  data() {
    return {
      file: null
    }
  }
}
</script>