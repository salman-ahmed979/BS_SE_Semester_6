<!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Engineering Assignment 2</title>
</head>

<body>
    <h2>Calculate Electricity Bill - PHP</h2>
    <div>
        <form action="" method="POST">
            <input type="number" min="1" name="Eunit" placeholder="Please enter no. of Units">
            <button type="submit">Submit</button>
        </form>
    </div>
    <div>     </div>
</body>
</html>-->
    <?php
    $result_str = $result = '';
    if (isset($_POST['Eunit'])) {
        $units = $_POST['Eunit'];
        if (!empty($units)) {
            $result = calculate_bill($units);
            $result_str = 'Total amount of ' . $units . ' units are - Rs. ' . $result;
        }
    }
    
    function calculate_bill($units) {
        $unit_cost_first = 3.50;
        $unit_cost_second = 4.00;
        $unit_cost_third = 5.20;
        $unit_cost_fourth = 6.50;
    
        if($units <= 50) {
            $bill = $units * $unit_cost_first;
        }
        else if($units > 50 && $units <= 100) {
            $temp = 50 * $unit_cost_first;
            $remaining_units = $units - 50;
            $bill = $temp + ($remaining_units * $unit_cost_second);
        }
        else if($units > 100 && $units <= 200) {
            $temp = (50 * 3.5) + (100 * $unit_cost_second);
            $remaining_units = $units - 150;
            $bill = $temp + ($remaining_units * $unit_cost_third);
        }
        else {
            $temp = (50 * 3.5) + (100 * $unit_cost_second) + (100 * $unit_cost_third);
            $remaining_units = $units - 250;
            $bill = $temp + ($remaining_units * $unit_cost_fourth);
        }
        return number_format((float)$bill, 2, '.', '');
    }
    echo "<p>$result_str</p>";
    ?>
