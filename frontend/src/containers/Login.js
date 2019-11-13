import React, { Component } from 'react';
import { Redirect } from 'react-router-dom'
import "./Login.css";

import ChatInstance from './../services/chatService'

export default class LoginLayout extends Component {

    constructor(props) {
        super(props);
        this.state = {
            redirect: false,
            username: 'Guest_' + Math.floor((Math.random() * 10000) + 1)
        };
    }

    usernameChangeHandler = (event) => {
        this.setState({
            username: event.target.value,
            redirect: false
        })
    }

    setRedirect = () => {
        ChatInstance.connect();
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
            <div className="container">
                <div className="row">
                    <div className="col-sm">

                    </div>
                    <div className="col-sm">
                        Login Page
                </div>
                    <div className="col-sm">

                    </div>
                </div>
                <div className="row">
                    <div className="col-sm">

                    </div>
                    <div className="col-sm">

                        <div className="login">
                            <form href="/lobby" onSubmit={() => this.props.onSubmit(this.state.username)} className="form">
                                <input
                                    type="text"
                                    onChange={this.usernameChangeHandler}
                                    placeholder="Enter your Username"
                                    value={this.state.username}
                                    required />
                                {this.renderRedirect()}
                                <button onClick={this.setRedirect} className="submit" type="submit" value="Submit">Play</button>
                            </form>
                        </div>

                        {/* <br></br>
                        <a className="b" href="/lobby">
                            <button type="button" class="btn btn-primary">Play as Guest</button>
                        </a> */}
                    </div>
                    <div className="col-sm">

                    </div>
                </div>
            </div>
        );
    }
}

// const LoginLayout = (props) => {
//     return (
//         <div className="container">
//             <div className="row">
//                 <div className="col-sm">

//                 </div>
//                 <div className="col-sm">
//                     Login page
//                 </div>
//                 <div className="col-sm">

//                 </div>
//             </div>
//             <div className="row">
//                 <div className="col-sm">

//                 </div>
//                 <div className="col-sm">
//                     <br></br>
//                     <a className="b" href="/lobby">
//                         <button type="button" class="btn btn-primary">Play as Guest</button>
//                     </a>
//                 </div>
//                 <div className="col-sm">

//                 </div>
//             </div>
//         </div>
//     );
// }

//export default LoginLayout;


