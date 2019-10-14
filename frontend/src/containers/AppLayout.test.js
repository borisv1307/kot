import React from 'react';
import { shallow } from 'enzyme';

import AppLayout from './AppLayout';

// verify lobby and play ToK
import {
    BrowserRouter as Router,
    Route,
    Link,
    Switch
} from 'react-router-dom';

import { Layout, Menu, Icon, Breadcrumb } from 'antd';

describe('Verify site layout template', () => {
    it('General layout should render correctly', () => {
        const errorPage = shallow(<AppLayout />);
        expect(errorPage).toMatchSnapshot();
    });

    it('renders lobby menu', () => {
        const wrapper = shallow(<AppLayout />);
        const lobby_menu = <Menu
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
        </Menu>;
        // expect(wrapper.contains(welcome)).toBe(true);
        // expect(wrapper.contains(welcome)).toEqual(true);
        expect(wrapper).toContainReact(lobby_menu);
    });

    it('renders lobby menu', () => {
        const wrapper = shallow(<AppLayout />);
        const lobby_menu = <Menu
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
        </Menu>;
        // expect(wrapper.contains(welcome)).toBe(true);
        // expect(wrapper.contains(welcome)).toEqual(true);
        expect(wrapper).toContainReact(lobby_menu);
    });
})