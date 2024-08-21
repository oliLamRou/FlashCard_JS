<script setup>
  import { ref, reactive } from 'vue'
  const userInput = reactive({
    new: false
  })

  const toggle = () => {
    userInput.new = !userInput.new
  }
</script>

<template>
  <form>
    <div class="input-group mb-3">
      <button class="btn btn-outline-secondary" type="button">Button</button>
      <select class="form-select" id="inputGroupSelect03" aria-label="Example select with button addon">
        <option selected>Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
      </select>
    </div>
    <div class="mb-3">
      <label for="newCardQuestion" class="form-label">Question</label>
      <input type="text" class="form-control" id="newCardQuestion" placeholder="dog">
    </div>    
    <div class="mb-3">
      <label for="newCardAnswer" class="form-label">Answer</label>
      <input type="text" class="form-control" id="newCardAnswer" placeholder="chien">
    </div>
    <button type="button" class="btn btn-primary">Submit</button>
    <button type="button" class="btn btn-secondary">clear</button>
  </form>
</template>
