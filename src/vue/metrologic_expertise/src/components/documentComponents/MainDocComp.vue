<template>
    <div class="text-document">
          <div  v-for="item in docJSON.data" :key="item.ref">
            <div
                v-bind:class="item.class"
                v-bind:style="item.style"
                v-bind:ref="item.ref">

              <div v-for="child in item.children" :key="child.ref">

                <ParagraphComp
                  v-if="child.type == 'p'"
                  :text_="child.text"
                  :ref_="child.ref"
                  :style_="child.style"
                  :class_="child.class"
                  :highlightAllow="canCreateSpan"
                  @textSelected="onTextSelected"
                >
                </ParagraphComp>

              </div>
            </div>
          </div>
        </div>
</template>

<script>

import ParagraphComp from './ParagraphComp.vue'

export default {

  name: 'MainDocComp',

  props: [
    'docJSON',
    'canCreateSpan'
  ],

  mixins: [
  ],

  components: {
    ParagraphComp
  },

  data () {
    return {

    }
  },

  methods: {
    onTextSelected (selectedText, showModal) {
      this.$emit('textSelected', selectedText, showModal)
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