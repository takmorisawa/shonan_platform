import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
// import * as serviceWorker from './serviceWorker';

import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { Provider } from 'react-redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import spotsReducer from './reducers';

// ReactDOM.render(<App />, document.getElementById('root'));
// serviceWorker.unregister();

const rootReducer = (state = {}, action) => {
  return {
    spots: spotsReducer(state.spots, action),
  };
};
const store = createStore(
  rootReducer,
  composeWithDevTools(applyMiddleware(thunk))
);

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
