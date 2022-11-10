
<template>
  <main>
    <div v-for="item in data">Alloha: {{item.name}}</div>
  </main>
</template>

  <script setup lang="ts">
  import axois from 'axios';
import { ref } from 'vue';
const data = ref([]);

  axois.get('http://localhost:8000/api/rubric/').then((dataresp)=>{
data.value = dataresp.data; 
  })
  .catch(error=>{
    console.log('alloha: ', error); 
   })
  </script>