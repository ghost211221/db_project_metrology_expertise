<template>
    <div>
        <div class="user user-name">
            UserName
        </div>
        <div class="btn btn-new" v-on:click="btn_new_click()">
            Новый документ
        </div>
        <div class="btn btn-load">
            Загрузить документ
        </div>
        <div class="btn btn-template">
            Загрузить шаблон
        </div>
        <div class="btn btn-sign">
            Настроить подпись
        </div>
    </div>
</template>

<script>
export default {
  name: 'Navigation',
  props: [
    'showInitFileDialog'
  ],
  methods: {
    btn_new_click: function () {
      console.log('div clicked')
      this.$emit('toggleInitFileDialog')
      // targetId = event.currentTarget.id
      // console.log(targetId) // returns 'foo'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
    div {
        color: #91A3B5;
    }
    .user {
        font-size: 16pt;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50px;
        width: 200px;
        background-color: #2A2A2A;
    }

    .btn {
        user-select: none; /* supported by Chrome and Opera */
        -webkit-user-select: none; /* Safari */
        -khtml-user-select: none; /* Konqueror HTML */
        -moz-user-select: none; /* Firefox */
        -ms-user-select: none; /* Internet Explorer/Edge */
        font-size: 16pt;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 30px;
        width: 200px;
        margin-top: 5px;
        margin-bottom: 5px;
    }

    .btn:hover {
        background-color: #333333;
    }

</style>
