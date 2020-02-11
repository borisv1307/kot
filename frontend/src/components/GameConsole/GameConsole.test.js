import React from "react";
import { shallow } from "enzyme";

import GameConsole from "./GameConsole";

describe("Verify GameConsole layout template", () => {
  it("GameConsole should render correctly", () => {
    const errorPage = shallow(<GameConsole />);
    expect(errorPage).toMatchSnapshot();
  });
});

describe("<GameConsole />", () => {
  const expected_user = "user_name";
  const expected_room = "room_name";
  const expected_cmd = "something_commandish";

  const testValues = {
    currentUser: expected_user,
    currentRoom: expected_room,
    cmd: expected_cmd,
    sendMessage: jest.fn(),
    hideMudUi: false
  };

  it("Submit works", () => {
    const component = shallow(<GameConsole {...testValues} />);

    component.setState({
      log: [],
      hideMudUi: false
    });

    const button = component.find("#send_button");
    expect(button.length).toBe(1);
    button.simulate("click");
    expect(testValues.sendMessage).toHaveBeenCalled();
    expect(testValues.sendMessage).toBeCalledWith({
      command: "gamelog_send_request",
      user: expected_user,
      room: expected_room,
      payload: expected_cmd
    });
  });
});
