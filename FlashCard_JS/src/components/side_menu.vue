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
  <v-navigation-drawer :width="322">
    <v-list-item title="My Application" subtitle="Vuetify"></v-list-item>
    <v-divider></v-divider>
    <v-list-item link title="List Item 1"></v-list-item>
    <v-list-item link title="List Item 2"></v-list-item>
    <v-list-item link title="List Item 3"></v-list-item>
  </v-navigation-drawer>
</template>