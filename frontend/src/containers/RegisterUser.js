import React, { Component } from 'react';
import { Redirect } from 'react-router-dom'
import Button from 'react-bootstrap/Button'
import "./Login.css";
import Form from "react-bootstrap/Form";

class RegisterUser extends Component {
  constructor(props){
    super(props);
    this.state={
      username:'',
      email:'',
      password:''
    }
  }

   usernameChangeHandler = (event) => {
        this.setState({
            username: event.target.value,
            redirect: false
        })
    }

    emailChangeHandler = (event) => {
        this.setState({
            email: event.target.value,
            redirect: false
        })
    }

    passwordChangeHandler = (event) => {
        this.setState({
            password: event.target.value,
            redirect: false
        })
    }

  setRedirect = () => {
      /* Add async exchange to determine login availability and eventually success/failure.
      Suggest using Auth0... example: https://auth0.com/blog/handling-authentication-in-react-with-context-and-hooks/ */
        this.setState({
            redirect: true
        })
    }

    renderRedirect = () => {
        const user = this.state.username;
        if (this.state.redirect) {
            return <Redirect to={{
                pathname: '/lobby',
                state: { username: user }
            }} />
        }
    }


  render() {
    return (
      <div>
        <Form>
            <h2>Register</h2>
            <Form.Group href="/lobby" onSubmit={() => this.props.onSubmit(this.state.username)}>
            <Form.Label>User Name</Form.Label>
           <Form.Control
             placeholder="Enter a Username"
             value={this.state.username}
             onChange = {this.usernameChangeHandler}
             />
             <Form.Label>Email</Form.Label>
           <Form.Control
             placeholder="Enter your Email"
             type="email"
             value={this.state.email}
             onChange = {this.emailChangeHandler}
             />
             <Form.Label>Password</Form.Label>
           <Form.Control
             type = "password"
             placeholder="Enter your Password"
             value={this.state.password}
             onChange = {this.passwordChangeHandler}
             />
             {this.renderRedirect()}
            </Form.Group>
            <Button variant="btn btn-secondary" onClick={this.setRedirect} className="submit" type="submit" value="Submit">Register</Button>
         </Form>
      </div>
    );
  }

}
export default RegisterUser
