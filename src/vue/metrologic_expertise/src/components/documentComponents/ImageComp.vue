<template>
  <img 
    :src="`data:image/png;base64,${src_}`"
    alt=""
    :ref="ref_"
    :style="style_"
    :class="class_"
  />
</template>

<script>

export default {

  name: 'ImageComp',

  mixins: [
  ],

  props: [
    'src_',
    'ref_',
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