import React from "react";
// import Select, { components } from 'react-select';
import { ToggleButton, ToggleButtonGroup } from "react-bootstrap";

import "./DiceBoard.css";

class DiceBoard extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.handleChange = this.handleChange.bind(this);
    this.clearSelected = this.clearSelected.bind(this);

    this.state = {
      username: props.currentUser,
      gameRoom: props.currentRoom,
      value: []
    };
  }

  handleChange(e) {
    this.setState({ value: e });
    this.props.callbackSendDiceSelectionOut(e);
  }

  clearSelected(e) {
    this.setState({ value: [] });
  }

  render() {
    return (
      <ToggleButtonGroup
        vertical
        type="checkbox"
        value={this.state.value}
        onChange={this.handleChange}
      >
        {this.props.data.map((entry, index) => (
          <ToggleButton key={index} value={index + 1}>
            {entry[0]}
          </ToggleButton>
        ))}
      </ToggleButtonGroup>
    );
  }
}

export default DiceBoard;
