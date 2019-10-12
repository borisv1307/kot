import React from 'react';
import { shallow, mount } from 'enzyme';

import Routes from './Routes';

import AppLayout from './AppLayout';
import NotFoundPage from './../components/NotFoundPage/NotFoundPage'

import { MemoryRouter } from 'react-router'
import { Route } from 'react-router-dom';

describe('routes using memory router', () => {
  it('should show Home component for / router (using memory router)', () => {
    const component = mount( <MemoryRouter initialEntries = {['/']} >
        <Routes/>
      </MemoryRouter>
    );
    expect(component.find(AppLayout)).toHaveLength(1);
  })
  it('should show No match component for route not defined', () => {
    const component = mount( <MemoryRouter initialEntries = {['/unknown']} >
        <Routes/>
      </MemoryRouter>
    );
    expect(component.find(NotFoundPage)).toHaveLength(1);
  })
})