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

    this.setState({ data: message.content });
  }

  render() {
    if (this.state.data) {
      return (
        <container className="card">
          {this.state.data.map((entry, index) => (
            <PlayerValues
              key={index}
              player_name={entry.player_name}
              victory_points={entry.victory_points} // 0 to 10
              health={entry.health} // 0 to 10
              energy={entry.energy} // 0 or more
              in_or_out_position={entry.in_or_out_position} // 'In' or 'Out'
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
