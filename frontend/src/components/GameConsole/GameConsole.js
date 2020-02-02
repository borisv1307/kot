import React from "react";
import "./GameConsole.css";

import GameLog from "./GameLog";

import GameInstance from "./../../services/gameService";

class GameConsole extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      username: props.currentUser,
      gameRoom: props.currentRoom,
      log: [], // this holds the name of each list
      cmd: props.cmd
    };

    this.waitForSocketConnection(() => {
      const initCmd = this.createInitUserCommand(
        this.state.username,
        this.state.gameRoom
      );
      GameInstance.sendMessage(initCmd);
      GameInstance.addCallback(this.serverResponseHandler.bind(this));
      GameInstance.addBeginTurnCallback(this.beginTurnHandler.bind(this));
    });

    this.handleChange = this.handleChange.bind(this);
    this.SubmitGameCommand = this.SubmitGameCommand.bind(this);
  }

  createInitUserCommand(user, room) {
    return {
      command: "init_user_request",
      user: user,
      room: room
    };
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

    let log_message = its_my_turn
      ? "your turn " + this.state.username
      : username_whos_turn_it_is + " turn...";

    this.setState({ log: [...this.state.log, log_message] });
  }

  serverResponseHandler(messages) {
    this.appendStateCmdToLog(messages);
  }

  waitForSocketConnection(callback) {
    const component = this;
    setTimeout(function() {
      // Check if websocket state is OPEN
      if (GameInstance.state() === 1) {
        console.log("Connection is made");
        callback();
        return;
      } else {
        console.log("wait for connection...");
        component.waitForSocketConnection(callback);
      }
    }, 100); // wait 100 milisecond for the connection...
  }

  appendStateCmdToLog(message) {
    // const room = message.room;
    // const user = message.user;
    const content = message.content;

    if (content === undefined || content === "") return;

    this.setState({ log: [...this.state.log, content] });

    return this.state.log;
  }

  SubmitGameCommand(e) {
    if (this.state.cmd === undefined || this.state.cmd === "") return;

    const command = {
      command: "gamelog_send_request",
      user: this.state.username,
      room: this.state.gameRoom,
      payload: this.state.cmd
    };

    this.props.sendMessage(command);
  }

  handleChange(e) {
    this.setState({
      cmd: e.target.value
    });
  }

  render() {
    return (
      <div className="game_console">
        <GameLog
          data={this.state.log}
          currentUser={this.state.username}
          currentRoom={this.state.gameRoom}
        />

        <form
          className="submit_game_command"
          onSubmit={this.SubmitGameCommand}
          onChange={this.handleChange}
        >
          <textarea
            name="text_entry"
            id="text_entry"
            type="text"
            value={this.state.value}
            onChange={this.handleChange}
          ></textarea>
        </form>
        <button
          name="send_button"
          id="send_button"
          className="btn btn-secondary"
          onClick={this.SubmitGameCommand}
        >
          Send
        </button>
      </div>
    );
  }
}

export default GameConsole;
