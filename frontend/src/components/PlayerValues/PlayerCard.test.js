import React from "react";
import { shallow } from "enzyme";

import PlayerCard from "./PlayerCard";

describe("Verify card detail template", () => {
  it("Card details should be rendered correctly", () => {
    const errorPage = shallow(<PlayerCard />);
    expect(errorPage).toMatchSnapshot();
  });
});
