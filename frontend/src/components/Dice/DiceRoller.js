import React from 'react';

import { List, Typography } from 'antd';
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
      log: rollExample, // this holds the name of each list
    };

    this.RequestRoll = this.RequestRoll.bind(this);
  }

  RequestRoll(e) {
    let data = this.state.log;




    // data.push(this.state.cmd);

    // TO DO : Call dice REST endpoint requesting reroll.
    //this.props.sendMessage(this.state.message)

    this.setState({
      log: data
    })
  }

  render() {
    return (
      <div className="DiceRoller">
        <DiceBoard data={this.state.log} />
        <button onClick={this.RequestRoll}>
          Roll
        </button>
      </div>
    )
  }
}

export default DiceRoller;