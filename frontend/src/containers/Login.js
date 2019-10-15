import React from 'react';
import "antd/dist/antd.css";
import "./Login.css";
import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

const LoginLayout = (props) => {
    return (
        <div>
            <Layout>
                <Header></Header>
                <Layout>
                    <Sider></Sider>
                    <Content>Login page</Content>
                    <Sider></Sider>
                </Layout>
                <Footer></Footer>
            </Layout>
        </div>
    );
}

export default LoginLayout;


