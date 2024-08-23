<script setup>
  import { ref, reactive } from 'vue'
  import { useDeck } from '@/stores/deck'
  import router from '@/router'
  
  const store = useDeck()
  const userInput = reactive({
    topic: "animal",
    amount: 5,
    languageA: "english",
    languageB: "french",
  })

  const submit = () => {
    store.generate(userInput)
    router.push('/')
  }
  
</script>

<template>
  <form>
    <div class="mb-3">
      <label for="newCardQuestion" class="form-label">Topic</label>
      <input type="text" class="form-control" id="newCardQuestion" v-model="userInput.topic">
    </div> 
    <div class="mb-3">
      <label for="newCardQuestion" class="form-label">Amount</label>
      <input type="number" class="form-control" id="newCardQuestion" v-model="userInput.amount">
    </div>    
    <div class="mb-3">
      <label for="newCardQuestion" class="form-label">LanguageA</label>
      <input type="text" class="form-control" id="newCardQuestion" v-model="userInput.languageA">
    </div>    
    <div class="mb-3">
      <label for="newCardAnswer" class="form-label">LanguageB</label>
      <input type="text" class="form-control" id="newCardAnswer" v-model="userInput.languageB">
    </div>
    <button type="button" class="btn btn-primary" @click="submit">Submit</button>
    <button type="button" class="btn btn-secondary">clear</button>
  </form>
</template>
