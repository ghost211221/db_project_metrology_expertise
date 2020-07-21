<template>
  <p
    v-bind:ref="ref_"
    v-bind:style="style_"
    v-bind:class="class_"
    v-on:mousedown="onmousedown"
    v-on:mouseup="onmouseup">
    {{ text_ }}
  </p>
</template>

<script>

import { SelectionsMixin } from './SelectionsMixin.js'

export default {

  name: 'ParagraphComp',

  mixins: [
      SelectionsMixin
  ],

  props: [
    'text_',
    'ref_',
    'style_',
    'class_',
    'highlightAllow'
  ],

  data () {
    return {

    }
  },
  
}
</script>

<style lang="css" scoped>
</style>