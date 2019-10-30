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

  async FetchRoll() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/dice/');

      const json_data = await res.json();
      var result = [];

      result.push([0, json_data.dice1]);
      result.push([1, json_data.dice2]);
      result.push([2, json_data.dice3]);
      result.push([3, json_data.dice4]);
      result.push([4, json_data.dice5]);
      result.push([5, json_data.dice6]);
      result.push([6, json_data.dice7]);

      // for (var i in json_data)
      //   result.push([i, json_data[i]]);
      return result;
    } catch (err) {
      console.log(err);
      //alert(err); // TypeError: failed to fetch
    }
  }

  async RequestRoll(e) {

    // let data = rollExample;

    try {

      let result = await this.FetchRoll();

      this.setState({ rolledDice: result });
    } catch (e) {
      console.log(e);
    }

    // TO DO : Call dice REST endpoint requesting reroll.
    //this.props.sendMessage(this.state.message)

    // this.setState({
    //   rolledDice: data
    // })
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