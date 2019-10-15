import React from 'react';

import { List, Typography } from 'antd';
import "./GameConsole.css";

import GameLog from './GameLog'

var rollExample = [
  'heart',
  'energy',
  'paw',
  '1',
  '2',
  '3'
];

class GameConsole extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      log: rollExample, // this holds the name of each list
      cmd: "enter cmd"
    };

    this.OnChange = this.OnChange.bind(this);
    this.SubmitGameCommand = this.SubmitGameCommand.bind(this);
  }

  SubmitGameCommand(e) {
    let data = this.state.log;
    data.push(this.state.cmd);

    // TO DO : Call dice REST endpoint requesting reroll.
    //this.props.sendMessage(this.state.message)

    this.setState({
      log: data
    })
  }

  OnChange(e) {
    this.setState({
      cmd: e.target.value
    })
  }

  render() {
    return (
      <div className="game_console">
        <GameLog data={this.state.log} />
        <form
          onSubmit={this.SubmitGameCommand}
          onChange={this.OnChange}
          className="submit_game_command"></form>
        <button onClick={this.SubmitGameCommand}>
          Submit Comand
          </button>
      </div>
    )
  }
}

export default GameConsole;