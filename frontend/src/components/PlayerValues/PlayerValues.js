import React from 'react';
import Heart from './../Images/Heart.gif'
import Star from './../Images/Star.png'
import Energy from './../Images/Energy.png'

import "./PlayerValues.css";

class PlayerValues extends React.Component {
    state = {
        victory_points: 0,
        health: 10,
        energy: 0,
        position: 'Out'
    }

    render() {

        return (
            <div>
                <div className="player-border">
                    <h2>Player A </h2>
                    <div className="player-values">
                        <p>Victory Points: <span className="badge badge-light">{this.state.victory_points}</span><img src={Star}></img></p>
                        <p>Health: <span className="badge badge-light">{this.state.health}</span><img src={Heart}></img></p>
                        <p>Energy: <span className="badge badge-light">{this.state.energy}</span><img src={Energy}></img></p>
                        <p>In/Out of Tokyo: <span className="badge badge-warning">{this.state.position}</span></p>
                    </div>
                </div>
            </div>
        );
    }
}

export default PlayerValues;