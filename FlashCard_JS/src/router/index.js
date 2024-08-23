import { createRouter, createWebHistory } from 'vue-router'
import home from '@/components/home.vue'
import generate from '@/components/generate.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes:[
		{name: 'Home', path:'/', component:home},
		{name: 'Generate', path:'/generate', component:generate},
	],
	linkActiveClass:'active'
});

export default router