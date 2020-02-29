import React from "react";
import {confirmAlert} from 'react-confirm-alert'; // Import
import 'react-confirm-alert/src/react-confirm-alert.css'; // Import css
import GameInstance from "../../services/gameService";


class YieldAlert extends React.Component {
    constructor(props, username, gameroom) {
        super(props);
        // super(props);

        this.state = {
            username: username,
            gameRoom: gameroom
        };

    }


    YieldTokyo(/*e*/) {
        try {
            GameInstance.sendMessage({
                command: "yield_tokyo_request",
                user: this.state.username,
                room: this.state.gameRoom,
                payload: this.state.username
            });
        } catch (exception) {
            console.log(exception);
        }
    }

    KeepTokyo(/*e*/) {
        try {
            GameInstance.sendMessage({
                command: "keep_tokyo_request",
                user: this.state.username,
                room: this.state.gameRoom,
                payload: this.state.username
            });
        } catch (exception) {
            console.log(exception);
        }
    }


    show = () => {
        confirmAlert({
            title: 'You\'ve been attacked!',
            message: 'Yield Tokyo?',
            buttons: [
                {
                    label: 'Yes',
                    onClick: () => this.YieldTokyo()
                },
                {
                    label: 'No',
                    onClick: () => this.KeepTokyo()
                }
            ]
        });
    };

    showCustom = () => {
        confirmAlert({
            customUI: ({onClose}) => {
                return (
                    <div style={{}} className='custom-ui'>
                        <h1>You've been attacked!</h1>
                        <p>Yield Tokyo?</p>
                        <button onClick={() => {
                            this.KeepTokyo();
                            onClose()
                        }}>
                            No
                        </button>


                        <button
                            onClick={() => {
                                this.YieldTokyo();
                                onClose();
                            }}>
                            Yes
                        </button>
                    </div>

                );
            }
        });
    };
}

export default YieldAlert