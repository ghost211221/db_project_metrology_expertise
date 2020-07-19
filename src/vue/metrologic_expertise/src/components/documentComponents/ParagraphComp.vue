<template>
  <p
    v-bind:ref="ref"
    v-bind:style="style"
    v-bind:class="class"
    v-on:mousedown="$emit(onmousedown)"
    v-on:mouseup="$emit(onmouseup)">
    {{ text }}
  </p>
</template>

<script>
import SelectionsMixin from './SelectionsMixin.js';
export default {

  name: 'ParagraphComp',
  props: [
    'text'
    'ref',
    'style',
    'class'
  ],

  data () {
    return {

    }
  },
  mixins: [
      SelectionsMixin,
  ]
}
</script>

<style lang="css" scoped>
</style>