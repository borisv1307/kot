import React from "react";
import { shallow } from "enzyme";

import PlayerValues from "./PlayerValues";

describe("Verify player value template", () => {
  it("Player values should be rendered correctly", () => {
    const errorPage = shallow(<PlayerValues />);
    expect(errorPage).toMatchSnapshot();
  });

  describe("<PlayerValues />", () => {
    const expected_player_name = "player_name";
    const expected_victory_points = "victory_points";
    const expected_health = "health";
    const expected_energy = "energy";
    const expected_in_or_out_position = "in_or_out_position";

    const testValues = {
      player_name: expected_player_name,
      victory_points: expected_victory_points, // 0 to 10
      health: expected_health, // 0 to 10
      energy: expected_energy, // 0 or more
      in_or_out_position: expected_in_or_out_position // 'In' or 'Out'
    };

    it("Submit works", () => {
      const wrapper = shallow(
        <PlayerValues
          player_name={testValues.player_name}
          victory_points={testValues.victory_points} // 0 to 10
          health={testValues.health} // 0 to 10
          energy={testValues.energy} // 0 or more
          in_or_out_position={testValues.in_or_out_position} // 'In' or 'Out'
        />
      );
      expect(wrapper.state()).toEqual({ ...testValues }); // passed
    });
  });
});
