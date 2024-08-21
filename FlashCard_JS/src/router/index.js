import { createRouter, createWebHistory } from 'vue-router'
import home from '@/components/home.vue'
import add_cards from '@/components/add_cards.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes:[
		{name: 'Home', path:'/', component:home},
		{name: 'New', path:'/new', component:add_cards},
	],
	linkActiveClass:'active'
});

export default router