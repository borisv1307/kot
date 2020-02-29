import React from "react";
import { Redirect } from "react-router-dom";
import "./LobbyListDisplay.css";
import Table from "react-bootstrap/Table";
import GameInstance from "../../services/gameService";

class LobbyListDisplay extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
      redirect: false,
      username: props.currentUser,
      gameRoom: props.currentRoom,
      data: props.data
    };

    GameInstance.addGameListResponseCallback(
      this.gameListResponseHandler.bind(this)
    );

    this.waitForSocketConnection(() => {
      const request = this.createRequestGameListCommand(
        this.state.username,
        this.state.gameRoom
      );
      GameInstance.sendMessage(request);
    });
  }

  waitForSocketConnection(callback) {
    const component = this;
    setTimeout(function() {
      // Check if websocket state is OPEN
      if (GameInstance.state() === 1) {
        console.log("Lobby connection is made");
        callback();
        return;
      } else {
        console.log("wait for lobby connection...");
        component.waitForSocketConnection(callback);
      }
    }, 100); // wait 100 milisecond for the connection...
  }

  createRequestGameListCommand(user, room) {
    return {
      command: "request_game_list",
      user: user,
      room: room
    };
  }

  gameListResponseHandler(message) {
    const content = message.content;

    if (content === undefined || content === "") return;

    if (content instanceof Object) {
      let game_list = [];
      try {
        for (const game_key in content) {
          let game = content[game_key];
          let player_detail = JSON.parse(game);

          let player_list = [];
          for (const person_key in player_detail) {
            let player = player_detail[person_key];
            player_list.push(player.username);
          }

          game_list.push({
            room_name: game_key,
            users: player_list.join()
          });
        }
      } catch (e) {}

      if (game_list.length) {
        this.setState({ data: game_list });
      }
    }
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

  renderState() {
    if (this.state.data instanceof Array) {
      if (this.state.data.length) {
        return (
          <div>
            <Table striped bordered hover>
              <thead>
                <tr>
                  <th>Players</th>
                  <th>Room Name</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {this.state.data.map((entry, index) => (
                  <tr key={index}>
                    <td>{entry.users}</td>
                    <td>{entry.room_name}</td>
                    <td>
                      <a className="b" href="/game">
                        {this.renderRedirect()}
                        <button
                          id={entry.room_name}
                          onClick={this.setRedirect} // (this.state.gameRoom)
                          className="btn btn-secondary"
                          type="button"
                        >
                          Join Room {entry.room_name}
                        </button>
                      </a>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </div>
        );
      }
    }
    return this.renderDefault();
  }

  renderDefault() {
    return (
      <div>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Players</th>
              <th>Room Name</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{this.state.username}</td>
              <td>{this.state.gameRoom}</td>
              <td>
                <a className="b" href="/game">
                  {this.renderRedirect()}
                  <button
                    id={this.state.gameRoom}
                    onClick={this.setRedirect} // (this.state.gameRoom)
                    className="btn btn-secondary"
                    type="button"
                  >
                    Join Room {this.state.gameRoom}
                  </button>
                </a>
              </td>
            </tr>
          </tbody>
        </Table>
      </div>
    );
  }

  render() {
    return this.renderState();
  }
}
export default LobbyListDisplay;
