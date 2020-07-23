<template>
  <ul
    :ref="ref_"
    :id="id_"
    :style="style_"
    :class="class_"
  >
    <li v-for="child in children_" :key="child.id"
      :ref_="child.ref"
      :id_="child.id"
      :style_="child.style"
      :class_="child.class"
      v-on:mousedown="onmousedown"
      v-on:mouseup="onmouseup"
    >
      {{ child.text }}
    </li>
  </ul>
</template>

<script>

import { SelectionsMixin } from './SelectionsMixin.js'

export default {

  name: 'ListComp',

  mixins: [
      SelectionsMixin
  ],

  props: [
    'children_',
    'ref_',
    'id_',
    'style_',
    'class_'
  ],

  data () {
    return {

    }
  },
  
}
</script>

<style lang="css" scoped>
</style>