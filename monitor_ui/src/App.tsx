import * as React from 'react';
import './App.css';
import {Provider} from 'react-redux';
import {Switch, Route} from 'react-router-dom';
import {LandingPage} from './pages';
import {store, history} from "./store";
import {ConnectedRouter} from 'connected-react-router'

class App extends React.Component {
  public render() {
    return (
        <Provider store={store}>
          <ConnectedRouter history={history}>
            <Switch>
                <Route exact path={'/goal_monitor/'} component={LandingPage}/>
            </Switch>
          </ConnectedRouter>
        </Provider>
    )
  }
}

export default App;
