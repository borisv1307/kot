import React from 'react';
import { shallow } from 'enzyme';

import DiceRoller from './DiceRoller';

describe('Verify DiceRoller layout template', () => {
    it('DiceRoller should render correctly', () => {
        const errorPage = shallow(<DiceRoller />);
        expect(errorPage).toMatchSnapshot();
    });
})