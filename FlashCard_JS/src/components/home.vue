<script setup>
	import cards from '@/components/cards.vue'
	import side_menu from '@/components/side_menu.vue'
</script>

<template>
  <div class="app-container">
    <div class="col-md-4 sidebar">
      <side_menu/>    
    </div>
    <div class="col-md-8 main-content p-5">
      <cards/>    
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