<script setup>
  
</script>

<template>
  <div class="p-5">
    <div class="input-group mb-3">
      <span class="input-group-text" id="inputGroup-sizing-sm">Categories</span>
      <button class="btn btn-outline-secondary" type="button" id="button-addon1">+</button>
    </div>    
    <div class="btn-group-vertical" role="group" aria-label="Basic radio toggle button group">
      <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
      <label class="btn btn-outline-light" for="btnradio1">Radio 1</label>

      <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
      <label class="btn btn-outline-light" for="btnradio2">Radio 2</label>

      <input type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
      <label class="btn btn-outline-light" for="btnradio3">Radio 3</label>
    </div>
  </div>
  
</template>
