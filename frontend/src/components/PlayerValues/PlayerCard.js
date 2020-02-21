import React from "react";
import Info from "./../Images/icons8-info-128.png";
import Energy from "./../Images/Energy.png";
import Footnote from "./../Images/icons8-footsteps-50.png";
import "./PlayerCard.css";

class PlayerCard extends React.Component {
  render() {
    let t_footnote = "None";
    if (this.props.footnote) {
      t_footnote = this.props.footnote;
    }

    return (
      <div>
        <div className="card-border">
          <p className="card-instances">
            {this.props.type}
            {this.props.name}
            <br />
            <span>
              {this.props.cost}
              <img className="img-energy" alt="" src={Energy}></img>
            </span>
            <span data-tooltip={this.props.effect}>
              <img className="img-info" alt="" src={Info}></img>
            </span>
            <span data-tooltip={t_footnote}>
              <img className="img-info" alt="" src={Footnote}></img>
            </span>
          </p>
        </div>
      </div>
    );
  }
}
export default PlayerCard;
