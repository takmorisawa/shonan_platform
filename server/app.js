var express = require("express");
var app = express();

var mysql = require("mysql");
var conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "NodeTest"
});

var server = app.listen(3000, function(){
  console.log("Node.js is listening to PORT:" + server.address().port)
});

var photo_list = [
  {
    id: "001",
    name: "photo001.jpg",
    type: "jpg",
    dataUrl: "http://localhost:3000/data/photo001.jpg"
  }
]

app.get("/api/photo/list", function(req, res, next){
  conn.query("select * from test_table", function(error, results, fields){
    if (error) throw error;
    res.send(results[0]);
  });
  // res.json(photo_list);
});

app.get("/api/photo/list/:photo_id", function(req, res, next){
  var photo;
  for (i = 0; i < photo_list.length; i++){
    if (photo_list[i].id == req.params.photo_id){
      var photo = photo_list[i];
    }
  }
  res.json(photo);
})
