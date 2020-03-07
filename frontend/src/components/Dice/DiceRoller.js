import React from "react";
import "./DiceRoller.css";
import Button from "react-bootstrap/Button";
import DiceBoard from "./DiceBoard";
import GameInstance from "../../services/gameService";

class DiceRoller extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      username: props.currentUser,
      gameRoom: props.currentRoom,
      currentTurnUser: "",
      rolledDice: [],
      selectedDice: [],
      allowReroll: true,
      allowEndTurn: false,
      diceAccepted: false,
      its_my_turn: false
    };

    this.AttemptReroll = this.AttemptReroll.bind(this);
    this.EndTurn = this.EndTurn.bind(this);
    this.ResolveDice = this.ResolveDice.bind(this);
    GameInstance.addDiceCallback(this.diceRollerHandler.bind(this));
    GameInstance.addBeginTurnCallback(this.beginTurnHandler.bind(this));
    GameInstance.addAllowEndTurnCallback(this.allowEndTurnHandler.bind(this));
  }

  componentDidMount() {
    // ... do something with fetchedData e.g. set the data
  }

  selectedDiceCallback = selectedDice => {
    this.setState({ selectedDice: selectedDice });
  };

  diceRollerHandler(message) {
    //    const room = message.room;
    const username_whos_turn_it_is = message.user;
    const content = message.content;

    let its_my_turn = username_whos_turn_it_is === this.state.username;
    this.setState({
      its_my_turn: its_my_turn,
      allowReroll: its_my_turn,
      currentTurnUser: username_whos_turn_it_is
    });

    if (!its_my_turn) {
      // clear dice display
      this.setState({ rolledDice: [] });
    } else {
      if (content === undefined || content === "") return;
      this.setState({ rolledDice: content });
    }
  }

  gameStarted() {
    return "" !== this.state.currentTurnUser;
  }

  beginTurnHandler(message) {
    // const room = message.room;
    // const user = message.user;
    const username_whos_turn_it_is = message.content;

    if (
      username_whos_turn_it_is === undefined ||
      username_whos_turn_it_is === ""
    )
      return;

    let its_my_turn = username_whos_turn_it_is === this.state.username;

    this.setState({
      allowReroll: its_my_turn,
      allowEndTurn: false,
      diceAccepted: false,
      rolledDice: [],
      selectedDice: [],
      //   allowReroll: true,
      its_my_turn: false,
      currentTurnUser: username_whos_turn_it_is
    });
  }

  allowEndTurnHandler(message) {
    if (this.state.its_my_turn) {
      this.setState({ allowEndTurn: true });
    }
  }

  ResolveDice(/*e*/) {
    try {
      GameInstance.sendMessage({
        command: "resolve_dice_request",
        user: this.state.username,
        room: this.state.gameRoom,
        payload: this.state.username
      });
      this.setState({ allowReroll: false, diceAccepted: true });
    } catch (exception) {
      console.log(exception);
    }
  }

  EndTurn(/*e*/) {
    if (this.state.diceAccepted === false) {
      this.ResolveDice();
    }

    try {
      GameInstance.sendMessage({
        command: "end_turn_request",
        user: this.state.username,
        room: this.state.gameRoom,
        payload: this.state.username
      });
    } catch (exception) {
      console.log(exception);
    }
  }

  async AttemptReroll(/*e*/) {
    try {
      if (false === this.determineSelectedDice()) {
        const messageObject = {
          user: this.state.username,
          room: this.state.gameRoom,
          data: ""
        };

        this.sendDiceStateRequest(messageObject);
      }
    } catch (exception) {
      console.log(exception);
    }
  }

  sendDiceStateRequest(envelope) {
    GameInstance.sendMessage({
      command: "return_dice_state_request",
      user: envelope.user,
      room: envelope.room,
      payload: ""
    });
  }

  determineSelectedDice() {
    let selected = this.state.rolledDice;

    if (this.state.selectedDice) {
      selected.forEach(index => {
        index[1] = false;
      });

      this.state.selectedDice.forEach(index => {
        selected[index - 1][1] = true;
      });
    }

    if (selected && selected.length > 0) {
      const messageObject = {
        user: this.state.username,
        room: this.state.gameRoom,
        data: selected
      };

      this.sendSelectedDice(messageObject);
      this.setState({
        message: ""
      });
      return true;
    }
    return false;
  }

  // sends dice back to server formatted as an array of 2d arrays.
  // first index: the roll value
  // second index: selected or not
  // payload format: [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
  sendSelectedDice(envelope) {
    GameInstance.sendMessage({
      command: "selected_dice_request",
      user: envelope.user,
      room: envelope.room,
      payload: envelope.data
    });
  }

  CalculateRerollCount() {
    if (this.state && this.state.selectedDice && this.state.rolledDice) {
      let keptDice = this.state.selectedDice.length;
      let totalDice = this.state.rolledDice.length;
      return totalDice - keptDice;
    }

    return 0;
  }

  playerHasRolled() {
    let hasRolledAtLeastOnce =
      this.state.rolledDice && this.state.rolledDice.length > 0;
    if (
      !this.state.diceAccepted &&
      this.state.its_my_turn &&
      hasRolledAtLeastOnce
    ) {
      return true;
    } else {
      return false;
    }
  }

  render() {
    let msg = <p>Game Started! Playing...</p>;
    if (!this.gameStarted()) {
      msg = <p>Waiting for more players, Please wait.</p>;
    }
    return (
      <div className="DiceRoller">
        {msg}
        <DiceBoard
          ref={this.textInput}
          callbackSendDiceSelectionOut={this.selectedDiceCallback}
          data={this.state.rolledDice}
          currentUser={this.state.username}
          currentRoom={this.state.gameRoom}
        />
        <Button
          className="btn btn-secondary"
          disabled={!this.gameStarted() || !this.state.allowReroll}
          onClick={this.AttemptReroll}
        >
          Roll
        </Button>

        <Button
          className="btn btn-secondary"
          disabled={!this.gameStarted() || !this.playerHasRolled()}
          onClick={this.ResolveDice}
        >
          Accept Dice
        </Button>

        <Button
          className="btn btn-secondary"
          disabled={!this.gameStarted() || !this.state.allowEndTurn}
          onClick={this.EndTurn}
        >
          End Turn
        </Button>
      </div>
    );
  }
}

export default DiceRoller;
