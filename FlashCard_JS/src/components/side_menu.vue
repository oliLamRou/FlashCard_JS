<script setup>
  import { ref, watch } from 'vue'
  import { useCards } from '@/stores/cards'
  const store = useCards()
  const choice = ref()
  
  watch(choice, (newChoice) => {
    store.update_category(newChoice)
  })

</script>

<template>
  <div class="p-2 d-grid">
    <div class="input-group mb-3">
      <span class="input-group-text" id="inputGroup-sizing-sm">Categories</span>
      <button class="btn btn-primary" type="button" id="button-addon1">+</button>
    </div>    
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
        class="btn btn-outline-primary btn-lg" 
        :for="'btnradio' + index"
      >
        {{ category }}
      </label>
    </div>
  </div>
</template>