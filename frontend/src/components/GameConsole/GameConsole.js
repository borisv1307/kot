import React from "react";
import "./GameConsole.css";

import GameLog from "./GameLog";

import GameInstance from "./../../services/gameService";

const gameLogExample = [
  // '-- Sammy turn –',
  // 'Rolled: E E H 1 2 3',
  // 'Decision: keep E E',
  // 'Rolled: E P 1 2 2',
  // 'Decision: keep E',
  // 'Rolled: 2 2 2 (TRIPPLE! +2 VP)',
  // ':: Gain: E E E +2 VP ::',
  // 'Buy: Psychic Probe',
  // 'End Turn'
];

class GameConsole extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      username: props.currentUser,
      gameRoom: props.currentRoom,
      log: [], // this holds the name of each list
      cmd: "enter cmd"
    };

    this.waitForSocketConnection(() => {
      const userObject = {
        user: this.state.username,
        room: this.state.gameRoom,
        data: this.state.cmd
      };

      GameInstance.initUser(userObject);
      GameInstance.addCallbacks(this.serverResponseHandler.bind(this));
    });

    this.handleChange = this.handleChange.bind(this);
    this.SubmitGameCommand = this.SubmitGameCommand.bind(this);
  }

  serverResponseHandler(messages) {
    this.appendStateCmdToLog(messages.content);
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
    const action = message.actionType;
    // const room = message.room;
    // const user = message.user;
    const content = message.content;

    if (content === undefined || content == "") return;

    switch (action) {
      case "GAMECONSOLE_ERROR":
        break;
      case "GAMECONSOLE_MESSAGE":
        break;
      case "GAMECONSOLE_DECISION":
        break;

      default:
        return;
    }

    this.setState({ log: [...this.state.log, content] });

    return this.state.log;
  }

  SubmitGameCommand(e) {
    const cmd = {
      user: this.state.username,
      room: this.state.gameRoom,
      content: this.state.cmd
    };

    this.appendStateCmdToLog(cmd);

    const messageObject = {
      user: this.state.username,
      room: this.state.gameRoom,
      data: this.state.cmd
    };

    GameInstance.sendGameLogCommand(messageObject);
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
          <textarea value={this.state.value} onChange={this.handleChange}>
            Type Command [enter]
          </textarea>
        </form>
        <button className="btn btn-secondary" onClick={this.SubmitGameCommand}>
          Submit Command
        </button>
      </div>
    );
  }
}

export default GameConsole;
