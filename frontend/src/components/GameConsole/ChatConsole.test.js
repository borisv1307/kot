import React from 'react';
import { shallow } from 'enzyme';

import ChatConsole from './ChatConsole';

describe('Verify ChatConsole layout template', () => {
    it('ChatConsole should render correctly', () => {
        const errorPage = shallow(<ChatConsole />);
        expect(errorPage).toMatchSnapshot();
    });
})