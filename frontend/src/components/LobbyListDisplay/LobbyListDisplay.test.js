import React from "react";
import { shallow } from "enzyme";

import LobbyListDisplay from "./LobbyListDisplay";

describe("Verify LobbyListDisplay layout template", () => {
  const test_player_details = [
    {
      users: ["edward", "marv", "bill", "gus"],
      room_name: "room 1"
    },
    {
      users: ["edward", "marv", "bill", "gus"],
      room_name: "room 2"
    },
    {
      users: ["edward", "marv", "bill", "gus"],
      room_name: "room 3"
    }
  ];

  const test_username = "test_user";
  const test_roomname = "test_room";

  const expected_state_values = {
    username: test_username,
    gameRoom: test_roomname,
    data: test_player_details
  };

  it("Verify parameter provided PlayeValues are rendered correctly", () => {
    const component = shallow(
      <LobbyListDisplay
        currentUser={test_username}
        currentRoom={test_roomname}
        data={test_player_details}
      />
    );
    expect(component).toMatchSnapshot();
  });

  it("Verify state transfers via props as expected", () => {
    const wrapper = shallow(
      <LobbyListDisplay
        currentUser={test_username}
        currentRoom={test_roomname}
        data={test_player_details}
      />
    );
    expect(wrapper.state()).toEqual({ ...expected_state_values }); // passed
  });

  it("playerUpdateHandler mehthod updates state as expected", () => {
    const wrapper = shallow(
      <LobbyListDisplay
        currentUser={test_username}
        currentRoom={test_roomname}
        data={[]}
      />
    );

    const expected_state_values_with_no_player_details = {
      username: test_username,
      gameRoom: test_roomname,
      data: []
    };

    expect(wrapper.state()).toEqual({
      ...expected_state_values_with_no_player_details
    });

    const expected_backend_callback_message = {
      user: test_username,
      room: test_roomname,
      content: JSON.stringify(test_player_details)
    };

    wrapper.instance().playerUpdateHandler(expected_backend_callback_message);

    expect(wrapper.state()).toEqual({ ...expected_state_values }); // passed
  });
});
