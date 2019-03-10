 <?php

$companyName = $_POST['companyName'];
$location = $_POST['location'];
$industry = $_POST['industry'];
$totalRevenue = $_POST['totalRev'];
$priorRevenue = $_POST['priorRev'];
$cogs = $_POST['cogs'];
$opExpenses = $_POST['opExpenses'];
$cashBalance = $_POST['cashBalance'];
$currentAssets = $_POST['cAssets'];
$currentLiabilities = $_POST['cLiabilities'];
$longtermLiabilities = $_POST['ltLiabilities'];
$ownerSat = $_POST['ownerSat'];
$employeeSat = $_POST['employeeSat'];
$newCustomers = $_POST['newCustomers'];
$startCustomers = $_POST['startCustomers'];
$endCustomers = $_POST['endCustomers'];
$rewardsProgram = $_POST['rewardsProgram'];
$totalInventory = $_POST['totalInventory'];
$deadInventory = $_POST['deadInventory'];
$expansion = $_POST['expansion'];

include("connection.php");
$sql = "INSERT INTO companies_table (company_name, location, industry, total_revenue, prior_revenue, cogs, op_expenses, cash_balance, current_assets, current_liabs, long_term_liabs, owner_sat, employee_sat, new_customers, start_customers, end_customers, rewards_program, total_inventory, dead_inventory, expansion)
VALUES ('$companyName', '$location', '$industry', '$totalRevenue', '$priorRevenue', '$cogs', '$opExpenses', '$cashBalance', '$currentAssets', '$currentLiabilities', '$longtermLiabilities', '$ownerSat', '$employeeSat', '$newCustomers', '$startCustomers', '$endCustomers', '$rewardsProgram', '$totalInventory', '$deadInventory', '$expansion')";

if ($conn->query($sql) == TRUE){
  echo "Information successfully added.";
} else {
  echo "Error, something went wrong!";
}
?>
