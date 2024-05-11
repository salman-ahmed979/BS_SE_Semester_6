<?php

// Fetching User inputs
$serverName = $_POST["serverName"];
$userName = $_POST["userName"];
$password = $_POST["password"];
$SQLDataBase = $_POST["databaseName"];
$SQLQuery = $_POST["sqlQuery"];

$connection = null;
if (empty($SQLDataBase)) {
    // creating connection
    $connection = new mysqli($serverName, $userName, $password);
}
else {
    $connection = new mysqli($serverName, $userName, $password, $SQLDataBase);
}

if (!$connection) {
    die("Connection Failed! " . mysqli_connect_error());
}

if (empty($SQLQuery)) {
    echo "<h1>No Query is provided</h1>";    
}
else {
    // Executing Query
    $queryResult = mysqli_query($connection, $SQLQuery);
    if(!empty($queryResult)) {
        echo "<h1>Query Executed Successfully</h1>";
        echo "<p>SQL Query Result: $queryResult</p>";
    }
}

mysqli_close($connection);

echo "<p><a href='index.html'>Click to proceed to Website</p>";

?>
