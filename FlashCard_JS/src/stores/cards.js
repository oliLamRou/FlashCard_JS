import { defineStore } from "pinia";

export const useCards = defineStore('pairForm',{
  state:() => ({
    cards: {
      question: 'Dog',
      answer: 'Chien',
      last: '2024/01/01',
      score: -1,
      url: ''
    }
  }),
})