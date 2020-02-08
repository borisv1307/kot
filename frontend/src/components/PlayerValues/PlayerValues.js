import React from "react";
import Heart from "./../Images/Heart.gif";
import Star from "./../Images/Star.png";
import Energy from "./../Images/Energy.png";
import "./PlayerValues.css";

class PlayerValues extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
      player_name: this.props.player_name,
      victory_points: this.props.victory_points, // 0 to 10
      health: this.props.health, // 0 to 10
      energy: this.props.energy, // 0 or more
      in_or_out_position: this.props.in_or_out_position // 'In' or 'Out'
    };
  }

  render() {
    return (
      <div>
        <div className="player-border">
          <h2>Player {this.state.player_name}</h2>
          <div className="player-values">
            <p>
              Victory Points:
              <span className="badge badge-light">
                {this.state.victory_points}
              </span>
              <img src={Star}></img>
            </p>
            <p>
              Health:
              <span className="badge badge-light">{this.state.health}</span>
              <img src={Heart}></img>
            </p>
            <p>
              Energy:
              <span className="badge badge-light">{this.state.energy}</span>
              <img src={Energy}></img>
            </p>
            <p>
              In/Out of Tokyo:
              <span className="badge badge-warning">
                {this.state.in_or_out_position}
              </span>
            </p>
          </div>
        </div>
      </div>
    );
  }
}
export default PlayerValues;
