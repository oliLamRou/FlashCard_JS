<script setup>
  import {ref, reactive, onMounted } from 'vue';
  import card from '@/components/card.vue'
  import { useCards } from '@/stores/cards'

  const store = useCards()

</script>

<template>
  <div class="col">
    <div class="row">
      <card :card="store.cards"/>
    </div>
    <div class="row mt-3">
      <div class="col-md-6">
        <div class="d-grid">
          <button type="button" class="btn btn-danger btn-lg">Bad</button>
        </div>
      </div>
      <div class="col-md-6">
        <div class="d-grid gap-1">
          <button type="button" class="btn btn-success btn-lg">Good</button>
        </div>
      </div>
    </div>    
  </div>
</template>