<template>
    <div class="main">
        <div class="nav-bar">
            <p>label</p>
        </div>
        <div class="container">            
            <div class="header">

                <div class="btn btn-auth"><center>Войти</center></div>
                <div class="btn btn-reg"><center>Зарегистрироваться</center></div>
                <div class="btn btn-save"><center>Сохранить</center></div>
                <div class="btn btn-send"><center>Генерация таблицы</center></div>
                
            </div>
            <div class="content">
                
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'main',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .main {
        display: flex;
    }

    .header {
        color: #202025;
        background-color: #F5F5F5;
        width: calc(100vw - 200px);
        height: 50px;
        display: flex;
        font-size: 14pt;
    }
    .nav-bar {
        background-color: #202025;
        width: 200px;
        height: 100vh;
        font-size: 24pt;
        color: #707090;
    }
    .content {

    }

    .btn {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 40px;
        width: 200px;
        background-color: #40C050;
        border-radius: 5px;
        margin: 5px;
    }
</style>
