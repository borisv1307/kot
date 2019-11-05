import React from 'react';
import "./Login.css";

const LoginLayout = (props) => {
    return (
        <div className="container">
            <div className="row">
                <div className="col-sm">

                </div>
                <div className="col-sm">
                    Login page
                </div>
                <div className="col-sm">

                </div>
            </div>
            <div className="row">
                <div className="col-sm">

                </div>
                <div className="col-sm">
                    <br></br>
                    <a className="b" href="/lobby">
                        <button type="button" class="btn btn-primary">Play as Guest</button>
                    </a>
                </div>
                <div className="col-sm">

                </div>
            </div>
        </div>
    );
}

export default LoginLayout;


