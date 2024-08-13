<script setup>
	import card from '@/components/card.vue'
</script>

<template>
	<div class="container-fluid">
		<div class="card-wrapper">
			<div class="col">
				<div class="row">
					<card/>
				</div>			
				<div class="row">
					<button type="button" class="btn btn-danger">Bad</button>				
				</div>
				<div class="row">	
					<button type="button" class="btn btn-success">Good</button>
				</div>
			</div>
		</div>
	</div>
</template>

<style>
	.card-wrapper {
		max-width: 500px;
		display: flex;
		justify-content: center;
		margin: 0 auto;
	}
</style>