#!/usr/bin/node
var request = require('request')
request.get(process.argv[2], (err, response, body)=>{
    if (err) console.log(err)
    console.log('code: ',response.statusCode)
})