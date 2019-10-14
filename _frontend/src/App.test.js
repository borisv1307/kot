import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});


// import React from 'react';
// import { shallow } from 'enzyme';
// import App from './App';

// it('renders without crashing', () => {
//   shallow(<App />);
// });

// // hello.test.js, again

// import React from "react";
// import { ReactDOM, render, unmountComponentAtNode } from "react-dom";
// import { act } from "react-dom/test-utils";
// // import pretty from "pretty";

// import App from "./App";

// let container = null;
// beforeEach(() => {
//   // setup a DOM element as a render target
//   container = document.createElement("div");
//   document.body.appendChild(container);
// });

// afterEach(() => {
//   // cleanup on exiting
//   unmountComponentAtNode(container);
//   container.remove();
//   container = null;
// });

// it("should render a greeting", () => {
//   act(() => {
//     render(<App />, container);
//   });

//   expect(
//     pretty(container.innerHTML)
//   ).toMatchInlineSnapshot(); /* ... gets filled automatically by jest ... */

//   // act(() => {
//   //     render(<Hello name="Jenny" />, container);
//   // });

//   // expect(
//   //     pretty(container.innerHTML)
//   // ).toMatchInlineSnapshot(); /* ... gets filled automatically by jest ... */

//   // act(() => {
//   //     render(<Hello name="Margaret" />, container);
//   // });

//   // expect(
//   //     pretty(container.innerHTML)
//   // ).toMatchInlineSnapshot(); /* ... gets filled automatically by jest ... */
// });

