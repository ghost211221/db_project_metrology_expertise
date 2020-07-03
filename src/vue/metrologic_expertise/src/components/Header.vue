<template>
    <div>
        <div class="auth">
            <div class="btn btn-login">
                Войти
            </div>
            <div class="btn btn-register">
                Регистрация
            </div>
            <div class="btn btn-logout">
                Выход
            </div>
        </div>
        <div class="document">
            <div class="btn btn-save">
                Сохранить
            </div>
            <div class="btn btn-report">
                Отчет
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
    div {
        color: #D9EBFD;;
        display: flex;
        justify-content: space-between;
    }

    .btn {
        font-size: 16pt;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 40px;
        width: 200px;
        margin: 5px;
        background-color: #038803;
    }

    .btn:hover {
        background-color: #139813;
    }

</style>
