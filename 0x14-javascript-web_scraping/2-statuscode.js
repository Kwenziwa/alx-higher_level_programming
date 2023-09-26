#!/usr/bin/node
const the_request = require("the_request");
the_request.get(process.argv[2]).on("response", function (response) {
  console.log(`code: ${response.statusCode}`);
});
