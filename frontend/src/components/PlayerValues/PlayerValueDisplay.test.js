import React from "react";
import { shallow } from "enzyme";

import PlayerValueDisplay from "./PlayerValueDisplay";

describe("Verify PlayerValueDisplay layout template", () => {
  const test_player_details = [
    {
      username: "howdy",
      victory_points: 1,
      health: 0,
      energy: 2,
      position: "Out"
    },
    {
      username: "ya",
      victory_points: 5,
      health: 5,
      energy: 4,
      position: "In"
    },
    {
      username: "all",
      victory_points: 10,
      health: 10,
      energy: 6,
      position: "Out"
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
      <PlayerValueDisplay
        currentUser={test_username}
        currentRoom={test_roomname}
        data={test_player_details}
      />
    );
    expect(component).toMatchSnapshot();
  });

  it("Verify state transfers via props as expected", () => {
    const wrapper = shallow(
      <PlayerValueDisplay
        currentUser={test_username}
        currentRoom={test_roomname}
        data={test_player_details}
      />
    );
    expect(wrapper.state()).toEqual({ ...expected_state_values }); // passed
  });

  it("playerUpdateHandler method updates state as expected", () => {
    const wrapper = shallow(
      <PlayerValueDisplay
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
