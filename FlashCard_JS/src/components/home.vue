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
    <v-navigation-drawer :width="322">
      <v-list-item title="My Application" subtitle="Vuetify"></v-list-item>
      <v-divider></v-divider>
      <v-list-item link title="List Item 1"></v-list-item>
      <v-list-item link title="List Item 2"></v-list-item>
      <v-list-item link title="List Item 3"></v-list-item>
    </v-navigation-drawer>
  </v-app>
</template>