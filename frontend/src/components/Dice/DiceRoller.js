import React from 'react';
import "./DiceRoller.css";

import DiceBoard from './DiceBoard'

var rollExample = [
  'heart',
  'energy',
  'paw',
  '1',
  '2',
  '3'
];

class DiceRoller extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      rolledDice: rollExample, // this holds the name of each list
    };

    this.RequestRoll = this.RequestRoll.bind(this);
  }

  RequestRoll(e) {

    let data = rollExample;

    // TO DO : Call dice REST endpoint requesting reroll.
    //this.props.sendMessage(this.state.message)

    this.setState({
      rolledDice: data
    })
  }

  render() {
    return (
      <div className="DiceRoller">
        <DiceBoard data={this.state.rolledDice} />
        <button onClick={this.RequestRoll}>Roll</button>
      </div>
    )
  }
}

export default DiceRoller;