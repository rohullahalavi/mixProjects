

//connect to sql database 
$db = mysqli_connect("localhost", "root", "", "test");

//create simle html form to enter data 
echo "<form action='php.php' method='post'>";
echo "Enter a number: <input type='text' name='num1'><br>";
echo "Enter another number: <input type='text' name='num2'><br>";
echo "<input type='submit' value='Add' name='add'>";
echo "<input type='submit' value='Subtract' name='subtract'>";
echo "<input type='submit' value='Multiply' name='multiply'>";
echo "<input type='submit' value='Divide' name='divide'>";
echo "</form>";







