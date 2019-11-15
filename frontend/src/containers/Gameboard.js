import React, { Component } from 'react';
import "./Gameboard.css";

import GameConsole from '../components/GameConsole/GameConsole'
import ChatConsole from '../components/GameConsole/ChatConsole'
import DiceRoller from './../components/Dice/DiceRoller'

export default class GameboardLayout extends Component {

    constructor(props) {
        super(props);

        let userName = 'Guest_' + Math.floor((Math.random() * 10000) + 1);
        let roomName = 'Room_' + Math.floor((Math.random() * 10000) + 1);
        if (props.location.state) {
            userName = userName;
            roomName = roomName;
        }

        this.state = {
            username: userName,
            gameRoom: roomName,
            loggedIn: true
        };
    }

    render() {
        return (
            <div>
                <br/>
                <h4>{this.state.gameRoom}</h4>
                <div className="container">
                    {
                        this.state.loggedIn ?
                            <div className="row">
                                <div className="col-sm">
                                    <DiceRoller />
                                </div>
                                <div className="col-sm">
                                    <GameConsole />
                                </div>
                                <div className="col-sm">
                                    <ChatConsole username={this.state.username} gameRoom={this.state.gameRoom} />
                                </div>
                            </div>
                            :
                            <p>Please login</p>
                    }
                </div>
            </div>
        );
    }
}
