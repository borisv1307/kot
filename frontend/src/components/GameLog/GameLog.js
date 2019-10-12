import React, { Component } from 'react';

import "./GameLog.css";

export default class GameLog extends Component {
  render() {
    return (
      <div className="gamelog">
        { this.props.children }
      </div>
    )
  }
}
