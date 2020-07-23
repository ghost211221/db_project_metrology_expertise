<template>
    <div class="text-document">
          <div  v-for="item in docJSON.data" :key="item.ref">
            <div
                v-bind:class="item.class"
                v-bind:style="item.style"
                v-bind:ref="item.ref">

              <div v-for="child in item.children" :key="child.ref">

                <br v-if="child.type == 'br'"/>

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
            </div>
          </div>
        </div>
</template>

<script>

import ParagraphComp from './ParagraphComp.vue'
import HeaderComp from './HeaderComp.vue'
import ImageComp from './ImageComp.vue'
import ListComp from './ListComp.vue'
import TableComp from './TableComp.vue'

export default {

  name: 'MainDocComp',

  props: [
    'docJSON'
  ],

  mixins: [
  ],

  components: {
    ParagraphComp,
    ImageComp,
    HeaderComp,
    ListComp,
    TableComp,
  },

  data () {
    return {      
      sel: null,
      selectedRange: null
    }
  },

  methods: {
    onTextSelected (selectedText, showModal) {
      this.$emit('textSelected', selectedText, showModal)
    },
    onAddedSpan (spanId) {
      this.$emit('addedSpan', spanId)
    }
  },

  mounted () {

  },

  computed: {

  }
}
</script>

<style lang="css" scoped>

  .page {
      width: 790pt;
      background-color: white;
  }
  
  .text-document {
    overflow: auto;
  }

  .highlight {
    background-color: #D05555;
  }
</style>