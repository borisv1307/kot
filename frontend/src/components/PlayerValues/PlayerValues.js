import React from "react";
import Heart from "./../Images/Heart.gif";
import Star from "./../Images/Star.png";
import Energy from "./../Images/Energy.png";
import "./PlayerValues.css";
import PlayerHandDisplay from "./PlayerHandDisplay";

class PlayerValues extends React.Component {
  render() {
    let you_or_them = "them";
    if (this.props.thisIsYou) {
      you_or_them = "you";
    }

    return (
      <div>
        <div className="container">
          <div className="row">
            <div className="col-sm player-border">
              <h2>{this.props.username}</h2>
              <p>{you_or_them}</p>
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
            <div className="col-sm">
              <PlayerHandDisplay data={this.props.cards} />
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default PlayerValues;
