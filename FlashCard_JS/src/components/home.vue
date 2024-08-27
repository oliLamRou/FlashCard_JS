<script setup>
  import {onMounted } from 'vue';
	import cards from '@/components/cards.vue'
  import score from '@/components/score.vue'
	import side_menu from '@/components/side_menu.vue'
  import { useDeck } from '@/stores/deck'
  const store = useDeck()

  onMounted( async () => {
    await store.load()
  })

</script>

<template>
  <div class="app-container">
    <div class="col-md-4 sidebar">
      <side_menu/>
    </div>
    <div class="col-md-8 main-content p-5" v-if="store.topic">
      <cards v-if="store.stack.length > 0"/>
      <score v-else/>
    </div>
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
  height: 100vh; /* Full viewport height */
}

.sidebar {
  background-color: #2c3e50;
}

.main-content {
  background-color: #ecf0f1; 
}
</style>