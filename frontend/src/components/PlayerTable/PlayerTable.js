import React from "react";
import "./PlayerTable.css";
import Go from "./../Images/icons8-go-48.png";
import Turn from "./../Images/icons8-turn-30.png";
import Waiting from "./../Images/icons8-wait-30.png";

import GameInstance from "../../services/gameService";

import MT_RESPONSE_PLAYERS_STATUS_UPDATE from "../../services/config";

class PlayerTable extends React.Component {
  _canvas = null;

  constructor(props, context) {
    super(props, context);

    this.state = {
      username: props.currentUser,
      gameRoom: props.currentRoom,
      data: props.data,
      currentTurnUser: ""
    };

    GameInstance.addCallback(
      MT_RESPONSE_PLAYERS_STATUS_UPDATE,
      this.playerUpdateHandler.bind(this)
    );
    GameInstance.addBeginTurnCallback(this.beginTurnHandler.bind(this));
  }

  playerUpdateHandler(message) {
    const content = message.content;

    if (content === undefined || content === "") return;

    let player_status = [];
    try {
      player_status = JSON.parse(content);
    } catch (e) {}
    this.setState({ data: player_status });
  }

  // componentDidUpdate() {
  //   this.tempDoCanvasStuff();
  // }

  // tempDoCanvasStuff() {
  //   if (this.state.data instanceof Array) {
  //     if (this.state.data && this.state.data.length > 0) {
  //       this._canvas = this.refs.canvas;
  //       // Make it visually fill the positioned parent
  //       this._canvas.style.width = "100%";
  //       this._canvas.style.height = "100%";
  //       // ...then set the internal size to match
  //       this._canvas.width = this._canvas.offsetWidth;
  //       this._canvas.height = this._canvas.offsetHeight;
  //       // const context = canvas.getContext("2d");
  //       // var dotsPerCircle = this.state.data.length;
  //       // var interval = (Math.PI * 2) / dotsPerCircle;
  //       // var centerX = 150;
  //       // var centerY = 150;
  //       // var radius = 75;
  //       // for (var i = 0; i < dotsPerCircle; i++) {
  //       //   let desiredRadianAngleOnCircle = interval * i;
  //       //   var x = centerX + radius * Math.cos(desiredRadianAngleOnCircle);
  //       //   var y = centerY + radius * Math.sin(desiredRadianAngleOnCircle);
  //       //   context.beginPath();
  //       //   context.arc(x, y, 3, 0, Math.PI * 2);
  //       //   context.closePath();
  //       //   context.fill();
  //       // }
  //     }
  //   }
  // }

  // componentDidMount() {
  //   this.tempDoCanvasStuff();
  // }

  genPos(dotsPerCircle) {
    if (dotsPerCircle < 1) {
      dotsPerCircle = 1;
    }

    var interval = (Math.PI * 2) / dotsPerCircle;
    var centerX = 200;
    var centerY = 200;
    var radius = 75;
    let positions = [];

    for (var i = 0; i < dotsPerCircle; i++) {
      let desiredRadianAngleOnCircle = interval * i;
      var x = centerX + radius * Math.cos(desiredRadianAngleOnCircle);
      var y = centerY + radius * Math.sin(desiredRadianAngleOnCircle);

      positions.push({
        position: "absolute",
        top: x,
        left: y,
        fill: "lime",
        stroke: "purple"
      });
    }
    return positions;
  }

  beginTurnHandler(message) {
    const username_whos_turn_it_is = message.content;

    if (
      username_whos_turn_it_is === undefined ||
      username_whos_turn_it_is === ""
    )
      return;

    let its_my_turn = username_whos_turn_it_is === this.state.username;

    this.setState({
      currentTurnUser: username_whos_turn_it_is,
      itsMyTurn: its_my_turn
    });
  }

  areYouMe(name) {
    return name === this.state.username;
  }

  isItsYourTurn() {
    return this.state.username == this.state.currentTurnUser;
  }

  isItThisGuyTurn(theGuy) {
    return theGuy == this.state.currentTurnUser;
  }

  gameStarted() {
    return "" !== this.state.currentTurnUser;
  }

  formatName(name) {
    let format = "";
    if (this.areYouMe(name)) format = "(YOU) ";
    return format + name;
  }

  provideShape(name) {
    if (this.isItsYourTurn() && this.areYouMe(name)) {
      return <img alt="Your Turn!" src={Go}></img>;
    } else if (this.isItThisGuyTurn(name)) {
      return <img alt="This persons turn." src={Turn}></img>;
    }
    return; // <img alt="Waiting for game to start..." src={Waiting}></img>;
  }

  provideColor(name) {
    if (this.isItsYourTurn() && this.areYouMe(name)) {
      return "green";
    } else if (this.isItThisGuyTurn(name)) {
      return "orange";
    }
    return "black";
  }

  getSeat(style_in, player) {
    return (
      <span className="seat_layout" style={{ ...style_in }}>
        <p style={{ color: this.provideColor(player) }}>
          {this.provideShape(player)}
          {this.formatName(player)}
        </p>
      </span>
    );
  }

  render() {
    if (this.state.data instanceof Array) {
      if (this.state.data && this.state.data.length > 0) {
        let items = this.genPos(this.state.data.length);

        let msg = <p>Game Started! {items.length} Playing...</p>;
        if (!this.gameStarted()) {
          msg = <p>Waiting, Please wait.</p>;
        }

        return (
          <div>
            {msg}
            <container className="player_seats">
              {this.state.data.map((entry, index) => (
                <span>{this.getSeat(items[index], entry.username)}</span>
              ))}
              {/* <canvas ref="canvas" width={640} height={425} /> */}
            </container>
          </div>
        );
      }
    }

    return <div></div>;
  }
}
export default PlayerTable;
