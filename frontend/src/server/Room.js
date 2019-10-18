import React from 'react';

var app = require("express")();
var http = require("http").Server(app);
var io = require("socket.io")(http);

const port = 3000;

app.get("/", function(req, res) {
  res.sendFile(__dirname + "/index.html");
});

io.on("connection", function(socket) {
  console.log("a user connected");

  socket.on("join_room", room => {
    socket.join(room);
  });

    http.listen(port, function() {
  console.log(`listening on *:${port}`);
});

socket.emit("new_visitor", visitor);

socket.on("visitors", visitors => {
  this.setState({
    visitors: visitors
  });
});
});

}