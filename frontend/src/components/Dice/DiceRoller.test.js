import React from "react";
import { shallow } from "enzyme";

import * as Constants from "../../constants";

import fetch from "isomorphic-fetch";

import DiceRoller from "./DiceRoller";

describe("Verify DiceRoller layout template", () => {
  it("DiceRoller should render correctly", () => {
    const errorPage = shallow(<DiceRoller />);
    expect(errorPage).toMatchSnapshot();
  });
});

test("default state expected to be..", done => {
  const wrapper = shallow(<DiceRoller />);

  expect(wrapper.state()).toEqual({
    rolledDice: [],
    selectedDice: [],
    allowReroll: true
  }); // passed

  done();
});

test("set state expected to..", done => {
  const wrapper = shallow(<DiceRoller />);

  expect(wrapper.state()).toEqual({
    rolledDice: [],
    selectedDice: [],
    allowReroll: true
  }); // passed

  wrapper.setState(
    {
      rolledDice: ["", ""],
      selectedDice: ["", "", "", ""],
      allowReroll: false
    },
    () => {
      expect(wrapper.state()).toEqual({
        rolledDice: ["", ""],
        selectedDice: ["", "", "", ""],
        allowReroll: false
      }); // passed

      done();
    }
  );
});

it("CalculateRerollCount() expect 2", () => {
  const wrapper = shallow(<DiceRoller />);

  wrapper.setState({
    rolledDice: ["", "", "", "", ""],
    selectedDice: ["", "", ""],
    allowReroll: false
  });

  const actual = wrapper.instance().CalculateRerollCount();

  expect(actual).toEqual(2);
});

it("selectedDiceCallback(selectedDice) expect state.selectedDice to be set", () => {
  const wrapper = shallow(<DiceRoller />);

  wrapper.setState({
    rolledDice: [],
    selectedDice: [],
    allowReroll: true
  });

  const actual = ["", "", "", ""];

  wrapper.instance().selectedDiceCallback(actual);

  expect(wrapper.state()).toEqual({
    rolledDice: [],
    selectedDice: actual,
    allowReroll: true
  });
});

test("should update a state on a next line", () => {
  const wrapper = shallow(<DiceRoller />);

  wrapper.setState({
    rolledDice: [],
    selectedDice: [],
    allowReroll: false
  });

  expect(wrapper.state()).toEqual({
    rolledDice: [],
    selectedDice: [],
    allowReroll: false
  }); // passed
});
