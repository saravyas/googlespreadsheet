var Gs = require('google-spreadsheet');
var file = require('./client_config.json');
// Please load your config file
var doc = new Gs('1PWaUJ-uwQFmFNzW1JwxsREwyCh6rLrBHjrZnanMtbnM');

doc.useServiceAccountAuth(file, function (err) {
 
  doc.getRows(1, function (err, rows) {
  	rows[2].del();
    console.log(rows);
  });
});

 
