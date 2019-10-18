import React from 'react';
import "./Gameboard.css";

import GameConsole from '../components/GameConsole/GameConsole'
import DiceRoller from './../components/Dice/DiceRoller'

const GameboardLayout = (props) => {
    return (
        <div>

            <div className="container">
                <div className="row">
                    <div className="col-sm">
                        <DiceRoller />
                    </div>
                    <div className="col-sm">
                        <GameConsole />
                    </div>
                    <div className="col-sm">

                    </div>
                </div>
            </div>
        </div>
    );
}

export default GameboardLayout;


