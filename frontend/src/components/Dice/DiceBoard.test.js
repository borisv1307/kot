import React from 'react';
import { shallow } from 'enzyme';

import DiceBoard from './DiceBoard';

describe('Verify DiceBoard layout template', () => {
    it('DiceBoard should render correctly', () => {
        const errorPage = shallow(<DiceBoard />);
        expect(errorPage).toMatchSnapshot();
    });
})