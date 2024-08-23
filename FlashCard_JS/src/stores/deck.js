import { defineStore } from "pinia";
import axios from 'axios'

export const useDeck = defineStore('storeDeck',{
  state:() => ({
    deck: [],
    topic: null,
    current: 0
  }),
  getters: {
    topics() {
      return new Set(this.deck.map(item => item.topic))
    },
    cards() {
      return this.deck.filter(card => card.topic === this.topic)
    },
    card() {
      return this.cards[this.current]
    },
  },
  actions:{
    async load() {
      try {
        const responce = await axios.get('http://localhost:5003/load_deck')
        this.deck = responce.data
      }
      catch(error) {
        console.log(error)
      }
    },
    async add() {
      try {
        const responce = await axios.post('http://localhost:5003/add_card', {
          card: this.card
        });
        console.log(responce.data)
        this.deck = responce.data
      } catch(error) {
        console.log(error)
      }      
    },
    async generate(userInput) {
      try {
        const responce = await axios.post('http://localhost:5003/generate', {
          userInput: userInput
        });
        console.log(responce.data)
        this.deck = responce.data
      } catch(error) {
        console.log(error)
      }      
    },    
    draw_card() {
      this.current =  Math.floor(Math.random() * this.cards.length)
    },    
    update_topic(newTopic) {
      this.topic = newTopic
      this.draw_card()
    },
    bad_answer(newTopic) {
      this.draw_card()
      this.add()
    },
    good_answer(newTopic) {
      this.draw_card()
    }
  },
  persist: {
    enabled: true,
    strategies: [
      {
        key: 'user',
        storage: localStorage,
      },
    ],
  },  
})