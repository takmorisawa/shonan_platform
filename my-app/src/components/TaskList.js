import React from 'react';
import { Button, List, ListItem, Card, CardContent } from '@material-ui/core'
import { MuiThemeProvider } from 'material-ui/styles'
import { theme } from '../theme'
import { TASK_STATUSES } from '../constants';

const TaskList = props => {
  return (
    <MuiThemeProvider theme={theme}>
    <List>
        {props.spots.map(item => (
          <ListItem>
            <Card style={{minWidth:"600px"}}>
              <CardContent>
                {item.name}
              </CardContent>
              <CardContent>
                {item.address}
              </CardContent>
              <Button variant="contained" color="primary"　style={{margin:"15px"}}
              onClick={()=>{props.onDeleteSpot(item.id)}}>
              投稿削除
              </Button>
            </Card>
          </ListItem>
        ))}
    </List>
    </MuiThemeProvider>
  );
};

export default TaskList;
