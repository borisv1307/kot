import React from "react";
import Hand from "./../Images/icons8-red-card-80.png";
import "./PlayerHandDisplay.css";
import PlayerCard from "./PlayerCard";

class PlayerHandDisplay extends React.Component {
  constructor(props, context) {
    super(props, context);

    let cards = this.updateCards(this.props.data);
    this.state = {
      username: this.props.currentUser,
      gameRoom: this.props.currentRoom,
      data: cards
    };
  }

  updateCards(data) {
    let cards = {};
    if (this.props.data) {
      try {
        cards = JSON.parse(data);
      } catch (e) {}
    }
    return cards;
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.props.data !== prevProps.data) {
      let cards = this.updateCards(this.props.data);
      this.setState({
        data: cards
      });
    }
  }

  render() {
    if (this.state.data && this.state.data.length > 0) {
      return (
        <div>
          <img className="img-hand" alt="" src={Hand}></img>
          <container className="player_hand_details">
            {this.state.data.map((entry, index) => (
              <PlayerCard
                key={index}
                name={entry.name}
                cost={entry.cost}
                effect={entry.effect}
                footnote={entry.footnote}
              />
            ))}
          </container>
        </div>
      );
    } else {
      return (
        <div>
          <img className="img-hand" alt="" src={Hand}></img>
          No Cards...
        </div>
      );
    }
  }
}
export default PlayerHandDisplay;
