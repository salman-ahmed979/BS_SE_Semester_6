<!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Engineering Assignment 2</title>
    <style>
        fieldset {
            width: 40%;
        }
        legend {
            font-size: 1.5em;
            font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        }
        input, select {
            border: 2px solid grey;
            width: 100%;
            height: 25px;
            margin-left: 3px;
            border-radius: 1em;
            margin-bottom: 8px;
        }
        button {
            width: 100%;
            margin-top: 1em;
            text-align: center;
            padding: 0.8em;
            margin-bottom: 0.4em;
            border: none;
            border-radius: 1em;
            background-color: black;
            color: aliceblue;
            cursor: pointer;
        }
        button:hover {
            background-color: #555;
        }
    </style>
</head>
<body>
    <div>
        <form action="" method="post">
            <fieldset>
                <legend>Calculator PHP</legend>
                <table>
                    <tr>
                        <td>Enter First Number: </td>
                        <td>
                            <input type="number" name="firstNumber" min="0" required>
                        </td>
                    </tr>
                    <tr>
                        <td>Select Operator: </td>
                        <td>
                            <select name="operator" required>
                                <option value="+" selected>+</option>
                                <option value="-">-</option>
                                <option value="*">*</option>
                                <option value="/">/</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>Enter Second Number: </td>
                        <td>
                            <input type="number" name="secondNumber" min="0" required>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><button type="submit">Calculate</button></td>
                    </tr>
                </table>
            </fieldset>
        </form>
    </div>
    <div>     </div>
 </body>
 </html> -->


        <?php
        
        function addition($num1, $num2) {
            return $num1 + $num2;
        }

        function subtraction($num1, $num2) {
            return $num1 - $num2;
        }

        function multiplication($num1, $num2) {
            return $num1 * $num2;
        }

        function division($num1, $num2) {
            if ($num2 == 0) return -1;
            return $num1 / $num2;
        }

        if(isset($_POST["firstNumber"])) {
            $firstNumber = $_POST["firstNumber"];
            $operator = $_POST["operator"];
            $secondNumber = $_POST["secondNumber"];
            $result = null;
            switch($operator)
            {
                case "+":
                    $result = addition($firstNumber, $secondNumber);
                    break;
                case "-":
                    $result = subtraction($firstNumber, $secondNumber);
                    break;
                case "*":
                    $result = multiplication($firstNumber, $secondNumber);
                    break;
                case "/":
                    $result = division($firstNumber, $secondNumber);
                    break;
            }
            // Output
            echo "<h4 style='display: inline;'>Calculated Answer: </h4><span><b>$result</b></span>";
        }
        ?>