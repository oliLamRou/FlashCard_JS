import { defineStore } from "pinia";
import axios from 'axios'

export const useCards = defineStore('pairForm',{
  state:() => ({
    cards: [],
    category: null
  }),
  getters: {
    categories() {
      return new Set(this.cards.map(item => item.category))
    }
  },
  actions:{
    async load() {
      try {
        const responce = await axios.get('http://localhost:5003/get_words')
        this.cards = responce.data
      }
      catch(error) {
        console.log(error)
      }
    },
    update_category(newCategory) {
      this.category = newCategory
    },
    bad_answer(newCategory) {
      // this.category = newCategory
    },
    good_answer(newCategory) {
      // this.category = newCategory
    }
  },
})