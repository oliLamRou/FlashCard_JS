<script setup>
  import { ref, watch } from 'vue'
  import { useDeck } from '@/stores/deck'
  import router from '@/router'

  const store = useDeck()
  const choice = ref()
  
  watch(choice, (newChoice) => {
    store.update_topic(newChoice)
  })

  const generate = () => {
    router.push('/generate')
  }

</script>

<template>
  <h1>Topics</h1>
  <div class="p-2 d-grid">
    <div 
      class="btn-group-vertical" 
      role="group" 
      aria-label="Basic radio toggle button group"
      v-for="(topic, index) in store.topics"
    >
      <input
        type="radio" 
        class="btn-check" 
        name="btnradio" 
        :id="'btnradio' + index"
        autocomplete="off"
        :value="topic"
        v-model="choice"

      >
      <label 
        class="btn btn-secondary btn-lg clean_text" 
        :for="'btnradio' + index"
      >
        {{ topic }}
      </label>
    </div>
    <div class="input-group mt-3">
      <button class="btn btn-outline-secondary" type="button" id="button-addon1" @click="generate">+</button>
    </div>        
  </div>
</template>