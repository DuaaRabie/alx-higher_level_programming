#!/usr/bin/node

const fs = require('fs');

const sourcePath1 = process.argv[2];
const sourcePath2 = process.argv[3];
const destPath = process.argv[4];

fs.readFile(sourcePath1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading file ${sourcePath1}:`, err);
  }

  fs.readFile(sourcePath2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading file ${sourcePath2}:`, err);
    }

    const combinedData = data1 + data2;

    fs.writeFile(destPath, combinedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to file ${destPath}:`, err);
      }

      console.log(`${combinedData}`);
    });
  });
});
