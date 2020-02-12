import React from "react";
import "./PlayerValueDisplay.css";
import PlayerValues from "./PlayerValues";
import GameInstance from "../../services/gameService";

import MT_RESPONSE_PLAYERS_STATUS_UPDATE from "../../services/config";

class PlayerValueDisplay extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
      username: props.currentUser,
      gameRoom: props.currentRoom,
      data: props.data
    };

    GameInstance.addCallback(
      MT_RESPONSE_PLAYERS_STATUS_UPDATE,
      this.playerUpdateHandler.bind(this)
    );
  }

  playerUpdateHandler(message) {
    const content = message.content;

    if (content === undefined || content === "") return;

    let player_status = [];
    try {
      player_status = JSON.parse(content);
    } catch (e) {}
    this.setState({ data: player_status });
  }

  render() {
    if (this.state.data) {
      return (
        <container className="player_details">
          {this.state.data.map((entry, index) => (
            <PlayerValues
              key={index}
              username={entry.username}
              victory_points={entry.victory_points} // 0 to 10
              current_health={entry.current_health} // 0 to 10
              energy={entry.energy} // 0 or more
              location={entry.location} // 'In' or 'Out'
              cards={entry.cards}
            />
          ))}
        </container>
      );
    } else {
      return <div>Waiting on Players</div>;
    }
  }
}
export default PlayerValueDisplay;
