import React, { Component } from 'react';
// import { makeStyles } from '@material-ui/core/styles';
import { connect } from 'react-redux';

import { AppBar, Toolbar, IconButton, Typography, Grid, Button, GridList, GridListTile, TextField } from '@material-ui/core'
// import { MenuIcon } from '@material-ui/icons/Menu'
// import logo from './logo.svg';

// import TasksPage from './components/TasksPage';
// import FlashMessage from './components/FlashMessage';
import { createSpot, editSpot, deleteSpot, fetchSpots } from './actions';
import { SERIES_LIST, MODEL_LIST } from './constants'

import './App.css';

// const useStyles = makeStyles((theme) => ({
//   root: {
//     flexGrow: 1,
//   },
//   button: {
//     padding: theme.spacing(1),
//     textAlign: 'center',
//     color: theme.palette.text.secondary,
//   },
// }));

class App extends Component {

  componentDidMount() {
    this.props.dispatch(fetchSpots());
  }

  constructor(props) {
    super(props);
    this.state = {
      viewMode: "TOP_VIEW",
      selectedSeries: "",
      selectedModel: "",
      taskMode: ""
    }
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


  addCookie = (key, val) => {
    var dt = new Date();
    dt.setDate(dt.getDate() + 30);
    document.cookie = key + "=" + val + ";expires=" + dt.toUTCString();
  }

  onCountAnswer = (device, answer) => {
    var count = 0;
    // this.props.spots.forEach((item) => {
    //   if (item["name"]==device && item["address"]==answer) { count++ }
    // });
    return count;
  };

  onClearCookie = () => {
    for (var model of MODEL_LIST) {
      document.cookie = model["name"] + "=;expires=" + new Date().toUTCString();
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

  renderNavigateButton = (content, view, task) => {
    return (
      <Button variant="contained" color="primary" style={{margin: "auto", textAlign: "center"}}
      onClick={()=>this.setState({ viewMode: view, taskMode: task })}
      >
        {content}
      </Button>
    );
  }

  renderAnswerButton = (device, answer) => {
    return (
      <Button variant="contained" color="primary"
      disabled={this.isYesNoButton(device)}
      onClick={()=>this.onCreateSpot({"name":device,"address":answer})}>
        {answer} ({this.onCountAnswer(device, answer)})
      </Button>
    );
  }


  renderModeSelect = () => {
    return (
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Typography variant="h6">この端末って楽天SIMが使えるの？</Typography>
        </Grid>
        <Grid item xs={3} style={{textAlign: "center"}}>
          {this.renderNavigateButton("入力", "SERIES_SELECTING_VIEW", "REPORT_TASK")}
        </Grid>
        <Grid item xs={3} style={{textAlign: "center"}}>
          {this.renderNavigateButton("閲覧", "SERIES_SELECTING_VIEW", "SUMMURY_TASK")}
        </Grid>
      </Grid>
    );
  }

  renderSeriesSelect = (seriesList) => {
    var cols = seriesList.length < 3 ? seriesList.length : 3;
    return (
      <GridList cols={cols} cellHeight={50}>
        <GridListTile cols={cols}>
          <Typography variant="h6">シリーズを選択</Typography>
        </GridListTile>
        {seriesList.map(item => (
          <GridListTile cols={1}>
            <Button variant="contained" color="primary"
            onClick = {() => { this.setState({viewMode: "SERIES_SELECTED_VIEW", selectedSeries: item["name"]}) }}>
              {item["name"]}
            </Button>
          </GridListTile>
      ) )}
      </GridList>
    );
  }

  renderModelSelect = (modelList) => {
    var cols = modelList.length < 3 ? modelList.length : 3
    return (
      <GridList cols={cols} cellHeight={50}>
      <GridListTile cols={cols}>
        <Typography variant="h6">機種を選択</Typography>
      </GridListTile>
        {modelList.map(item => (
          <GridListTile cols={1}>
            <Button variant="contained" color="primary" style={{margin: "auto"}}
            onClick = {() => { this.setState({viewMode: "REPORT_VIEW", selectedModel: item["name"]}) }}>
              {item["name"]}
            </Button>
          </GridListTile>
      ) )}
      </GridList>
    );
  }

  renderReport = (model) => {
    return (
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Typography variant="h6">『{model}』の楽天SIMの利用可否</Typography>
        </Grid>
        <Grid item xs={4}>
          {this.renderAnswerButton(model, "yes")}
        </Grid>
        <Grid item xs={4}>
          {this.renderAnswerButton(model, "no")}
        </Grid>
        <Grid item xs={12}>
          <TextField label="コメント欄（自由投稿、最大128文字）"
          fullWidth multiline rows={10} variant="outlined">
          </TextField>
        </Grid>
      </Grid>
    );
  }

  renderSummury = () => {
    return (
      <div>
        SUMMURY
        {this.renderNavigateButton("TOP_VIEW", "TOP_VIEW", "")}
      </div>
    );
  }

  renderBody = () => {
    switch (this.state["viewMode"]) {
      case "TOP_VIEW":
        return this.renderModeSelect();

      case "SERIES_SELECTING_VIEW":
        return this.renderSeriesSelect(SERIES_LIST);

      case "SERIES_SELECTED_VIEW":
        if (this.state["taskMode"] === "REPORT_TASK") {
          this.setState({ viewMode: "MODEL_SELECTING_VIEW" })
        }
        else {
          this.setState({ viewMode: "SUMMURY_VIEW" })
        }
        break;

      case "MODEL_SELECTING_VIEW":
        var modelList = MODEL_LIST.filter((item => { return item["series"] === this.state["selectedSeries"] }));
        return this.renderModelSelect(modelList);

      case "REPORT_VIEW":
        return this.renderReport(this.state["selectedModel"]);

      case "SUMMURY_VIEW":
        return this.renderSummury();

      default:
        break;
    }
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

      <Grid container spacing={2}>
        <Grid item xs={12} container spacing={1}>
          <AppBar position="static">
            <Toolbar>
              <IconButton edge="start" className="{classes.menuButton}" color="inherit" aria-label="menu"
              onClick={() => {this.setState({viewMode: "TOP_VIEW"})} }>
                <Typography variant="h6" className="{classes.title}">
                  みんなの楽天SIM
                </Typography>
              </IconButton>
            </Toolbar>
          </AppBar>
        </Grid>
        <Grid item xs={12} style={{margin: "30px"}}>
          {this.renderBody()}
        </Grid>

        <Grid item xs={12} style={{margin: "30px 0"}}>
          test tools
          <Button variant="contained"
            onClick={()=>this.onClearCookie()}>
            Clear Cookie
          </Button>
        </Grid>
      </Grid>
    );
  }
}

function mapStateToProps(state) {
  const { spots, isLoading, error } = state.spots;
  return { spots, isLoading, error };
}

export default connect(mapStateToProps)(App);
