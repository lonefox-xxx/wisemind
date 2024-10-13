const fs = require('fs')

const quotes = JSON.parse(fs.readFileSync('./qoutes.json', 'utf8'))
console.log(quotes.length)