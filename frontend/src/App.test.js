import React from 'react';
import ReactDOM from 'react-dom';
import { shallow } from 'enzyme';
import App from './App';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
});

describe('Verify Enzyme testing dependencies are available', () => {
  it('renders without crashing - using enzym shallow rerendering', () => {
    shallow(<App />);
  });

  // it('renders welcome message - using jest-enzyme', () => {
  //   const wrapper = shallow(<App />);
  //   const welcome = <p>Edit <code>src/App.js</code> and save to reload.</p>;
  //   // expect(wrapper.contains(welcome)).toBe(true);
  //   // expect(wrapper.contains(welcome)).toEqual(true);
  //   expect(wrapper).toContainReact(welcome);
  // });
 })