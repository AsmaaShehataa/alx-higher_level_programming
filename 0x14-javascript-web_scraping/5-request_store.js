#!/usr/bin/node

const request = require('request');
const fscrap = require('fscrap');
const url = process.argv[2];
const fileName = process.argv[3];

const fileStream = fscrap.createWriteStream(fileName);
request(url).pipe(fileStream);
