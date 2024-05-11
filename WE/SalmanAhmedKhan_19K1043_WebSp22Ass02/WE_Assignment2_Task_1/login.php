<?php
session_start();

// Check username and password are correct
if ($_POST["userName"] == "Salman" && $_POST["password"] == "19K1043") {
    $_SESSION["Login"] = true;
    echo "<h4>You are Logged In Successfully</h4>";
    echo "<p><a href='document.php'>Link to Protected File</p>";
}
else {
    $_SESSION["Login"] = false;
    echo "<h4>Logged In Failed<br>Kindly click below</h4>";
    echo "<p><a href='document.php'>Link to Protected File</p>";
}
?>