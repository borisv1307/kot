import React from 'react';
import { shallow } from 'enzyme';

import CardStore from './CardStore';

describe('Verify CardStore layout template', () => {
    it('Verify parameter provided cards are rendered correctly', () => {

        const card = [
            { name: 'Armor Plating', cost: 4, type: 'Keep', effect: 'Ignore damage of 1', footnote: ' ' },
            { name: 'Commuter Train', cost: 4, type: 'Discard', effect: 'Gain 2 victory points', footnote: ' ' },
            { name: 'Giant Brain', cost: 5, type: 'Keep', effect: 'You have one extra reroll each turn', footnote: ' ' }
        ];

        const component = shallow(<CardStore data={card} />);
        expect(component).toMatchSnapshot();
    });
})