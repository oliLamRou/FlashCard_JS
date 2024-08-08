<script setup>
  import {ref, reactive} from 'vue';

  const word = reactive({
    word: "placeholder",
    answer: "answer",
    last: "2024/01/01"
  })

</script>
<template>
  <div class="container">
    <div class="row">
      <div class="col-12 card-wrapper"> 
        <div class="card custom-card">
          <img src="https://picsum.photos/200/200?random=1" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">{{word.word}}</h5>
            <p class="card-text">{{word.answer}}</p>
            <p class="card-text"><small class="text-muted">Last try: {{word.last}}</small></p>
          </div>  
        </div>
      </div>
    </div>
  </div>
</template>

<style>
  .custom-card {
  width: 20%;
  min-width: 200px;
  }
  .card-wrapper {
    display: flex;
    justify-content: center;
  }
</style>