<template>
  
  <table
    :ref="ref_"
    :id="id_"
    :style="style_"
    :class="class_"
  >
    <tr v-for="row in children_" :key="row.id">
      <td v-for="cell in row.children"
        :key="cell.id"
        :ref_="cell.ref"
        :id_="cell.id"
        :style_="cell.style"
        :class_="cell.class"
        v-on:mousedown="onmousedown"
        v-on:mouseup="onmouseup"
      >
        
        <div v-for="child in cell.children" :key="child.ref">

          <ParagraphComp
            v-if="child.type == 'p'"
            :text_="child.text"
            :ref_="child.ref"
            :id_="child.id"
            :style_="child.style"
            :class_="child.class"
            @addedSpan="onAddedSpan"
            @textSelected="onTextSelected"
            @textHighlighted="$emit('textHighlighted')"
          />

          <ListComp
            v-if="child.type == 'ul'"
            :children_="child.children"
            :ref_="child.ref"
            :id_="child.id"
            :style_="child.style"
            :class_="child.class"
            @addedSpan="onAddedSpan"
            @textSelected="onTextSelected"
            @textHighlighted="$emit('textHighlighted')"
          />

          <TableComp
            v-if="child.type == 'table'"
            :children_="child.children"
            :ref_="child.ref"
            :id_="child.id"
            :style_="child.style"
            :class_="child.class"
            @addedSpan="onAddedSpan"
            @textSelected="onTextSelected"
            @textHighlighted="$emit('textHighlighted')"
          />

          <HeaderComp
            v-if="child.type.startsWith('h')"
            :type="child.type"
            :text_="child.text"
            :ref_="child.ref"
            :id_="child.id"
            :style_="child.style"
            :class_="child.class"
            @addedSpan="onAddedSpan"
            @textSelected="onTextSelected"
            @textHighlighted="$emit('textHighlighted')"
          />

          <ImageComp
            v-if="child.type == 'img'"
            :src_="child.image"
            :ref_="child.ref"
            :style_="child.style"
            :class_="child.class"
          />

        </div>

      </td>
    </tr>
    
  </table>


<!--   <ul
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
  </ul> -->
</template>

<script>

import ParagraphComp from './ParagraphComp.vue'
import HeaderComp from './HeaderComp.vue'
import ImageComp from './ImageComp.vue'
import ListComp from './ListComp.vue'
import TableComp from './TableComp.vue'

import { SelectionsMixin } from './SelectionsMixin.js'

export default {

  name: 'TableComp',

  mixins: [
      SelectionsMixin
  ],

  components: {
    ParagraphComp,
    ImageComp,
    HeaderComp,
    ListComp,
    TableComp,
  },

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

  methods: {    
    onTextSelected (selectedText, showModal) {
      this.$emit('textSelected', selectedText, showModal)
    },
    onAddedSpan (spanId) {
      this.$emit('addedSpan', spanId)
    }
  }
  
}
</script>

<style lang="css" scoped>
</style>