import React from 'react';
import { shallow } from 'enzyme';

import DiceRoller from './DiceRoller';

// let state = {
//     rolledDice: ['1', '2', '3', '4'], // this holds the name of each list
//     selectedDice: ['1', '2', '3', '4', '5', '6'], // this holds the name of each list
//     allowReroll: true
//   };

describe('Verify DiceRoller layout template', () => {
    it('DiceRoller should render correctly', () => {
        const errorPage = shallow(<DiceRoller />);
        expect(errorPage).toMatchSnapshot();
    });
})

// test('Link changes the class when hovered', () => {
//     const wrapper = shallow(<DiceRoller />);

//     var result = [];
//     result.push(['1', true]);
//     result.push(['1', false]);

    // wrapper.find("button").simulate("onClick", {
    //     target: 
    // })
    // const component = renderer.create(
    //   <DiceRoller />,
    // );
    // let tree = component.toJSON();
    // expect(tree).toMatchSnapshot();
// });

// describe('Verify selectedDiceCallback', () => {
//     it('selectedDiceCallback should sets state selectedDice correctly', () => {
//         const errorPage = shallow(<DiceRoller />);
//         let actual = 'expected';
//         errorPage.selectedDiceCallback(actual);
//         expect(errorPage.state.selectedDice).toBe(actual);
//     });
// })

// describe('Verify SendKept', () => {
//     it('SendKept should calculate remaining roll count correctly', () => {
//         const rollerPage = shallow(<DiceRoller />);
//         let actual = rollerPage.CalculateRerollCount(state);
//         expect(actual == 2);
//     });
// })