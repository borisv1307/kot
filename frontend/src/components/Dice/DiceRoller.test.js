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

describe("Verify DiceRoller", () => {
  const test_username = "test_user";
  const test_roomname = "test_room";

  it("default state expected to be..", done => {
    const wrapper = shallow(
      <DiceRoller currentUser={test_username} currentRoom={test_roomname} />
    );

    expect(wrapper.state()).toEqual({
      username: test_username,
      gameRoom: test_roomname,
      currentTurnUser: "",
      rolledDice: [],
      selectedDice: [],
      allowReroll: true,
      allowEndTurn: false,
      diceAccepted: false,
      its_my_turn: false
    });

    done();
  });

  it("set state expected to..", done => {
    const wrapper = shallow(
      <DiceRoller currentUser={test_username} currentRoom={test_roomname} />
    );

    expect(wrapper.state()).toEqual({
      username: test_username,
      gameRoom: test_roomname,
      currentTurnUser: "",
      rolledDice: [],
      selectedDice: [],
      allowReroll: true,
      allowEndTurn: false,
      diceAccepted: false,
      its_my_turn: false
    });

    wrapper.setState(
      {
        username: test_username,
        gameRoom: test_roomname,
        rolledDice: ["", ""],
        selectedDice: ["", "", "", ""],
        allowReroll: true,
        allowEndTurn: false,
        diceAccepted: false,
        its_my_turn: false,
        currentTurnUser: ""
      },
      () => {
        expect(wrapper.state()).toEqual({
          username: test_username,
          gameRoom: test_roomname,
          rolledDice: ["", ""],
          selectedDice: ["", "", "", ""],
          allowReroll: true,
          allowEndTurn: false,
          diceAccepted: false,
          its_my_turn: false,
          currentTurnUser: ""
        });

        done();
      }
    );
  });

  it("CalculateRerollCount() expect 2", () => {
    const wrapper = shallow(
      <DiceRoller currentUser={test_username} currentRoom={test_roomname} />
    );

    wrapper.setState({
      username: test_username,
      gameRoom: test_roomname,
      rolledDice: ["", "", "", "", ""],
      selectedDice: ["", "", ""],
      allowReroll: true,
      allowEndTurn: false,
      diceAccepted: false,
      its_my_turn: false,
      currentTurnUser: ""
    });

    const actual = wrapper.instance().CalculateRerollCount();

    expect(actual).toEqual(2);
  });

  it("selectedDiceCallback(selectedDice) expect state.selectedDice to be set", () => {
    const wrapper = shallow(
      <DiceRoller currentUser={test_username} currentRoom={test_roomname} />
    );

    wrapper.setState({
      username: test_username,
      gameRoom: test_roomname,
      rolledDice: [],
      selectedDice: [],
      allowReroll: true,
      allowEndTurn: true,
      diceAccepted: false,
      its_my_turn: false,
      currentTurnUser: ""
    });

    const actual = ["", "", "", ""];

    wrapper.instance().selectedDiceCallback(actual);

    expect(wrapper.state()).toEqual({
      username: test_username,
      gameRoom: test_roomname,
      rolledDice: [],
      selectedDice: actual,
      allowReroll: true,
      allowEndTurn: true,
      diceAccepted: false,
      its_my_turn: false,
      currentTurnUser: ""
    });
  });

  test("should update a state on a next line", () => {
    const wrapper = shallow(
      <DiceRoller currentUser={test_username} currentRoom={test_roomname} />
    );
    wrapper.setState({
      username: test_username,
      gameRoom: test_roomname,
      rolledDice: [],
      selectedDice: [],
      allowReroll: false,
      allowEndTurn: true,
      diceAccepted: false,
      its_my_turn: false,
      currentTurnUser: ""
    });

    expect(wrapper.state()).toEqual({
      username: test_username,
      gameRoom: test_roomname,
      rolledDice: [],
      selectedDice: [],
      allowReroll: false,
      allowEndTurn: true,
      diceAccepted: false,
      its_my_turn: false,
      currentTurnUser: ""
    });
  });
});
