<script setup>
  import {ref, reactive, onMounted } from 'vue';
  import card from '@/components/card.vue'
  import { useDeck } from '@/stores/deck'

  const store = useDeck()
  const show_answer = ref(false)

  onMounted( async () => {
    await store.load()
  })

  const answer = () => {
    show_answer.value = true
  }

  const bad_answer = () => {
    show_answer.value = false
    store.bad_answer()
  }  

  const good_answer = () => {
    show_answer.value = false
    store.good_answer()
  }

</script>

<template>
  <h1>{{store.category}}</h1>
  <div class="col" v-if="store.topic">
    <div class="row">
      <card :card="store.card" :answer="show_answer"/>
    </div>
    <div class="row mt-3" v-show="!show_answer">
      <div class="d-grid">
          <button 
            type="button" 
            class="btn btn-outline-primary btn-lg"
            @click="answer"
          >Show Answer</button>
      </div>
    </div>
    <div class="row mt-3" v-show="show_answer">
      <div class="col-md-6">
        <div class="d-grid">
          <button 
            type="button" 
            class="btn btn-outline-danger btn-lg"
            @click="bad_answer"
          >Bad</button>
        </div>
      </div>
      <div class="col-md-6">
        <div class="d-grid gap-1">
          <button 
            type="button" 
            class="btn btn-outline-success btn-lg"
            @click="good_answer"
          >Good</button>
        </div>
      </div>
    </div>    
  </div>
</template>