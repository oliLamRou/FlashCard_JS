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
  <div class="col">
    <h3>Good</h3>
    <ul>
      <li v-for="good in store.good">
        <b>{{good.question}}: {{good.answer}}({{good.score}})</b>
      </li>
    </ul>
    <h3>Bad</h3>
    <ul>
      <li v-for="bad in store.bad">
        <b>{{bad.question}}: {{bad.answer}}({{bad.score}})</b>
      </li>
    </ul>
  </div>
</template>