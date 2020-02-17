import React, { Component } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import GameboardLayout from "./Gameboard";
import LobbyLayout from "./Lobby";
import LoginLayout from "./Login";
import NotFoundPage from "./../components/NotFoundPage/NotFoundPage";

import "./AppLayout.css";

class AppLayout extends Component {
  state = {
    collapsed: false
  };

  onCollapse = collapsed => {
    this.setState({ collapsed });
  };

  toggle = () => {
    this.setState({
      collapsed: !this.state.collapsed
    });
  };

  render() {
    return (
      <Router>
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <a className="navbar-brand" href="/login">
            Home
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarNavDropdown"
            aria-controls="navbarNavDropdown"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNavDropdown">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="nav-link" href="/login">
                  Login
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/lobby">
                  Lobby <span className="sr-only">(current)</span>
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/game">
                  Play KoT
                </a>
              </li>
            </ul>
          </div>
        </nav>
        <Switch>
          <Route exact path="/" component={LobbyLayout} />
          <Route path="/login" component={LoginLayout} />
          <Route path="/game" component={GameboardLayout} />
          <Route path="/lobby" component={LobbyLayout} />
          <Route component={NotFoundPage} />
        </Switch>
      </Router>
    );
  }
}

export default AppLayout;
