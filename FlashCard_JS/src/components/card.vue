<script setup>
  import {ref, reactive, onMounted } from 'vue';

  const props = defineProps({
    card: Object,
    require: true
  })

  // const word = reactive({
  //   word: "placeholder",
  //   answer: "answer",
  //   last: "2024/01/01"
  // })

  // var API_KEY = '45426294-13da5b0d5a5784f39d76e7197';
  // var URL = "https://pixabay.com/api/?key="+API_KEY+"&q="+encodeURIComponent('red roses');
  // $.getJSON(URL, function(data){
  // if (parseInt(data.totalHits) > 0)
  //     $.each(data.hits, function(i, hit){ console.log(hit.pageURL); });
  // else
  //     console.log('No hits');
  // });

</script>
<template>
  <div class="card">
    <div class="card-header">
      <h3>Category</h3>
    </div>
    <img src="https://picsum.photos/200/200?random=1" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{props.card.question}}</h5>
      <p class="card-text">{{props.card.answer}}</p>
      <p class="card-text"><small class="text-muted">Last try: {{props.card.last}}</small></p>
    </div>  
  </div>
</template>