import React from 'react';
import { shallow } from 'enzyme';

import GameLog from './GameLog';

describe('Verify GameLog layout template', () => {
    it('Verify parameter provided logs are rendered correctly', () => {

        const tLog = [
            '-- Sammy turn –',
            'Rolled: E E H 1 2 3',
            'Decision: keep E E',
            'Rolled: E P 1 2 2',
            'Decision: keep E',
            'Rolled: 2 2 2 (TRIPPLE! +2 VP)',
            ':: Gain: E E E +2 VP ::',
            'Buy: Psychic Probe',
            'End Turn'
        ];

        const component = shallow(<GameLog data={tLog} />);
        expect(component).toMatchSnapshot();
    });
})