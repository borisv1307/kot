import React from 'react';
import { shallow } from 'enzyme';

import GameboardLayout from './Gameboard';

describe('Verify gameboard layout template', () => {
  it('Gameboard should render correctly', () => {
    const errorPage = shallow(<GameboardLayout />);
    expect(errorPage).toMatchSnapshot();
  });
})