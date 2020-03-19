import React, { Component } from 'react';

import { Grid, Button, TextField } from '@material-ui/core'
import { createMuiTheme } from '@material-ui/core/styles';
import { MuiThemeProvider } from 'material-ui/styles';

import { theme } from '../theme'
import TaskList from './TaskList';
import { TASK_STATUSES } from '../constants';

class TasksPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showNewCardForm: false,
    };
  }

  render() {
    if (this.props.isLoading) {
      return (
        <div>
          Loading...
        </div>
      );
    }

    return (
      <MuiThemeProvider theme={theme}>
        <div>
          <div style={{ margin: "25px 20px 25px 20px" }}>
            <Button variant="contained" color="primary" style={{margin:"10px 0"}}
              onClick={()=>this.setState({ showNewCardForm: !this.state.showNewCardForm })}>
              ＋スポット追加
            </Button>
            {
              this.state.showNewCardForm &&
              <AddTaskForm onCreateTask={this.props.onCreateTask}
                onCreateSpot={this.props.onCreateSpot}
              />
            }
          </div>
          <div>
            <div style={{ margin: "25px 20px 25px 20px" }}>
              <h2>投稿一覧</h2>
              <TaskList
                spots={this.props.spots}
                // onStatusChange={this.props.onStatusChange}
                onDeleteSpot={this.props.onDeleteSpot}
              />
            </div>
          </div>
        </div>
      </MuiThemeProvider>
    );
  }
}

export default TasksPage;


class AddTaskForm extends Component {
  componentDidMount() {
    // To disabled submit button at the beginning.
    //this.props.form.validateFields();
  }

  constructor(props) {
    super(props);
    this.state = {
      name: "NoName",
      address: "NoAddress",
    };
  }

  handleSubmit = e => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {
      if (!err) {
        console.log('Received values of form: ', values);
        this.props.onCreateSpot(values)
      }
    });
  };

  render() {
    return (
      <MuiThemeProvider theme={theme}>
        <form noValidate autoComplete="off">
          <Grid container>
            <Grid item xs={4}>
              <TextField id="filled-basic" label="Name" variant="outlined"
                onChange={e=>{this.setState({name:e.target.value});
              }}
              />
            </Grid>
            <Grid item xs={4}>
              <TextField id="filled-basic" label="Address" variant="outlined"
                onChange={e=>{this.setState({address:e.target.value})}}
              />
            </Grid>
            <Grid item xs={4}>
              <Button variant="contained" color="primary"
              onClick={()=>{
                this.props.onCreateSpot({name:this.state.name,address:this.state.address})
              }}
              >
              post
              </Button>
            </Grid>
          </Grid>
        </form>
      </MuiThemeProvider>
    );
  }
}

//const WrappedAddTaskForm = Form.create({ name: 'add_task_form' })(AddTaskForm);
