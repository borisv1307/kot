import React from 'react';
import { shallow } from 'enzyme';

import LobbyLayout from './Lobby';

describe('Verify lobby template', () => {
  it('Lobby should render correctly', () => {
    const errorPage = shallow(<LobbyLayout />);
    expect(errorPage).toMatchSnapshot();
  });
})