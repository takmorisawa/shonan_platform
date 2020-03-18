import React from 'react';
import { List, ListItem, Card, CardContent } from '@material-ui/core'
import { TASK_STATUSES } from '../constants';


const TaskList = props => {
  return (
    <List>
        {props.tasks.map(item => (
          <ListItem>
            <Card>
              <CardContent>
                {item.name}
              </CardContent>
              <CardContent>
                {item.address}
              </CardContent>
            </Card>
            {/*<select value={item.status} onChange={(e) => {onStatusChange(e, item.id)}}>
              {TASK_STATUSES.map(status => (
                <option key={status} value={status}>{status}</option>
              ))}
            </select>
            <Button type="danger" onClick={()=>{props.onDeleteTask(item.id)}}>
              タスク削除
            </Button>*/}
          </ListItem>
        ))}
    </List>
  );

  function onStatusChange(e, id) {
    props.onStatusChange(id, e.target.value);
  }
};

export default TaskList;
