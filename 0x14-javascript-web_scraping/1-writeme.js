#!/usr/bin/node

const fs = require("fs");

const theFilePath = process.argv[2];
const theContentToWrite = process.argv[3];

if (!theFilePath || !theContentToWrite) {
  console.error('Usage: node write_file.js <file_path> "<content_to_write>"');
  process.exit(1);
}

fs.writeFile(theFilePath, theContentToWrite, "utf-8", (error) => {
  if (error) {
    console.error(`An error occurred while writing to the file: ${error}`);
  } else {
    console.log(`Content has been successfully written to ${theFilePath}`);
  }
});

