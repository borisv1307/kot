import React, { Component } from 'react';
import { Redirect } from 'react-router-dom'
import Button from 'react-bootstrap/Button'
import "./Login.css";
import Form from "react-bootstrap/Form";

class RegisterUser extends Component {
  constructor(props){
    super(props);
    this.state={
      first_name:'',
      last_name:'',
      email:'',
      password:''
    }
  }

  setRedirect = () => {
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
            <Form.Label>First Name</Form.Label>
           <Form.Control
             placeholder="Enter your First Name"
             floatingLabelText="First Name"
             onChange = {(event,newValue) => this.setState({first_name:newValue})}
             />
             <Form.Label>Last Name</Form.Label>
           <Form.Control
             placeholder="Enter your Last Name"
             floatingLabelText="Last Name"
             onChange = {(event,newValue) => this.setState({last_name:newValue})}
             />
             <Form.Label>Email</Form.Label>
           <Form.Control
             placeholder="Enter your Email"
             type="email"
             floatingLabelText="Email"
             onChange = {(event,newValue) => this.setState({email:newValue})}
             />
             <Form.Label>Password</Form.Label>
           <Form.Control
             type = "password"
             placeholder="Enter your Password"
             floatingLabelText="Password"
             onChange = {(event,newValue) => this.setState({password:newValue})}
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
