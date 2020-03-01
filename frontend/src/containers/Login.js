import React, { Component } from "react";
import { Redirect } from "react-router-dom";
import Button from "react-bootstrap/Button";
import "./Login.css";
import Form from "react-bootstrap/Form";
import RegisterUser from "./RegisterUser";

export default class LoginLayout extends Component {
  constructor(props) {
    super(props);

    let user = "";
    let password = "";
    if (props.location && props.location.state) {
      user = "Guest_" + Math.floor(Math.random() * 10000 + 1);
    }

    this.state = {
      redirect: false,
      username: user,
      userPassword: password
    };
  }

  usernameChangeHandler = event => {
    this.setState({
      username: event.target.value,
      redirect: false
    });
  };

  passwordChangeHandler = event => {
    this.setState({
      userPassword: event.target.value,
      redirect: false
    });
  };

  setRedirect = () => {
    this.setState({
      redirect: true
    });
  };

  renderRedirect = () => {
    const user = this.state.username;
    if (this.state.redirect) {
      return (
        <Redirect
          to={{
            pathname: "/lobby",
            state: { username: user }
          }}
        />
      );
    }
  };

  render() {
    return (
      <div className="container">
        <h1>Welcome to KoT</h1>
        <br />
        <div className="row">
          <div className="col-sm p-4">
            <div className="login">
              <Form className="login">
                <h2>Login to Join a Game</h2>
                <Form.Group
                  href="/lobby"
                  onSubmit={() => this.props.onSubmit(this.state.username)}
                >
                  <Form.Label>Username</Form.Label>
                  <Form.Control
                    type="text"
                    onChange={this.usernameChangeHandler}
                    placeholder="Enter your Username"
                    value={this.state.username}
                    required
                  />
                  <Form.Label>Password</Form.Label>
                  <Form.Control
                    type="password"
                    onChange={this.passwordChangeHandler}
                    placeholder="Enter your Password"
                    value={this.state.password}
                    required
                  />
                  {this.renderRedirect()}
                </Form.Group>
                <Button
                  variant="btn btn-secondary"
                  onClick={this.setRedirect}
                  className="submit"
                  type="submit"
                  value="Submit"
                >
                  Login
                </Button>
              </Form>
            </div>
          </div>
          <div className="col-sm">
            <RegisterUser />
          </div>
        </div>
      </div>
    );
  }
}
