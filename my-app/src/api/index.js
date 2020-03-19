import axios from 'axios';

// const API_BASE_URL = 'http://www.mypress.jp:3003'; // json-server用
// const API_BASE_URL = 'http://www.mypress.jp:8080'; // Django用
const API_BASE_URL = 'http://127.0.0.1:8000';

const client = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  },
});

export function fetchSpots() {
  var res = client.get('/api/spots/');
  console.log(res)
  return res
}

export function createSpot(params) {
  console.log(params)
  return client.post('/api/spots/', params);
}

export function editSpot(id, params) {
  return client.put(`/api/${id}`, params);
}

export function deleteSpot(id) {
  return client.delete(`/api/spots/${id}/`);
}
