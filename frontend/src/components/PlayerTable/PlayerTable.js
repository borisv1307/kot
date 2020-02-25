import React from "react";
import "./PlayerTable.css";
import Go from "./../Images/icons8-go-48.png";
import Turn from "./../Images/icons8-turn-30.png";

import GameInstance from "../../services/gameService";

import MT_RESPONSE_PLAYERS_STATUS_UPDATE from "../../services/config";

class PlayerTable extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
      username: props.currentUser,
      gameRoom: props.currentRoom,
      data: props.data,
      currentTurnUser: "",
      tableAreaWidth: 0,
      tableAreaHeight: 0,
      centerX: 0,
      centerY: 0
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

  componentDidUpdate(prevProps, prevState) {
    if (this.state.data !== prevState.data) {
      this.doCanvasStuff();
    }
  }

  doCanvasStuff() {
    if (this.state.data instanceof Array) {
      if (this.state.data && this.state.data.length > 0) {
        let canvas = this.refs.canvas;
        // Make it visually fill the positioned parent
        canvas.style.width = "100%";
        canvas.style.height = "100%";

        // ...then set the internal size to match
        canvas.width = this.state.tableAreaWidth;
        canvas.height = this.state.tableAreaHeight;
        const context = canvas.getContext("2d");
        context.fillStyle = "tan";
        var dotsPerCircle = this.state.data.length;
        // if (dotsPerCircle < 1) {
        //   dotsPerCircle = 1;
        // }
        // context.fillStyle = "blue";
        // context.fillRect(0, 0, canvas.width, canvas.height);
        var interval = (Math.PI * 2) / dotsPerCircle;
        let centerX = this.state.centerX > 0 ? this.state.centerX : 100;
        let centerY = this.state.centerY > 0 ? this.state.centerY : 100;
        let radius =
          (this.state.tableAreaWidth < this.state.tableAreaHeight
            ? this.state.tableAreaWidth
            : this.state.tableAreaHeight) * 0.4;
        context.beginPath();
        for (var i = 0; i < dotsPerCircle; i++) {
          let desiredRadianAngleOnCircle = interval * i;
          var x = centerX + radius * Math.cos(desiredRadianAngleOnCircle);
          var y = centerY + radius * Math.sin(desiredRadianAngleOnCircle);
          if (i == 0) context.moveTo(x, y);
          // context.beginPath();
          // context.arc(x, y, 3, 0, Math.PI * 2);
          // context.seg
          // context.closePath();
          // context.fill();

          context.lineTo(x, y);
        }
        context.closePath();
        context.fill();
      }
    }
  }

  componentDidMount() {
    const height = this.divElement.clientHeight;
    const width = this.divElement.clientWidth;
    let centerX = width / 2;
    let centerY = height / 2;

    this.setState({
      tableAreaHeight: height,
      tableAreaWidth: width,
      centerX: centerX,
      centerY: centerY
    });
  }

  genPos(dotsPerCircle) {
    let centerX = this.state.centerX > 0 ? this.state.centerX : 100;
    let centerY = this.state.centerY > 0 ? this.state.centerY : 100;
    if (dotsPerCircle <= 1) {
      return [
        {
          position: "absolute",
          top: centerY,
          left: centerX
        }
      ];
    }

    let interval = (Math.PI * 2) / dotsPerCircle;

    let width = this.state.tableAreaWidth > 0 ? this.state.tableAreaWidth : 200;
    let height =
      this.state.tableAreaHeight > 0 ? this.state.tableAreaHeight : 200;

    let radius =
      (this.state.tableAreaWidth < this.state.tableAreaHeight
        ? this.state.tableAreaWidth
        : this.state.tableAreaHeight) * 0.35;
    let positions = [];

    for (let i = 0; i < dotsPerCircle; i++) {
      let angleRad = interval * i;
      let x = centerX + radius * Math.cos(angleRad);
      let y = centerY + radius * Math.sin(angleRad);

      positions.push({
        position: "absolute",
        top: y,
        left: x
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
    return this.state.username === this.state.currentTurnUser;
  }

  isItThisGuyTurn(theGuy) {
    return theGuy === this.state.currentTurnUser;
  }

  gameStarted() {
    return "" !== this.state.currentTurnUser;
  }

  formatName(name) {
    let format = name;

    if (this.areYouMe(name)) format = format + "(YOU) ";

    if (this.isItsYourTurn() && this.areYouMe(name)) {
      return (
        <div className="txt_bounds">
          <p className="txt_format">{name}</p>
          <p className="txt_format">Your Turn!</p>
        </div>
      );
    } else if (this.isItThisGuyTurn(name)) {
      return (
        <div className="txt_bounds">
          <p className="txt_format">{name}</p>
          <p className="txt_format">Turn!</p>
        </div>
      );
    }

    return (
      <div className="txt_bounds">
        <p className="txt_format">{name}</p>
      </div>
    );
  }

  provideShape(name) {
    if (this.isItsYourTurn() && this.areYouMe(name)) {
      return <img alt="Your Turn!" src={Go}></img>;
    }
    // else if (this.isItThisGuyTurn(name)) {
    //   return <img alt="This persons turn." src={Turn}></img>;
    // }
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
          <div
            id="table_area"
            ref={divElement => {
              this.divElement = divElement;
            }}
          >
            {msg}
            {/* Size: width<b>{this.state.tableAreaWidth}px</b> height
            <b>{this.state.tableAreaHeight}px</b> */}
            <container className="player_seats">
              {this.state.data.map((entry, index) => (
                <span key={index}>
                  {this.getSeat(items[index], entry.username)}
                </span>
              ))}
            </container>
            <canvas ref="canvas" />
          </div>
        );
      }
    }

    return (
      <div
        className="test"
        ref={divElement => {
          this.divElement = divElement;
        }}
      >
        <container className="player_seats"></container>
        <canvas ref="canvas" width={640} height={425} />
      </div>
    );
  }
}
export default PlayerTable;
