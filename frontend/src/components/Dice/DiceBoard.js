import React from 'react';

import "./DiceBoard.css";

const DiceBoard = (props) => {
    return (
        <div>
            {
                props.data.map(dice =>
                    <li key={dice}>{dice}</li>
                )
            }
        </div>
    );
};

export default DiceBoard;