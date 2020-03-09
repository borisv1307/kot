import React, { Component } from "react";
import "./Gameboard.css";
import config from "../services/config";

import GameConsole from "../components/GameConsole/GameConsole";
import DiceRoller from "./../components/Dice/DiceRoller";
import CardStore from "../components/Cards/CardStore";
import PlayerValuesDisplay from "./../components/PlayerValues/PlayerValueDisplay";
import PlayerTable from "../components/PlayerTable/PlayerTable";
import GameInstance from "./../services/gameService";
import YieldAlert from "../components/Alerts/YieldAlert";
import ChooseYielderAlert from "../components/Alerts/ChooseYielderAlert";
import WinnerAlert from "../components/Alerts/WinnerAlert";

export default class GameboardLayout extends Component {
    constructor(props) {
        super(props);

        let userName = "Guest_1234";
        let roomName = "Room_1234";
        if (props.location && props.location.state) {
            userName = props.location.state.username;
            roomName = props.location.state.gameRoom;
        }

        this.state = {
            username: userName,
            gameRoom: roomName,
            loggedIn: true
        };

        GameInstance.connect(this.state.gameRoom, config.GAME_SOCKET_API_PATH);
        GameInstance.addYieldCallback(this.showAlert.bind(this));
        GameInstance.addWinnerCallback(this.showWinner.bind(this));
        GameInstance.addYieldForcedCallback(this.showForceYieldChoice.bind(this))
    }

    showAlert(message) {
        let username_whos_turn_it_is = message.user;
        let yieldAlert = new YieldAlert(
            this.props,
            this.state.username,
            this.state.gameRoom
        );
        if (this.state.username === username_whos_turn_it_is) {
            // yieldAlert.showCustom()
            yieldAlert.show()
        }
    }

    showWinner(message) {
        let winner = message.user;
        let winnerAlert = new WinnerAlert(this.props, winner);
        winnerAlert.show();
        // yieldAlert.showCustom()
    }

    showForceYieldChoice(message){
      let username_whos_turn_it_is = message.user;
      if (this.state.username === username_whos_turn_it_is) {
        let users = message.content;
        let chooseYielder = new ChooseYielderAlert(this.props, this.state.username, this.state.gameRoom, users[0], users[1])
        chooseYielder.show()
      }
    }


  render() {
    return (
      <div className="board_container">
        <br />
        <h4>{this.state.gameRoom}</h4>

        <div className="col">
          <CardStore
            currentUser={this.state.username}
            currentRoom={this.state.gameRoom}
          />
        </div>

        <div>
          {this.state.loggedIn ? (
            <div>
              <div className="row">
                <div className="col-sm-4">
                  <PlayerValuesDisplay
                    currentUser={this.state.username}
                    currentRoom={this.state.gameRoom}
                    displayOnlySelf={true}
                  />
                </div>
                <div className="col-sm-2">
                  <DiceRoller
                    currentUser={this.state.username}
                    currentRoom={this.state.gameRoom}
                  />
                </div>
                <div className="col-sm-4 board_middle_column">
                  <GameConsole
                    sendMessage={payload => {
                      GameInstance.sendMessage(payload);
                    }}
                    currentUser={this.state.username}
                    currentRoom={this.state.gameRoom}
                  />
                </div>

                <div className="col-sm-2">
                  <PlayerTable
                    currentUser={this.state.username}
                    currentRoom={this.state.gameRoom}
                  />
                </div>
              </div>
              <div className="row">
                <div className="col-sm">
                  <PlayerValuesDisplay
                    currentUser={this.state.username}
                    currentRoom={this.state.gameRoom}
                    displayOnlySelf={false}
                  />
                </div>
              </div>
            </div>
          ) : (
            <p>Please login</p>
          )}
        </div>
        <div className="col">
          <a href="https://icons8.com/">Images Provided by icons8.com</a>
        </div>
      </div>
    );
  }
}
