<script setup>
  import {ref, reactive} from 'vue';

  const word = reactive({
    word: "placeholder",
    answer: "answer",
    last: "2024/01/01"
  })

  var API_KEY = '45426294-13da5b0d5a5784f39d76e7197';
  var URL = "https://pixabay.com/api/?key="+API_KEY+"&q="+encodeURIComponent('red roses');
  $.getJSON(URL, function(data){
  if (parseInt(data.totalHits) > 0)
      $.each(data.hits, function(i, hit){ console.log(hit.pageURL); });
  else
      console.log('No hits');
  });  

</script>
<template>
  <div class="card">
    <div class="card-header">
      <h3>Title</h3>
    </div>
    <!-- <img src="https://picsum.photos/200/200?random=1" class="card-img-top" alt="..."> -->
    <img src="https://pixabay.com/en/blossom-bloom-flower-195893/" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{word.word}}</h5>
      <p class="card-text">{{word.answer}}</p>
      <p class="card-text"><small class="text-muted">Last try: {{word.last}}</small></p>
    </div>  
  </div>
</template>