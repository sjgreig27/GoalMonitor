import {createBrowserHistory} from 'history';
import {applyMiddleware, combineReducers, createStore} from "redux";
import {routerMiddleware, connectRouter} from "connected-react-router";


export const history = createBrowserHistory();
const middleware = routerMiddleware(history);

const reducers = combineReducers({router: connectRouter(history)});

export const store = createStore(reducers, applyMiddleware(middleware));

export default store

