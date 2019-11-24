import React from 'react';

import "./PlayerValues.css";

class PlayerValues extends React.Component {
    state = {
        victory_points: 0,
        health: 10,
        position: 'Out'
    }

    render() {
        return (
            <div>
                <div className="player-border">
                    <h2>Player A </h2>
                    <div className="player-values">
                        <p>Victory Points: <span className="badge badge-light">{this.state.victory_points}</span></p>
                        <p>Health: <span className="badge badge-light">{this.state.health}</span></p>
                        <p>In/Out of Tokyo: <span >{this.state.position}</span></p>
                    </div>
                </div>
            </div>
        );
    }
}

export default PlayerValues;