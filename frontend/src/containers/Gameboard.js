import React from 'react';
import "antd/dist/antd.css";
import "./Gameboard.css";
import { Layout } from 'antd';

import GameLog from './../components/Logs/GameLog'
import DiceRoller from './../components/Dice/DiceRoller'

const { Header, Footer, Sider, Content } = Layout;

const GameboardLayout = (props) => {
    return (
        <div>
            <Layout>
                <Header></Header>
                <Layout>
                    <Sider>
                        <DiceRoller />
                    </Sider>
                    <Content>
                        <GameLog />
                    </Content>
                    <Sider></Sider>
                </Layout>
                <Footer></Footer>
            </Layout>
        </div>
    );
}

export default GameboardLayout;


