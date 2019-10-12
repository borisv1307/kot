import React from 'react';
import "antd/dist/antd.css";
import "./Gameboard.css";
import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

const GameboardLayout = (props) => {
    return (
        <div>
            <Layout>
                <Header></Header>
                <Layout>
                    <Sider></Sider>
                    <Content>Game Goes Here</Content>
                    <Sider></Sider>
                </Layout>
                <Footer></Footer>
            </Layout>
        </div>
    );
}

export default GameboardLayout;


