import { defineStore } from "pinia";
import axios from 'axios'

export const useDeck = defineStore('storeDeck',{
  state:() => ({
    deck: [],
    topic: null,
    stack: [],
    good: [],
    bad: [],
  }),
  getters: {
    topics() {
      return new Set(this.deck.map(item => item.topic))
    },
    cards() {
      return this.deck.filter(card => card.topic === this.topic)
    },
    card() {
      return this.stack.at(-1)
    },
  },
  actions:{
    async load() {
      try {
        const response = await axios.get('http://localhost:5003/')
        this.deck = response.data
      }
      catch(error) {
        console.log(error)
      }
    },
    async generate(userInput) {
      try {
        const response = await axios.post('http://localhost:5003/generate', {
          userInput: userInput
        });
        this.deck = response.data
      } catch(error) {
        console.log(error)
      }
    },
    async score() {
      try {
        const response = await axios.put('http://localhost:5003/score', {
          card: this.card
        });
        this.deck = response.data
      } catch(error) {
        console.log(error)
      }
    },
    shuffle() {
      let stack = this.cards
      let currentIndex = stack.length;
      while (currentIndex != 0) {
        let randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        [stack[currentIndex], stack[randomIndex]] = [stack[randomIndex], stack[currentIndex]];
      }
      this.stack = stack
    },
    discard() {
      this.stack.pop()
    },    
    update_topic(newTopic) {
      this.topic = newTopic
      this.good = []
      this.bad = []
      this.shuffle()
    },
    good_answer(newTopic) {
      this.card['score'] = this.card['score'] + 1
      this.score()
      this.good.push(this.card)
      this.discard()
    },
    bad_answer(newTopic) {
      this.card['score'] = this.card['score'] - 1
      this.score()
      this.bad.push(this.card)
      this.discard()
    },    
  }, 
})