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

describe('Verify site layout template', () => {
    it('General layout should render correctly', () => {
        const errorPage = shallow(<AppLayout />);
        expect(errorPage).toMatchSnapshot();
    });

    it('renders lobby menu', () => {
        const wrapper = shallow(<AppLayout />);

        const login_menu = <li className="nav-item">
            <a className="nav-link" href="/login">Login</a>
        </li>

        const lobby_menu = <li className="nav-item">
            <a className="nav-link" href="/lobby">Lobby <span className="sr-only">(current)</span></a>
        </li>

        const game_menu = <li className="nav-item">
            <a className="nav-link" href="/game">Play KoT</a>
        </li>

        expect(wrapper).toContainReact(login_menu);
        expect(wrapper).toContainReact(lobby_menu);
        expect(wrapper).toContainReact(game_menu);
    });
})