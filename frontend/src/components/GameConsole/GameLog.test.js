import React from 'react';
import { shallow } from 'enzyme';

import GameLog from './GameLog';

describe('Verify GameLog layout template', () => {
    it('Verify parameter provided logs are rendered correctly', () => {

        const tLog = [];

        const component = shallow(<GameLog data={tLog} />);
        expect(component).toMatchSnapshot();
    });
})