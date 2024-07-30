#!/usr/bin/node
var fs = require('fs')

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err, data)=>{
    if (err) throw err
} );