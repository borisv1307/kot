import React from "react";
import Heart from "./../Images/Heart.gif";
import Star from "./../Images/Star.png";
import Energy from "./../Images/Energy.png";
import "./PlayerValues.css";
import PlayerHandDisplay from "./PlayerHandDisplay";

class PlayerValues extends React.Component {
  render() {
    return (
      <div>
        <div class="container">
          <div class="row">
            <div class="col-sm player-border">
              <h2>Player {this.props.username}</h2>
              <div className="player-values">
                <p>
                  Victory Points:
                  <span className="badge badge-light">
                    {this.props.victory_points}
                  </span>
                  <img alt="" src={Star}></img>
                </p>
                <p>
                  Health:
                  <span className="badge badge-light">
                    {this.props.current_health}
                  </span>
                  <img alt="" src={Heart}></img>
                </p>
                <p>
                  Energy:
                  <span className="badge badge-light">{this.props.energy}</span>
                  <img alt="" src={Energy}></img>
                </p>
                <p>
                  In/Out of Tokyo:
                  <span className="badge badge-warning">
                    {this.props.location}
                  </span>
                </p>
              </div>
            </div>
            <div class="col-sm">
              <PlayerHandDisplay data={this.props.cards} />
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default PlayerValues;
