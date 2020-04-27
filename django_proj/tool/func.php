<?php
// const BASE_URL = 'http://localhost:8000/api/';
const BASE_URL = 'http://18.216.105.170/api/';
const AUTH_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTg3Mjc2MTY2LCJlbWFpbCI6IiJ9.xpO7uGD3Nw1CgeU2ephLf0xJcTEGOlDMGHGZXx9QsqQ";

function sendJson($url, $method = "GET", $argary = array()) {
  $query_string = json_encode($argary);
  $options = array (
     'http' => array (
         'method' => $method,
         'header' => 'Content-type: application/json',
         'content' => $query_string,
         'ignore_errors' => true,
         'protocol_version' => '1.1'
         ),
     'ssl' => array (
         'verify_peer' => false,
         'verify_peer_name' => false
         )
     );
  $contents = @file_get_contents(BASE_URL . $url, false, stream_context_create($options));
  return $contents;
}

function sendJson_($url, $method = "GET", $argary = array()) {
  $headers = [
      'Content-type: application/json',
  ];

  $curl = curl_init(htmlspecialchars_decode($url));
  curl_setopt_array($curl, [
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => $headers
  ]);

  $json = curl_exec($curl);
  return $json;
}

/**
 * シリーズ一覧を取得する
 * @return {Object} シリーズオブジェクトの配列
 */
function getSerieses() {
  return sendJson("serieses/");
}

/**
 * 指定シリーズの機種一覧を取得する
 * @param {number} seriesId シリーズID
 * @return {object} 機種オブジェクトの配列
 */
function getDevices($seriesId) {
  return sendJson("serieses/" . $seriesId . "/get_related_devices/");
}

/**
 * 使用可否情報を投稿する
 * @param {string} userId ユーザーID
 * @param {boolean} usable 使用可否
 * @param {string} commnet コメント
 * @param {number} deviceId デバイスID
 */
function postReport($userId, $usable, $comment, $deviceId) {
  $data = array(
    "user_id" => $userId,
    "usable" => $usable,
    "comment" => $comment,
    "device" => $deviceId,
    "product" => 1);
  return sendJson("rakutensim/reports/", "POST", $data);
}

/**
 * 指定シリーズの使用可否集計値を取得する
 * @param {number} seriesId シリーズID
 * @return {Object} 機種別の使用可否集計結果の配列
 */
function countReports($seriesId) {
  return sendJson("serieses/" . $seriesId . "/count_related_reports/");
}

/**
 * 指定機種のコメント一覧を取得する
 * @param {number} deviceId 機種のID
 * @return {Object} 使用可否別のコメント情報の配列
 */
function getReports($deviceId) {
  return sendJson("devices/" . $deviceId . "/get_related_comments/");
}
?>
