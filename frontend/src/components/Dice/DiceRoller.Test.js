import React from 'react';
import { shallow } from 'enzyme';

import DiceRoller from './DiceRoller';

describe('Verify DiceRoller layout template', () => {
    it('DiceRoller should render correctly', () => {
        const errorPage = shallow(<DiceRoller />);
        expect(errorPage).toMatchSnapshot();
    });

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
            'energy',];

        const component = shallow(<TurnLogs data={tLog} />);
        expect(component).toMatchSnapshot();
    });
})