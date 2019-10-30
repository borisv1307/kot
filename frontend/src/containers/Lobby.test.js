import React from 'react';
import { shallow } from 'enzyme';

import LoginLayout from './Lobby';

describe('Verify lobby template', () => {
  it('Lobby should render correctly', () => {
    const errorPage = shallow(<LoginLayout />);
    expect(errorPage).toMatchSnapshot();
  });
})