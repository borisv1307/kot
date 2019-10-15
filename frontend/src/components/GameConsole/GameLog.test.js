import React from 'react';
import { shallow } from 'enzyme';

import GameLog from './GameLog';

describe('Verify GameLog layout template', () => {
    it('GameLog should render correctly', () => {
        const errorPage = shallow(<GameLog />);
        expect(errorPage).toMatchSnapshot();
    });

    it('Verify parameter provided logs are rendered correctly', () => {
        // class FaceValues(enum):
        // One = 0
        // Two = 1
        // Three = 2
        // Attack = 3
        // Heart = 4
        // Energy = 5

        const tLog = [
            '1',
            '2',
            '3',
            'attack',
            'heal',
            'energy',];

        const component = shallow(<Gamelog data={tLog} />);
        expect(component).toMatchSnapshot();
    });
})