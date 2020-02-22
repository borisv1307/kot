import React from "react";
import { shallow } from "enzyme";

import LobbyListDisplay from "./LobbyListDisplay";

describe("Verify LobbyListDisplay layout template", () => {
  const test_player_details = [
    {
      room_name: "room 1",
      users: ["edward", "marv", "bill", "gus"]
    },
    {
      room_name: "room 2",
      users: ["edward", "marv", "bill", "gus"]
    },
    {
      room_name: "room 3",
      users: ["edward", "marv", "bill", "gus"]
    }
  ];

  const test_username = "test_user";
  const test_roomname = "test_room";

  const expected_state_values = {
    redirect: false,
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

  it("gameListResponseHandler method updates state as expected", () => {
    const test_player_callback_details = {
      Room_8684: [
        {
          username: "Guest_1234",
          current_health: 10,
          location: "Out",
          is_alive: true,
          victory_points: 0,
          energy: 0,
          cards: []
        }
      ],
      Room_1234: [
        {
          username: "Guest_1234",
          current_health: 10,
          location: "Out",
          is_alive: true,
          victory_points: 0,
          energy: 0,
          cards: []
        }
      ]
    };

    const wrapper = shallow(
      <LobbyListDisplay
        currentUser={test_username}
        currentRoom={test_roomname}
        data={[]}
      />
    );

    const expected_state_values_with_no_player_details = {
      redirect: false,
      username: test_username,
      gameRoom: test_roomname,
      data: []
    };

    const expected_backend_callback_message = {
      user: test_username,
      room: test_roomname,
      content: JSON.stringify(test_player_callback_details)
    };

    wrapper
      .instance()
      .gameListResponseHandler(expected_backend_callback_message);

    expect(wrapper.state()).toEqual({
      ...expected_state_values_with_no_player_details
    });
  });
});
