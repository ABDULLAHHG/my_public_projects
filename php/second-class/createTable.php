
<?php
$servername = "localhost";
$username = "root";
$password = "1234";
$databasename = "company2";
$conn = new mysqli($servername, $username, $password , $databasename);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


$sql = "create table employee (
    id int auto_increment primary key,
    employee varchar(255) not null,
    department varchar(255) not null,
    password varchar(255) not null,
    date datetime default current_timestamp
);";

if ($conn->query($sql) === TRUE) {
    echo "Table created successfully";
} else {
    echo "Error creating Table: " . $conn->error;
}

$conn->close();
?>