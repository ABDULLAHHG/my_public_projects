
<?php
$servername = "localhost";
$username = "root";
$password = "1234";
$databasename = "company2";
$conn = new mysqli($servername, $username, $password , $databasename);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


$sql = "insert employee (employee , department , password) values ('aboud' , 'cs' , '1234');";

if ($conn->query($sql) === TRUE) {
    echo "record created successfully";
} else {
    echo "Error creating record: " . $conn->error;
}

$conn->close();
?>