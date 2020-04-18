const BASE_URL = "http://18.216.105.170/api/";
//const BASE_URL = "http://localhost:8000/api/";

async function sendJson(url, method="GET", data={}) {
  param = {
    mode: "cors",
    method: method,
    headers: {
      "Content-Type": "application/json"
    },
  }

  if (method != "GET") {
    param.body = JSON.stringify(data);
  }

  const res = await fetch(BASE_URL + url, param);
  return await res.json();
}


/**
 * シリーズ一覧を取得する
 * @return {Object} シリーズオブジェクトの配列
 */
async function getSerieses() {
  return sendJson("serieses/");
}

/**
 * 指定シリーズの機種一覧を取得する
 * @param {number} seriesId シリーズID
 * @return {object} 機種オブジェクトの配列
 */
async function getDevices(seriesId) {
  return sendJson("serieses/" + seriesId + "/get_related_devices/");
}

/**
 * 指定シリーズの使用可否集計値を取得する
 * @param {number} seriesId シリーズID
 * @return {Object} 機種別の使用可否集計結果の配列
 */
async function countReports(seriesId) {
  return sendJson("serieses/" + seriesId + "/count_related_reports/");
}

/**
 * 指定機種のコメント一覧を取得する
 * @param {number} deviceId 機種のID
 * @return {Object} 使用可否別のコメント情報の配列
 */
async function analyzeReports(deviceId) {
  return sendJson("devices/" + deviceId + "/get_related_comments/");
}

/**
 * 使用可否情報を投稿する
 * @param {string} userId ユーザーID
 * @param {boolean} usable 使用可否
 * @param {string} commnet コメント
 * @param {number} deviceId デバイスID
 */
async function postReport(userId, usable, comment, deviceId) {
  data = {
    "user_id": userId,
    "usable": usable,
    "comment": comment,
    "device": deviceId,
    "product": 1
  };

  sendJson("rakutensim/reports/", "POST", data);
}
