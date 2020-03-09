import React from "react";
import {confirmAlert} from 'react-confirm-alert'; // Import
import 'react-confirm-alert/src/react-confirm-alert.css'; // Import css
import GameInstance from "../../services/gameService";


class ChooseYielderAlert extends React.Component {
    constructor(props, username, gameroom, player1, player2) {
        super(props);
        // super(props);

        this.state = {
            username: username,
            gameRoom: gameroom,
            player1: player1,
            player2: player2
        };

    }

    kickOut(player) {
        try {
            GameInstance.sendMessage({
                command: "force_yield_tokyo_request",
                user: this.state.username,
                room: this.state.gameRoom,
                payload: player
            });
        } catch (exception) {
            console.log(exception);
        }
    }


    show = () => {
        confirmAlert({
            title: 'You\'re  taking Tokyo!',
            message: 'Who do you want to force to yield?',
            buttons: [
                {
                    label: this.state.player1,
                    onClick: () => this.kickOut(this.state.player1)
                },
                {
                    label: this.state.player2,
                    onClick: () => this.kickOut(this.state.player2)
                }
            ]
        });
    };

}

export default ChooseYielderAlert