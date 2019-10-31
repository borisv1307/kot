import React from 'react';
import "./DiceRoller.css";

import DiceBoard from './DiceBoard'

class DiceRoller extends React.Component {

  state = {
    rolledDice: [], // this holds the name of each list
    selectedDice: [], // this holds the name of each list
    allowReroll: true
  };

  constructor(props) {
    super(props);

    // this.textInput = React.createRef();

    this.AttemptReroll = this.AttemptReroll.bind(this);
  }

  selectedDiceCallback = (selectedDice) => {
    this.setState({ selectedDice: selectedDice });
    // console.log('selected :', selectedDice);
    // console.log('total :', this.state.rolledDice.length);
  }

  async AttemptReroll(e) {

    try {
      // this.textInput.clearSelected();

      let rerollThisMany = this.CalculateRerollCount(this.state);

      let result = await this.RequestDiceRoll(rerollThisMany);

      if (result) {
        this.setState({ rolledDice: result });
      }
    } catch (exception) {
      console.log(exception);
    }
  }

  async CalculateRerollCount(selectedDice, rolledDice) {
    if (selectedDice && rolledDice) {
      let keptDice = selectedDice.length;
      let totalDice = rolledDice.length;
      let reroll = totalDice - keptDice;
      if (reroll > 0) {
        return reroll;
      }
    }

    return 0;
  }

  async RequestDiceRoll(rerollThisMany) {
    try {

      // TO DO: Provide rerollThisMany to server request

      const res = await fetch('http://127.0.0.1:8000/api/dice/');

      const json_data = await res.json();
      var result = [];

      result.push([json_data.dice1, json_data.dice1_selected]);
      result.push([json_data.dice2, json_data.dice2_selected]);
      result.push([json_data.dice3, json_data.dice3_selected]);
      result.push([json_data.dice4, json_data.dice4_selected]);
      result.push([json_data.dice5, json_data.dice5_selected]);
      result.push([json_data.dice6, json_data.dice6_selected]);

      this.state.allowReroll = json_data.allowReroll;

      return result;
    } catch (err) {
      console.log(err);
    }
  }

  render() {
    return (
      <div className="DiceRoller">
        <DiceBoard ref={this.textInput} callbackFromParent={this.selectedDiceCallback} data={this.state.rolledDice} />
        <button disabled={!this.state.allowReroll} onClick={this.AttemptReroll}>Roll</button>
      </div>
    )
  }
}

export default DiceRoller;