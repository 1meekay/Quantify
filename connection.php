<?php

$host = "localhost";
$dbusername = "test_proj";
$dbpassword = "projtest";
$dbname = "test_companies";

# create connection
$conn = new mysqli($host, $dbusername, $dbpassword, $dbname) or die("Couldn't connect to database..".mysqli_connect_error());

mysqli_set_charset($conn, "utf8");
?>
