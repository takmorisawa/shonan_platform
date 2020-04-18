// var url = "http://18.216.105.170/api/simreports/rakuten/";
var url = "http://localhost:8000/api/rakutensim/reports/";

async function getReports() {
  const res = await fetch(url, {
    mode: "cors",
    method: "GET",
  });
  const json = await res.json();
  return json;
}

async function postReport(userId, usable, comment) {
  const res = await fetch(url, {
    mode: "cors",
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      "user_id": userId,
      "usable": usable,
      "comment": comment,
      "device": 1,
      "product": 1
    })
  });
}

async function analyzeReports() {
  const json = await getReports();
  ret = {};

  const yesList = json.filter((item) => {
    return item["usable"];
  });

  const noList = json.filter((item) => {
    return !item["usable"];
  });

  return { "yes": yesList, "no": noList }
}
