<script setup>
	import cards from '@/components/cards.vue'
	import side_menu from '@/components/side_menu.vue'
</script>

<template>
  <div class="app-container">
    <aside class="sidebar">
      <side_menu/>
    </aside>
    <main class="main-content">
      <cards class="p-5"/>
    </main>
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
  height: 100vh; /* Full viewport height */
}

.sidebar {
  width: 400px;
  background-color: #2c3e50; /* Example sidebar background */
  color: white;
  padding: 20px;
  box-sizing: border-box;
}

.main-content {
	width: 100%;
  background-color: #ecf0f1; /* Example main content background */
  padding: 20px;
  box-sizing: border-box;
  overflow-y: auto; /* Adds scrolling if content overflows */
}
</style>