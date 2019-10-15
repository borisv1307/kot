import React from 'react';
import { shallow } from 'enzyme';

import DiceBoard from './DiceBoard';

describe('Verify DiceBoard layout template', () => {
    it('Verify parameter provided dice are rendered correctly', () => {
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
            'energy'];

        const component = shallow(<DiceBoard data={tLog} />);
        expect(component).toMatchSnapshot();
    });
})