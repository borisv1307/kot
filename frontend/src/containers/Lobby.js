import React, { Component } from 'react';
import { Redirect } from 'react-router-dom'
import "./Lobby.css";

export default class LobbyLayout extends Component {

    constructor(props) {
        super(props);
        let user = 'Guest_' + Math.floor((Math.random() * 10000) + 1);
        if (props.location.state)
            user = props.location.state.username;
        this.state = {
            redirect: false,
            username: user,
            gameRoom: 'Room_' + Math.floor((Math.random() * 10000) + 1)
        };
    }

    setRedirect = () => {
        this.setState({
            redirect: true
        })
    }

    renderRedirect = () => {
        const user = this.state.username;
        const room = this.state.gameRoom;
        if (this.state.redirect) {
            return <Redirect to={{
                pathname: '/game',
                state: {
                    username: user,
                    gameRoom: room
                }
            }} />
        }
    }

    roomChangeHandler = (event) => {
        this.setState({
            gameRoom: event.target.value,
        })
    }

    render() {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-sm">
                        {/* something in the future */}
                    </div>
                    <div className="col-sm">
                        <br></br>
                        <p>TO DO: <br />Add list of channels. MT to add a list of game rooms to be provided to this page via websocket.<br /> This also implies backend must managing channel groups.</p>

                        <label>Enter a room name (eventually select existing):
                                <input
                                id="room_input"
                                name="room_name"
                                type="text"
                                size="100"
                                onChange={this.roomChangeHandler}
                                placeholder="What chat room would you like to enter?"
                                value={this.state.gameRoom}
                                required />
                        </label>

                        <a className="b" href="/game">
                            {this.renderRedirect()}
                            <button onClick={this.setRedirect} className="btn btn-primary" type="button">Hi {this.state.username}, please click to enter room {this.state.gameRoom}</button>
                        </a>

                    </div>
                    <div className="col-sm">
                        {/* something in the future */}
                    </div>
                </div>
            </div>
        );
    }
}

// const LobbyLayout = (props) => {
//     return (
        // <div className="container">
        //     <div className="row">
        //         <div className="col-sm">

        //         </div>
        //         <div className="col-sm">
        //             <br></br>
        //             <a className="b" href="/game">
        //                 <p>TO DO: <br/>Add list of channels. MT to add a list of game rooms to be provided to this page via websocket.<br/> This also implies backend must managing channel groups.</p>
        //                 <button type="button" class="btn btn-primary">{this.state.username} CLICK TO ENTER GAME ROOM</button>
        //             </a>
        //         </div>
        //         <div className="col-sm">

        //         </div>
        //     </div>
        // </div>
//     );
// }

// export default LobbyLayout;


