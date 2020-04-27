<?php

include "func.php";

if ($_SERVER['REQUEST_METHOD'] === 'POST'){
  $userId = $_POST['user_id'];
  $usable = isset($_POST['usable']) ? true : false;
  $comment = $_POST['comment'];
  $result = postReport($userId, $usable, $comment, 1);
  //echo $result;
  header('Location: http://'.$_SERVER['HTTP_HOST'].dirname($_SERVER['PHP_SELF']).'/test.php');
  exit();
}
