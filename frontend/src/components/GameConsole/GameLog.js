import React from 'react';

import { List } from 'antd';
import "./GameLog.css";

const GameLog = (props) => {
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


export default GameLog;