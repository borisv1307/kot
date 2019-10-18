import React from 'react';
import "./Lobby.css";
import openSocket from "socket.io-client";

const socket = openSocket("http://localhost:3000");

const LobbyLayout = (props) => {
    return (
        <div className="container">
            <div className="row">
                <div className="col-sm">

                </div>
                <div className="col-sm">
                    Your In the Lobby...
                </div>
                <div className="col-sm">

                </div>
            </div>
        </div>
    );
}

export default LobbyLayout;
