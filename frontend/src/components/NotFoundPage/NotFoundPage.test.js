import React from 'react';
import { shallow } from 'enzyme';

import NotFoundPage from './NotFoundPage';

describe('Verify 404 default error page', () => {
    it('NoFoundPage should render correctly', () => {
        const errorPage = shallow(<NotFoundPage />);
        expect(errorPage).toMatchSnapshot();
    });
})