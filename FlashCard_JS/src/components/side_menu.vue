<script setup>
  import { ref, watch } from 'vue'
  import { useDeck } from '@/stores/deck'
  import router from '@/router'

  const store = useDeck()
  const choice = ref()
  
  watch(choice, (newChoice) => {
    store.update_category(newChoice)
  })

  const generate = () => {
    router.push('/generate')
  }

</script>

<template>
  <div class="p-2 d-grid">
    <div 
      class="btn-group-vertical" 
      role="group" 
      aria-label="Basic radio toggle button group"
      v-for="(category, index) in store.categories"
    >
      <input
        type="radio" 
        class="btn-check" 
        name="btnradio" 
        :id="'btnradio' + index"
        autocomplete="off"
        :value="category"
        v-model="choice"

      >
      <label 
        class="btn btn-secondary btn-lg" 
        :for="'btnradio' + index"
      >
        {{ category }}
      </label>
    </div>
    <div class="input-group mt-3">
      <button class="btn btn-outline-secondary" type="button" id="button-addon1" @click="generate">+</button>
    </div>        
  </div>
</template>