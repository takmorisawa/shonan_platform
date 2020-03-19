import React, { Component } from 'react';
import { connect } from 'react-redux';

import { List, ListItem } from '@material-ui/core'
import logo from './logo.svg';

import TasksPage from './components/TasksPage';
import FlashMessage from './components/FlashMessage';
import { createSpot, editSpot, deleteSpot, fetchSpots } from './actions';

import './App.css';

class App extends Component {

  componentDidMount() {
    this.props.dispatch(fetchSpots());
  }

  onCreateSpot = ({ name, address }) => {
    this.props.dispatch(createSpot({ name, address }));
  };

  onStatusChange = (id, status) => {
    this.props.dispatch(editSpot(id, { status }));
  };

  onDeleteSpot = (id) => {
    this.props.dispatch(deleteSpot(id));
  };

  render() {
    return (
      <div>
        <div>
          {this.props.error && <FlashMessage message={this.props.error} />}
          <TasksPage
            spots={this.props.spots}
            onCreateSpot={this.onCreateSpot}
            onStatusChange={this.onStatusChange}
            onDeleteSpot={this.onDeleteSpot}
            isLoading={this.props.isLoading}
          />
        </div>
      </div>
    );
  }
}

function mapStateToProps(state) {
  const { spots, isLoading, error } = state.spots;
  return { spots, isLoading, error };
}

export default connect(mapStateToProps)(App);
