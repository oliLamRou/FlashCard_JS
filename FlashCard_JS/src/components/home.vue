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
  <v-app>
    <side_menu/>
  </v-app>
</template>