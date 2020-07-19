<template>
    <div class="text-document">
          <div  v-for="item in docJSON.data" :key="item.ref">
            <div
                v-bind:class="item.class"
                v-bind:style="item.style"
                v-bind:ref="item.ref">

              <div v-for="child in item.children" :key="child.ref">
                <!-- <h1
                  v-if="child.type === 'p'"
                  v-bind:ref="child.ref"
                  v-bind:style="child.style"
                  v-bind:class="child.class"
                  v-on:mousedown="onmousedown"
                  v-on:mouseup="onmouseup">
                  {{ child.text }}
                </h1>
                <h2
                  v-if="child.type === 'p'"
                  v-bind:ref="child.ref"
                  v-bind:style="child.style"
                  v-bind:class="child.class"
                  v-on:mousedown="onmousedown"
                  v-on:mouseup="onmouseup">
                  {{ child.text }}
                </h2>
                <h3
                  v-if="child.type === 'p'"
                  v-bind:ref="child.ref"
                  v-bind:style="child.style"
                  v-bind:class="child.class"
                  v-on:mousedown="onmousedown"
                  v-on:mouseup="onmouseup">
                  {{ child.text }}
                </h3>
                <h4
                  v-if="child.type === 'p'"
                  v-bind:ref="child.ref"
                  v-bind:style="child.style"
                  v-bind:class="child.class"
                  v-on:mousedown="onmousedown"
                  v-on:mouseup="onmouseup">
                  {{ child.text }}
                </h4> -->
                <p
                  v-if="child.type === 'p'"
                  v-bind:ref="child.ref"
                  v-bind:style="child.style"
                  v-bind:class="child.class"
                  v-on:mousedown="onmousedown"
                  v-on:mouseup="onmouseup">
                  {{ child.text }}
                </p>
                <!-- <ul 
                  v-if="child.type === 'ul'"
                  v-bind:ref="child.ref"
                  v-bind:class="child.class"
                  v-bind:style="child.style"
                  v-on:mousedown="onmousedown"
                  v-on:mouseup="onmouseup">
                  
                  <li v-for="_li in child.children" :key="_li.ref"
                    v-if="_li._li === 'li'"
                    v-bind:ref="_li.ref"
                    v-bind:class="_li.class"
                    v-bind:style="_li.style"
                    v-on:mousedown="onmousedown"
                    v-on:mouseup="onmouseup">
                    {{  _li.text }}
                  </li>
                </ul> -->
              </div>
            </div>
          </div>
        </div>
</template>

<script>
// import ParagraphComp from './ParagraphComp.vue'

export default {

  name: 'MainDocComp',
  props: [
    'docJSON'
  ],
  components: {
    // ParagraphComp
  },

  data () {
    return {

    }
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