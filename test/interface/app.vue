<template>
  <div>
    <p>My File Selector: <file-select v-model="file"></file-select></p>
    <p v-if="file">{{file.name}}</p>
  </div>
</template>

<script>
import FileSelect from './FileSelect.vue'

export default {
  components: {
    FileSelect
  },

  data() {
    return {
      file: null
    }
  },
  methods: {
    getJson(url){
      return fetch(url)
      .then(result => console.log(result))
      .catch(error => this.$refs.error.setText(error));
    }
  }
</script>


fetch("https://jokes-database.p.rapidapi.com/", {
    "method": "GET",
    "headers": {
        "x-rapidapi-host": "jokes-database.p.rapidapi.com",
        "x-rapidapi-key": this.apiKey
    }
})
.then(response => { 
    if(response.ok){
        return response.json()    
    } else{
        alert("Server returned " + response.status + " : " + response.statusText);
    }                
})
.then(response => {
    this.result = response.body; 
    this.responseAvailable = true;
})
.catch(err => {
    console.log(err);
});