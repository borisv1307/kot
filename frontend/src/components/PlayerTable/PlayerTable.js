import React from "react";
import "./PlayerTable.css";
import Go from "./../Images/icons8-go-48.png";
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
        if (canvas) {
          // Make it visually fill the positioned parent
          canvas.style.width = "100%";
          canvas.style.height = "100%";

          // ...then set the internal size to match
          canvas.width = this.state.tableAreaWidth;
          canvas.height = this.state.tableAreaHeight;

          const context = canvas.getContext("2d");
          var dotsPerCircle = this.state.data.length;

          if (dotsPerCircle <= 2) dotsPerCircle = 3;

          // context.fillStyle = "blue";
          // context.fillRect(0, 0, canvas.width, canvas.height);
          var interval = (Math.PI * 2) / dotsPerCircle;
          let centerX = this.state.centerX > 0 ? this.state.centerX : 100;
          let centerY = this.state.centerY > 0 ? this.state.centerY : 100;
          let radius = this.state.tableAreaWidth * 0.5;

          context.beginPath();
          for (var i = 0; i < dotsPerCircle; i++) {
            context.fillStyle = "tan";
            let desiredRadianAngleOnCircle = interval * i;
            var x = centerX + radius * Math.cos(desiredRadianAngleOnCircle);
            var y = centerY + radius * Math.sin(desiredRadianAngleOnCircle);
            if (i === 0) context.moveTo(x, y);
            context.lineTo(x, y);
          }
          context.closePath();
          context.fill();

          this.state.data.map((entry, index) => {
            let desiredRadianAngleOnCircle = interval * index;
            var x = centerX + radius * Math.cos(desiredRadianAngleOnCircle);
            var y = centerY + radius * Math.sin(desiredRadianAngleOnCircle);
            context.fillStyle = "tan";
            context.font = "20px Arial";
            const txt = this.formatName(entry.username);
            const tInfo = context.measureText(txt);
            const tWidth = tInfo.width * 0.5;

            let txtX = x - tWidth;
            if (x + tWidth > this.state.tableAreaWidth) txtX = x - tInfo.width;

            context.fillStyle = "white";
            /// draw background rect assuming height of font
            context.fillRect(txtX - 2, y - 20 + 2, tInfo.width + 4, 24);

            context.fillStyle = "black";
            context.fillText(txt, txtX, y);

            const img = this.provideShape();
            if (img) context.drawImage(img, x, y);
          });
        }
      }
    }
  }

  componentDidMount() {
    if (this.divElement) {
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
    if (this.isItsYourTurn() && this.areYouMe(name)) {
      return name + "Your Turn!";
    } else if (this.isItThisGuyTurn(name)) {
      return name + "Turn!";
    }
    return name;
  }

  provideShape(name) {
    if (this.isItsYourTurn() && this.areYouMe(name)) {
      return this.refs.Go_Image;
    }
    return null;
  }

  render() {
    if (this.state.data instanceof Array) {
      if (this.state.data && this.state.data.length > 0) {
        // let items = this.genPos(this.state.data.length);

        let msg = <p>Game Started! {this.state.data.length} Playing...</p>;
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
            <img hidden ref="Go_Image" src={Go}></img>
            {msg}
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
