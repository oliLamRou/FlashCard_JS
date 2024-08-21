import { defineStore } from "pinia";
import axios from 'axios'

export const useCards = defineStore('pairForm',{
  state:() => ({
    deck: [],
    category: null,
    current: 0
  }),
  getters: {
    categories() {
      return new Set(this.deck.map(item => item.category))
    },
    cards() {
      return this.deck.filter(card => card.category === this.category)
    },
    card() {
      return this.cards[this.current]
    },
  },
  actions:{
    async load() {
      try {
        const responce = await axios.get('http://localhost:5003/get_words')
        this.deck = responce.data
      }
      catch(error) {
        console.log(error)
      }
    },
    draw_card() {
      this.current =  Math.floor(Math.random() * this.cards.length)
    },    
    update_category(newCategory) {
      this.category = newCategory
      this.draw_card()
    },
    bad_answer(newCategory) {
      this.draw_card()
    },
    good_answer(newCategory) {
      this.draw_card()
    }
  },
})