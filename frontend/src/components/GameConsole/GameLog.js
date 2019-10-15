import React from 'react';

import "./GameLog.css";

const GameLog = (props) => {

    return (
        <div>
            {
                props.data.map(entry =>
                    <li key={entry}>{entry}</li>
                )
            }
        </div>
    );
}

export default GameLog;