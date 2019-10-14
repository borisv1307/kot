import React, { Component } from 'react';
import {
    BrowserRouter as Router,
    Route,
    Switch
} from 'react-router-dom';

import AppLayout from './AppLayout';
import NotFoundPage from './../components/NotFoundPage/NotFoundPage'

class Routes extends Component {
    render() {
        return (
            <div>
                <Router>
                    <div>
                        <Switch>
                            <Route exact path="/" component={AppLayout} />
                            <Route component={AppLayout} />
                        </Switch>
                    </div>
                </Router>
            </div>
        )
    }
}

export default Routes;