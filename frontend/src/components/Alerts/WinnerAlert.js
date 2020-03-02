import React from "react";
import {confirmAlert} from 'react-confirm-alert'; // Import
import 'react-confirm-alert/src/react-confirm-alert.css'; // Import css


class WinnerAlert extends React.Component {
    constructor(props, username) {
        super(props);

        this.state = {
            username: username,
        };

    }

    show = () => {
        confirmAlert({
            title: 'There is a winner.',
            message: 'Game is over. ' + this.state.username + " has won.",
            buttons: [
                {
                    label: 'Ok'
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

export default WinnerAlert