const initialState = {
  spots: [],
  isLoading: false,
  error: null,
};

export default function spots(state = initialState, action) {
  switch (action.type) {
    case 'FETCH_SPOTS_STARTED': {
      return {
        ...state,
        isLoading: true,
      };
    }
    case 'FETCH_SPOTS_SUCCEEDED': {
      return {
        ...state,
        spots: action.payload.spots,
        isLoading: false,
      };
    }
    case 'FETCH_SPOTS_FAILED': {
      return {
        ...state,
        isLoading: false,
        error: action.payload.error,
      };
    }
    case 'CREATE_TASK_SUCCEEDED': {
      return {
        ...state,
        spots: state.spots.concat(action.payload.task),
      };
    }
    case 'EDIT_TASK_SUCCEEDED': {
      const { payload } = action;
      const nextSpots = state.spots.map(task => {
        if (task.id === payload.task.id) {
          return payload.task;
        }

        return task;
      });
      return {
        ...state,
        spots: nextSpots,
      };
    }
    case 'DELETE_TASK_SUCCEEDED': {
      const { payload } = action;
      const nextSpots = state.spots.filter(task => task.id !== payload.id)
      return {
        ...state,
        spots: nextSpots,
      };
    }
    default: {
      return state;
    }
  }
}
