import React from 'react';

import { List, Typography } from 'antd';
import "./DiceBoard.css";

const DiceBoard = (props) => {
    return (
        <div>
            <List
                // header={<div>Header</div>}
                // footer={<div>Footer</div>}
                bordered
                dataSource={props.data}
                renderItem={item => (
                    <List.Item>
                        {item}
                    </List.Item>
                )}
            />
        </div>
    );
}


export default DiceBoard;