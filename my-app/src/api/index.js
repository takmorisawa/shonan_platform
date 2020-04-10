import axios from 'axios';

const API_BASE_URL = 'http://18.216.105.170';
const API_PATH = '/api';
// const API_BASE_URL = 'http://127.0.0.1:8000';
// const API_PATH = '';

const client = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  },
});

export function fetchSpots() {
  var res = client.get(API_PATH + '/spots/');
  console.log(res)
  return res
}

export function createSpot(params) {
  return client.post(API_PATH + '/spots/', params);
}

export function editSpot(id, params) {
  return client.put(API_PATH + '/pots/${id}', params);
}

export function deleteSpot(id) {
  return client.delete(API_PATH + '/spots/${id}/');
}
