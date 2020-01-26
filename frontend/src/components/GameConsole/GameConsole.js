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
      cmd: ""
    };

    this.waitForSocketConnection(() => {
      const initCmd = this.createInitUserCommand(
        this.state.username,
        this.state.gameRoom
      );
      GameInstance.sendMessage(initCmd);
      GameInstance.addCallbacks(this.serverResponseHandler.bind(this));
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

    const command = this.createGameLogCommand(
      this.state.username,
      this.state.gameRoom,
      this.state.cmd
    );

    GameInstance.sendMessage(command);
  }

  createGameLogCommand(user, room, cmd) {
    return {
      command: "gamelog_send_request",
      user: user,
      room: room,

      // payload format: [['text entered by user']
      payload: cmd
    };
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
            value={this.state.value}
            onChange={this.handleChange}
          ></textarea>
        </form>
        <button className="btn btn-secondary" onClick={this.SubmitGameCommand}>
          Submit Command
        </button>
      </div>
    );
  }
}

export default GameConsole;
