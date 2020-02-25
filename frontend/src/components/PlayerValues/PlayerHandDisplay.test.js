import React from "react";
import { shallow } from "enzyme";

import PlayerHandDisplay from "./PlayerHandDisplay";

describe("Verify PlayerHandDisplay layout template", () => {
  const test_player_details = [
    {
      name: "howdy",
      cost: 1,
      effect: 0,
      footnote: 2
    },
    {
      name: "ya",
      victory_points: 5,
      health: 5,
      footnote: 4
    },
    {
      name: "all",
      cost: 10,
      health: 10,
      footnote: 6
    }
  ];

  const json_test_player_details = JSON.stringify(test_player_details);

  const test_username = "test_user";
  const test_roomname = "test_room";

  const expected_state_values = {
    username: test_username,
    gameRoom: test_roomname,
    data: test_player_details
  };

  it("Verify parameter provided PlayeValues are rendered correctly", () => {
    const component = shallow(
      <PlayerHandDisplay
        currentUser={test_username}
        currentRoom={test_roomname}
        data={json_test_player_details}
      />
    );
    expect(component).toMatchSnapshot();
  });

  it("Verify state transfers via props as expected", () => {
    const wrapper = shallow(
      <PlayerHandDisplay
        currentUser={test_username}
        currentRoom={test_roomname}
        data={json_test_player_details}
      />
    );
    expect(wrapper.state()).toEqual({ ...expected_state_values }); // passed
  });

  it("verify default states are as expected", () => {
    const wrapper = shallow(
      <PlayerHandDisplay
        currentUser={test_username}
        currentRoom={test_roomname}
        data={JSON.stringify([])}
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
  });
});
