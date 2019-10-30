import React from 'react';
import { shallow } from 'enzyme';

import Routes from './Routes';

describe('Verify routes are reliable', () => {
    it('Verify root of site render correctly', () => {
        const errorPage = shallow(<Routes />);
        expect(errorPage).toMatchSnapshot();
    });
})