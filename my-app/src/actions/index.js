import * as api from '../api';

function fetchSpotsSucceeded(spots) {
  return {
    type: 'FETCH_SPOTS_SUCCEEDED',
    payload: {
      spots,
    },
  };
}

function fetchSpotsFailed(error) {
  return {
    type: 'FETCH_SPOTS_FAILED',
    payload: {
      error,
    },
  };
}

function fetchSpotsStarted() {
  return {
    type: 'FETCH_SPOTS_STARTED',
  };
}

export function fetchSpots() {
  return dispatch => {
    dispatch(fetchSpotsStarted());

    api
      .fetchSpots()
      .then(resp => {
        dispatch(fetchSpotsSucceeded(resp.data));
      })
      .catch(err => {
        dispatch(fetchSpotsFailed(err.message));
      });
  };
}

function createSpotSucceeded(task) {
  return {
    type: 'CREATE_TASK_SUCCEEDED',
    payload: {
      task,
    },
  };
}

export function createSpot({ name, address }) {
  return dispatch => {
    api.createSpot({ name, address }).then(resp => {
      dispatch(createSpotSucceeded(resp.data));
    });
  };
}

function editSpotSucceeded(task) {
  return {
    type: 'EDIT_TASK_SUCCEEDED',
    payload: {
      task,
    },
  };
}

export function editSpot(id, params = {}) {
  return (dispatch, getState) => {
    const task = getTaskById(getState().spots.spots, id);
    const updatedTask = Object.assign({}, task, params);
    api.editSpot(id, updatedTask).then(resp => {
      dispatch(editSpotSucceeded(resp.data));
    });
  };
}


function getTaskById(spots, id) {
  return spots.find(task => task.id === id);
}


function deleteSpotSucceeded(id) {
  return {
    type: 'DELETE_TASK_SUCCEEDED',
    payload: {
      id,
    },
  };
}

export function deleteSpot(id) {
  return (dispatch, getState) => {
    api.deleteSpot(id).then(resp => {
      console.log(resp)
      dispatch(deleteSpotSucceeded(id));
    });
  };
}
