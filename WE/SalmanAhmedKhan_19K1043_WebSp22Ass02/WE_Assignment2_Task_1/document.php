<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recheck Login</title>
</head>
<body>
    <?php
        session_start();
        if ($_SESSION["Login"] == false) {
            header("Location: Login.html");
        }
    ?>
    <h1>
        This is Protected File
    </h1>
    <p>This Document require Login as Requirement</p>
</body>
</html>