import React, { Component } from "react";
import { Redirect } from "react-router-dom";
import "./Lobby.css";
import config from "../services/config";
import GameInstance from "./../services/gameService";
import LobbyListDisplay from "../components/LobbyList/LobbyListDisplay";

export default class LobbyLayout extends Component {
  constructor(props) {
    super(props);
    let user = "Guest_1234";
    let room = "";
    if (props.location && props.location.state) {
      user = props.location.state.username;
      room = "Room_" + Math.floor(Math.random() * 10000 + 1);
    }

    this.state = {
      redirect: false,
      username: user,
      gameRoom: room
    };

    const rand_socket_entry = Math.floor(Math.random() * 10000 + 1);
    GameInstance.connect(rand_socket_entry, config.LOBBY_SOCKET_API_PATH);
  }

  setRedirect = e => {
    this.setState({
      gameRoom: e.target.id,
      redirect: true
    });
  };

  renderRedirect = () => {
    const user = this.state.username;
    const room = this.state.gameRoom;
    if (this.state.redirect) {
      return (
        <Redirect
          to={{
            pathname: "/game",
            state: {
              username: user,
              gameRoom: room
            }
          }}
        />
      );
    }
  };

  roomChangeHandler = event => {
    this.setState({
      gameRoom: event.target.value
    });
  };

  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm p-4">
            <br></br>
            <p>
              TO DO: <br />
              Add list of channels. MT to add a list of game rooms to be
              provided to this page via websocket.
              <br /> This also implies backend must managing channel groups.
            </p>
          </div>
          <div className="col-sm p-4">
            <label>
              Enter a room name (eventually select existing):
              <input
                id="room_input"
                name="room_name"
                type="text"
                size="40"
                onChange={this.roomChangeHandler}
                placeholder="What chat room would you like to enter?"
                value={this.state.gameRoom}
                required
              />
            </label>

            <a className="b" href="/game">
              {this.renderRedirect()}
              <button
                id={this.state.gameRoom}
                onClick={this.setRedirect} // (this.state.gameRoom)
                className="btn btn-secondary"
                type="button"
              >
                Hi {this.state.username}, please click to enter room{" "}
                {this.state.gameRoom}
              </button>
            </a>
          </div>

          <div className="col-sm p-4">
            <LobbyListDisplay
              currentUser={this.state.username}
              currentRoom={this.state.gameRoom}
              data={[]}
              //   setRedirect={dest_room => {
              //     //if (dest_room) {
              //     this.setRedirect(dest_room);
              //     //}
              //   }}
            />
          </div>
        </div>
      </div>
    );
  }
}
