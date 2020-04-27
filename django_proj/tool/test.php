<?php

include "func.php";

$seriesId = 1;
$deviceId = 1;

if ($_SERVER['REQUEST_METHOD'] === 'POST'){
  $seriesId = $_POST["series_id"];
  $deviceId = $_POST["device_id"];
}

$serieses = getSerieses();
$devices = getDevices($seriesId);
$countby = countReports($seriesId);
$reports = getReports($deviceId);

// echo "<pre>";
// var_dump($countby);
// echo "</pre>";
?>

<!DOCTYPE html>
<html lang="ja" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <form class="" method="post">

      <!-- series table -->
      <div class="" style="margin: 10px 0">
        <h3>get serieses:</h3>
        <table id="series_table" border="1">
          <thead>
            <tr>
              <td>id</td>
              <td>name</td>
            </tr>
          </thead>
        </table>
      </div>

      <h3>count by series:</h3>

      <label for="">series id: </label>
      <input type="text" name="series_id" value="<?php echo $seriesId; ?>">
      <input type="submit" name="" value="update">
      <br>

      <!-- count table -->
      <div class="" style="margin: 10px 0">
        <table id="count_table" border="1">
          <thead>
            <tr>
              <td>id</td>
              <td>name</td>
              <td>yes</td>
              <td>no</td>
            </tr>
          </thead>
        </table>
      </div>

      <h3>get reports:</h3>

      <label for="">device id: </label>
      <input type="text" name="device_id" value="<?php echo $deviceId; ?>">
      <input type="submit" name="" value="update">

      <!-- yes table -->
      <div class="" style="margin: 10px 0">
        <label>yes reports:</label>
        <table id="yes_table" border="1">
          <thead>
            <tr>
              <td>user_id</td>
              <td>date</td>
              <td>comment</td>
            </tr>
          </thead>
        </table>
      </div>

      <!-- no table -->
      <div class="" style="margin: 10px 0">
        <label>no repots:</label>
        <table id="no_table" border="1">
          <thead>
            <tr>
              <td>user_id</td>
              <td>date</td>
              <td>comment</td>
            </tr>
          </thead>
        </table>
      </div>

    </form>

    <form class="" action="view.php" method="post" style="border: thin solid">
      <h3>post report:</h3>

      <label>user_id:</label>
      <input type="text" name="user_id" value="test_user_id">
      <br>

      <label>yes/no:</label>
      <input type="checkbox" name="usable" checked>
      <br>

      <label>commnet:</label>
      <input type="text" name="comment" value="this is a test comment.">
      <br>

      <input type="submit" value="post report" style="margin: 10px 0"/>

    </form>

    <!-- template -->
    <template id="template" style="">
      <tr>
        <td></td><td></td><td></td>
      </tr>
    </template>

    <!-- template -->
    <template id="template2" style="">
      <tr>
        <td></td><td></td><td></td><td></td>
      </tr>
    </template>

    <!-- script for creating table -->
    <script type="text/javascript">

      var template = document.getElementById("template");

      var func = (list, table) => {
        list.forEach((item) => {
          const clone = document.importNode(template.content, true);
          const td = clone.querySelectorAll("td");
          td[0].textContent = item["user_id"];
          td[1].textContent = item["date"];
          td[2].textContent = item["comment"];
          table.appendChild(clone);
        });
      };

      var result = JSON.parse('<?php echo $reports; ?>');

      var yesList = result["yes"];
      var yesTable = document.getElementById("yes_table");
      func(yesList,yesTable);

      var noList = result["no"];
      var noTable = document.getElementById("no_table");
      func(noList,noTable);

    </script>

    <script type="text/javascript">

      var table = document.getElementById("series_table");
      var list = JSON.parse('<?php echo $serieses; ?>');
      list.forEach((item) => {
        var tr = document.createElement("tr");
        var td1 = document.createElement("td");
        var td2 = document.createElement("td");
        td1.textContent = item["id"];
        td2.textContent = item["name"];
        tr.appendChild(td1);
        tr.appendChild(td2);
        table.appendChild(tr);
      });

    </script>

    <script type="text/javascript">

      var table = document.getElementById("count_table");
      var template = document.getElementById("template2");
      var list = JSON.parse('<?php echo $countby; ?>');
      list.forEach((item) => {
        const clone = document.importNode(template.content, true);
        const td = clone.querySelectorAll("td");
        td[0].textContent = item["device_id"];
        td[1].textContent = item["device_name"];
        td[2].textContent = item["yes"];
        td[3].textContent = item["no"];
        table.appendChild(clone);
      });

    </script>
  </body>
</html>
