import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import './index.css';
import App from './App';
import Homepage from './components/Homepage';
import About from './components/About';
import Predict from './components/Predict';
import Teams from './components/Teams';
import Predict_Win_Team from './components/Predict_Win_Team';
import Predict_Score from './components/Predict_Score';
import Predict_Select_Team from './components/Predict_Select_Team';

import * as serviceWorker from './serviceWorker';

const routing = (
  <Router>
    <Switch>
      <App>
        <Route exact path="/" component={Homepage} />
        <Route exact path="/teams" component={Teams} />
        <Route exact path="/about" component={About} />
        <Route exact path="/predict" component={Predict} />
        <Route exact path="/predict_win_team" component={Predict_Win_Team} />
        <Route exact path="/predict_score" component={Predict_Score} />
        <Route exact path="/predict_select_team" component={Predict_Select_Team} />
      </App>
    </Switch>
  </Router>
)

ReactDOM.render(routing, document.getElementById('root'));

serviceWorker.unregister();
