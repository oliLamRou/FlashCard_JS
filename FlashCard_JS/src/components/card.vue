<script setup>
  import {ref, reactive, onMounted, watch } from 'vue';

  const props = defineProps({
      card: {
        type: Object,
        require: true
      },
      answer: {
        type: Boolean,
      }
  })

</script>
<template>
  <div class="card mb-2">
    <div class="row g-0">
      <div class="col-md-5 p-1">
        <img src="https://picsum.photos/200/200?random=1" class="card-img-top" alt="...">
      </div>
      <div class="col-md-7">
        <div class="card-body">
          <h3 class="card-title clean_text">{{props.card.question}}</h3>
          <h3 class="card-text clean_text" v-show="props.answer">
            <b>{{props.card.answer}}</b>
          </h3>
          <p class="card-text"><small class="text-muted">Last try: {{props.card.last}}</small></p>
        </div>
      </div>
    </div>
  </div>  
</template>