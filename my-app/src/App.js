import React, { Component } from 'react';
import { connect } from 'react-redux';

import { Button, List, ListItem, Card, CardContent } from '@material-ui/core'
import logo from './logo.svg';

import TasksPage from './components/TasksPage';
import FlashMessage from './components/FlashMessage';
import { createSpot, editSpot, deleteSpot, fetchSpots } from './actions';

import './App.css';

class App extends Component {

  componentDidMount() {
    this.props.dispatch(fetchSpots());
  }

  addCookie = (key, val) => {
    var dt = new Date();
    dt.setDate(dt.getDate() + 30);
    document.cookie = key + "=" + val + ";expires=" + dt.toUTCString();
  }

  onCreateSpot = ({ name, address }) => {
    this.addCookie(name, "done")
    this.props.dispatch(createSpot({ name, address }));
  };

  onStatusChange = (id, status) => {
    this.props.dispatch(editSpot(id, { status }));
  };

  onDeleteSpot = (id) => {
    this.props.dispatch(deleteSpot(id));
  };

  onCount = (device, answer) => {
    let count;
    count = 0;
    this.props.spots.forEach((item) => {
      if (item["name"]==device && item["address"]==answer) { count++ }
    });
    return count;
  };

  onClearCookie = () => {
    for (var device of ["experia1", "experia2"]) {
      document.cookie = device + "=" + ";expires=" + new Date().toUTCString();
    }
  }

  isCookieEnable = () => {
    this.addCookie("check", "done");
    return document.cookie.match(/check/) != null;
  }

  isYesNoButton = (device) => {
    var pattern = new RegExp(device);
    var result = document.cookie.match(pattern);
    return !this.isCookieEnable() || result != null;
  }

  render() {
    if (!this.isCookieEnable()) {
      return (
        <div>
          Please enable cookie.
        </div>
      );
    }

    return (
      <div>
        <Card>
          test tools
          <Button variant="contained"
          onClick={()=>this.onClearCookie()}>
            Clear Cookie
          </Button>
        </Card>
        <List>
          <ListItem>Can you activate Rakuten-SIM with...</ListItem>
          {["experia1","experia2"].map(device => (
            <ListItem>
              <Card>
                <CardContent>
                  {device}?

                  <Button variant="contained" color="primary" style={{margin:"0 15px"}}
                  disabled={this.isYesNoButton(device)}
                  onClick={()=>this.onCreateSpot({"name":device,"address":"yes"})}>
                    Yes ({this.onCount(device,"yes")})
                  </Button>

                  <Button variant="contained" color="primary" style={{margin:"0 15px"}}
                  disabled={this.isYesNoButton(device)}
                  onClick={()=>this.onCreateSpot({"name":device,"address":"no"})}>
                    No ({this.onCount(device,"no")})
                  </Button>
                </CardContent>
              </Card>
            </ListItem>
          ))}
        </List>

        {/*<div>
          {this.props.error && <FlashMessage message={this.props.error} />}
          <TasksPage
            spots={this.props.spots}
            onCreateSpot={this.onCreateSpot}
            onStatusChange={this.onStatusChange}
            onDeleteSpot={this.onDeleteSpot}
            isLoading={this.props.isLoading}
          />
        </div>*/}

      </div>
    );
  }
}

function mapStateToProps(state) {
  const { spots, isLoading, error } = state.spots;
  return { spots, isLoading, error };
}

export default connect(mapStateToProps)(App);
