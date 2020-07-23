<template>
  <div>
    <h1
      v-if="type == 'h1'"
      v-bind:ref="ref_"
      :id="id_"
      v-bind:style="style_"
      v-bind:class="class_"
      v-on:mousedown="onmousedown"
      v-on:mouseup="onmouseup">
      {{ text_ }}
    </h1>
    <h2
      v-if="type == 'h2'"
      v-bind:ref="ref_"
      :id="id_"
      v-bind:style="style_"
      v-bind:class="class_"
      v-on:mousedown="onmousedown"
      v-on:mouseup="onmouseup">
      {{ text_ }}
    </h2>
    <h3
      v-if="type == 'h3'"
      v-bind:ref="ref_"
      :id="id_"
      v-bind:style="style_"
      v-bind:class="class_"
      v-on:mousedown="onmousedown"
      v-on:mouseup="onmouseup">
      {{ text_ }}
    </h3>
    <h4
      v-if="type == 'h4'"
      v-bind:ref="ref_"
      :id="id_"
      v-bind:style="style_"
      v-bind:class="class_"
      v-on:mousedown="onmousedown"
      v-on:mouseup="onmouseup">
      {{ text_ }}
    </h4>
    <h5
      v-if="type == 'h5'"
      v-bind:ref="ref_"
      :id="id_"
      v-bind:style="style_"
      v-bind:class="class_"
      v-on:mousedown="onmousedown"
      v-on:mouseup="onmouseup">
      {{ text_ }}
    </h5>
    <h6
      v-if="type == 'h6'"
      v-bind:ref="ref_"
      :id="id_"
      v-bind:style="style_"
      v-bind:class="class_"
      v-on:mousedown="onmousedown"
      v-on:mouseup="onmouseup">
      {{ text_ }}
    </h6>
    <h7
      v-if="type == 'h7'"
      v-bind:ref="ref_"
      :id="id_"
      v-bind:style="style_"
      v-bind:class="class_"
      v-on:mousedown="onmousedown"
      v-on:mouseup="onmouseup">
      {{ text_ }}
    </h7>
    <h8
      v-if="type == 'h8'"
      v-bind:ref="ref_"
      :id="id_"
      v-bind:style="style_"
      v-bind:class="class_"
      v-on:mousedown="onmousedown"
      v-on:mouseup="onmouseup">
      {{ text_ }}
    </h8>
  </div>
</template>

<script>

import { SelectionsMixin } from './SelectionsMixin.js'

export default {

  name: 'HeaderComp',

  mixins: [
      SelectionsMixin
  ],

  props: [
    'text_',
    'ref_',
    'id_',
    'style_',
    'class_',
    'highlightAllow',
    'type'
  ],

  data () {
    return {

    }
  },
  
}
</script>

<style lang="css" scoped>
</style>