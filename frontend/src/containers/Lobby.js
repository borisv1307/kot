import React from 'react';
import "antd/dist/antd.css";
import "./Lobby.css";
import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

const LobbyLayout = (props) => {
    return (
        <div>
            <Layout>
                <Header></Header>
                <Layout>
                    <Sider></Sider>
                    <Content>Your In the Lobby...</Content>
                    <Sider></Sider>
                </Layout>
                <Footer></Footer>
            </Layout>
        </div>
    );
}

export default LobbyLayout;


