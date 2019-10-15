import React, { Component } from 'react';
import {
    BrowserRouter as Router,
    Route,
    Link,
    Switch
} from 'react-router-dom';

import { Layout, Menu, Icon } from 'antd';

import GameboardLayout from './Gameboard';
import LobbyLayout from './Lobby';
import LoginLayout from './Login';
import NotFoundPage from './../components/NotFoundPage/NotFoundPage'

import "./AppLayout.css";

const { Header, Content, Footer } = Layout;

class AppLayout extends Component {

    state = {
        collapsed: false,
    };

    onCollapse = (collapsed) => {
        this.setState({ collapsed });
    }
    
    toggle = () => {
        this.setState({
            collapsed: !this.state.collapsed,
        });
    }

    render() {
        return (
            <Router>
                <div>
                    <Layout className="layout">
                        <Header>
                            <div className="logo" />
                            <Menu
                                theme="dark"
                                mode="horizontal"
                                defaultSelectedKeys={['1']}
                                style={{ lineHeight: '64px' }}>
                                <Menu.Item key="1">
                                    <Icon type="cluster" />
                                    <span>Lobby</span>
                                    <Link to="/lobby" />
                                </Menu.Item>
                                <Menu.Item key="2">
                                    <Icon type="desktop" />
                                    <span>Play ToK</span>
                                    <Link to="/game" />
                                </Menu.Item>
                                <Menu.Item key="3">
                                    <Icon type="login" />
                                    <span>Login</span>
                                    <Link to="/login" />
                                </Menu.Item>
                            </Menu>
                        </Header>
                        <Content style={{ margin: '24px 16px', padding: 24, background: '#fff', minHeight: 280 }}>
                            <Switch>
                                <Route exact path="/" component={LobbyLayout} />
                                <Route path="/game" component={GameboardLayout} />
                                <Route path="/lobby" component={LobbyLayout} />
                                <Route path="/login" component={LoginLayout} />
                                <Route component={NotFoundPage} />
                            </Switch>
                        </Content>
                        <Footer style={{ textAlign: 'center' }}>SE691 Software Studio - ToK</Footer>
                    </Layout>
                </div>
            </Router>
        );
    }
}

export default AppLayout;