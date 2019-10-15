import React from 'react';
import { shallow } from 'enzyme';

import GameConsole from './GameConsole';

describe('Verify GameConsole layout template', () => {
    it('GameConsole should render correctly', () => {
        const errorPage = shallow(<GameConsole />);
        expect(errorPage).toMatchSnapshot();
    });
})