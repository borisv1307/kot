import React from 'react';
import "./GameConsole.css";

import GameLog from './GameLog'

const gameLogExample = [
  '-- Sammy turn –',
  'Rolled: E E H 1 2 3',
  'Decision: keep E E',
  'Rolled: E P 1 2 2',
  'Decision: keep E',
  'Rolled: 2 2 2 (TRIPPLE! +2 VP)',
  ':: Gain: E E E +2 VP ::',
  'Buy: Psychic Probe',
  'End Turn'
];

class GameConsole extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      log: gameLogExample, // this holds the name of each list
      cmd: "enter cmd"
    };

    this.handleChange = this.handleChange.bind(this);
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

  handleChange(e) {
    this.setState({
      cmd: e.target.value
    })
  }

  render() {
    return (
      <div className="game_console">
        <GameLog data={this.state.log} />

        <form className="submit_game_command"
          onSubmit={this.SubmitGameCommand}
          onChange={this.handleChange}>
          <textarea value={this.state.value} onChange={this.handleChange}>Type Command [enter]</textarea>
        </form>
        <button onClick={this.SubmitGameCommand}>
          Submit Comand
          </button>
      </div>
    )
  }
}

export default GameConsole;