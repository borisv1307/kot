import React from "react";
import { shallow } from "enzyme";

import PlayerValues from "./PlayerValues";

describe("Verify player value template", () => {
  it("Player values should be rendered correctly", () => {
    const errorPage = shallow(<PlayerValues />);
    expect(errorPage).toMatchSnapshot();
  });
});
